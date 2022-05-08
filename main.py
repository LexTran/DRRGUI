from asyncio.windows_events import NULL
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QGridLayout
from DRRGUI import *
import matplotlib
matplotlib.use('TKAgg')
import numpy as np
from PIL import Image, ImageQt
import weakref
import nibabel as nib
from nibabel import nifti1
from nibabel.affines import voxel_sizes
from nibabel.optpkg import optional_package
from nibabel.orientations import aff2axcodes, axcodes2ornt

from matplotlib import pyplot as plt
from matplotlib import transforms as trans
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from genericpath import isfile
import logging
import os
from typing import Callable
from pathlib import Path
from rich.logging import RichHandler         # 终端美化工具
from time import time

import deepdrr
from deepdrr import geo
from deepdrr.utils import test_utils, image_utils
from deepdrr.projector import Projector

import pydrr
from pydrr import autoinit
import SimpleITK as sitk
import mpl_toolkits.axes_grid1
from pydrr import utils

from nibabel.viewers import OrthoSlicer3D

class MyClass(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyClass, self).__init__(parent)
        self.setupUi(self)
        self.Input.clicked.connect(self.openimage)
        self.Slicer3D.clicked.connect(self.OpenSlicer3D)
        self.DRRShow.clicked.connect(self.ShowDeepDRR)
        self.DRRShow_2.clicked.connect(self.ShowTraditionalDRR)
        self.Volume = None
        self.imgName = None

    def openimage(self):
        try:
            imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片","","*.nii.gz;;*.mhd;;*All Files(*)")
            self.imgName = imgName
            if imgType == ".mhd":
                try:
                    mhd2nii(imgName)
                except:
                    print("Convert .mhd to .nii failed!")
            try:
                self.Volume = nib.load(imgName)
                data = self.Volume.get_fdata()
                width, height, queue = self.Volume.dataobj.shape
                self.CTInfo.setText(f"CT volume size is {width} x {height} x {queue}")
            except:
                print("Read CT Wrong!")
        except:
            print("File path Wrong!")

    def OpenSlicer3D(self):
        data = self.Volume.get_fdata()

        try:
            OrthoSlicer3D(self.Volume.dataobj).show()
        except:
            print("OrthoSlicer3D Wrong!")

    def ShowDeepDRR(self):
        try:
            patient = deepdrr.Volume.from_nifti(self.imgName, use_thresholding=True)                                                                       # 指定输入图像，读取CT容积
            patient.faceup()

            # define the simulated C-arm
            carm = deepdrr.MobileCArm(
                patient.center_in_world,
                source_to_detector_distance = 1600,
                source_to_isocenter_vertical_distance = 1280,
                source_to_isocenter_horizontal_offset = 0,
                free_space = 820,
                sensor_height = 1536,
                sensor_width = 1536,
                pixel_size = 0.6,
            )

            with Projector(patient, 
                    carm=carm,
                    step=0.01,
                    spectrum='60KV_AL35', # Options are `'60KV_AL35'`, `'90KV_AL40'`, and `'120KV_AL43'`
                    photon_count=100000,
                    add_noise=True,
                    threads=8,
                ) as projector:
                    # carm.move_to(alpha=0, beta=-15)
                    image = projector()

            image = (image * 255).astype(np.uint8)
            img = Image.fromarray(image)
            qt_img = ImageQt.ImageQt(img)
            self.DeepDRRDisplay.setPixmap(QtGui.QPixmap.fromImage(qt_img).scaled(self.DeepDRRDisplay.width(), self.DeepDRRDisplay.height()))
            self.DeepDRRDisplay.show()
        except:
            print("DeepDRR Wrong!")

    def ShowTraditionalDRR(self):
        try:
            filename = self.imgName
            itkimage = sitk.ReadImage(filename)
            volume  = sitk.GetArrayFromImage(itkimage)
            spacing = itkimage.GetSpacing()
            spacing = spacing[::-1]
            pydrr.set_current_kernel('render_with_cubic_interp')
            volume = pydrr.utils.HU2Myu(volume - 1000, 0.2683)
            pm_Nx3x4, image_size, image_spacing = load_test_projection_matrix()
            T_Nx4x4 = load_test_transform_matrix()
            # Construct objects
            volume_context = pydrr.VolumeContext(volume.astype(np.float32), spacing)
            geometry_context = pydrr.GeometryContext()
            geometry_context.projection_matrix = pm_Nx3x4

            n_channels = T_Nx4x4.shape[0] * pm_Nx3x4.shape[0]
            detector = pydrr.Detector(pydrr.Detector.make_detector_size(image_size, n_channels), image_spacing)
            # detector = pydrr.Detector.from_geometry(geometry_context, T_Nx4x4) # You can use from_geometry if you set pixel_size and image_size.
            projector = pydrr.Projector(detector, 1.0).to_gpu()

            # Host memory -> (Device memory) -> Texture memory
            t_volume_context = volume_context.to_texture()
            d_image = projector.project(t_volume_context, geometry_context, T_Nx4x4)

            # Device memory -> Host memory
            image = d_image.get()
            print('Result image shape:', image.shape)
            plt.figure(figsize=(12,9))
            im = plt.imshow(image[:, :, 2], interpolation='none', cmap='gray')
            rot = trans.Affine2D().rotate_deg_around(image.shape[0]/2,image.shape[1]/2,90)
            im.set_transform(im.get_transform()+rot)
            plt.axis('off')
            plt.show()
            # save_image('drr.mhd', image, image_spacing)
            try: 
                image = np.transpose(image, (2,0,1))
                spacing = (*spacing[::-1], 1)
                itkimage = sitk.GetImageFromArray(image)
                itkimage.SetSpacing(spacing)
                qt_img = ImageQt.ImageQt(itkimage)
                self.TraditionalDRRDisplay.setPixmap(QtGui.QPixmap.fromImage(qt_img).scaled(self.TraditionalDRRDisplay.width(), self.TraditionalDRRDisplay.height()))
                self.TraditionalDRRDisplay.show()
            except:
                print("Show Traditional DRR Wrong!")
        except:
            print("Traditional DRR Wrong!")

def save_image(filename, image, spacing):
    image = np.transpose(image, (2,0,1))
    spacing = (*spacing[::-1], 1)
    itkimage = sitk.GetImageFromArray(image)
    itkimage.SetSpacing(spacing)
    sitk.WriteImage(itkimage, filename)

def mhd2nii(mhdfilename):
    # TODO: Convert mhd file to nii file
    pass

def load_test_projection_matrix(SDD=2000, SOD=1800, image_size=[1280, 1280], spacing=[0.287, 0.287] ):
    if isinstance(image_size, list):
        image_size = np.array(image_size)

    if isinstance(spacing, list):
        spacing = np.array(spacing)

    extrinsic_R = utils.convertTransRotTo4x4([[0,0,0,90,0,0],
                                              [0,0,0,0,90,0],
                                              [0,0,0,0,0,90]])

    # print('extrinsic_R:', extrinsic_R)
    # print('extrinsic_R.shape:', extrinsic_R.shape)

    extrinsic_T = utils.convertTransRotTo4x4([0,0,-SOD,0,0,0])

    # print('extrinsic_T:', extrinsic_T)
    # print('extrinsic_T.shape:', extrinsic_T.shape)

    extrinsic = utils.concatenate4x4(extrinsic_T, extrinsic_R)

    # print('extrinsic:', extrinsic)
    # print('extrinsic.shape:', extrinsic.shape)

    intrinsic = np.array([[-SDD/spacing[0], 0, image_size[0]/2.0], # unit: [pixel]
                          [0, -SDD/spacing[1], image_size[1]/2.0],
                          [0,                0,               1]])

    # print('intrinsic:', intrinsic)
    # print('intrinsic.shape:', intrinsic.shape)

    pm_Nx3x4 = utils.constructProjectionMatrix(intrinsic, extrinsic)
    # pm_Nx3x4 = np.repeat(pm_Nx3x4, 400, axis=0)

    # print('pm_Nx3x4:', pm_Nx3x4)
    # print('pm_Nx3x4.shape:', pm_Nx3x4.shape)

    return pm_Nx3x4, image_size, spacing

def load_test_transform_matrix(n_channels=1):
    T_Nx6 = np.array([0,0,0,90,0,0])
    T_Nx6 = np.expand_dims(T_Nx6, axis=0)
    T_Nx6 = np.repeat(T_Nx6, n_channels, axis=0)
    T_Nx4x4 = utils.convertTransRotTo4x4(T_Nx6)

    # print('T_Nx4x4:', T_Nx4x4)
    # print('T_Nx4x4.shape:', T_Nx4x4.shape)

    return T_Nx4x4

if __name__ == '__main__':
    log = logging.getLogger().handlers.clear()
    log = logging.getLogger('deepdrr')
    log.addHandler(RichHandler())
    log.setLevel(logging.INFO)

    os.environ['PATH'] += ';'+r"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64"
    os.environ['PATH'] += ';'+r"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\include"
    os.environ['PATH'] += ';'+r"D:\Program Files (x86)\Windows Kits\10\Include\10.0.19041.0\ucrt"
    if(os.system("cl.exe")):
        raise RuntimeError("cl.exe still not found, path probably incorrect")

    app = QApplication(sys.argv)
    myWin = MyClass()
    myWin.show()
    sys.exit(app.exec_())