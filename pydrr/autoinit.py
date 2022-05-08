import pycuda.autoinit
from pydrr.KernelManager import initialize
import os

os.environ['PATH'] += ';'+r"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64"
os.environ['PATH'] += ';'+r"C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.29.30133\include"
os.environ['PATH'] += ';'+r"D:\Program Files (x86)\Windows Kits\10\Include\10.0.19041.0\ucrt"
if(os.system("cl.exe")):
    raise RuntimeError("cl.exe still not found, path probably incorrect")
    
initialize()
