# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe
import sys

sys.setrecursionlimit(10000000)

includes = ["requests","requests_toolbelt","pdfkit"] #"encodings", "encodings.*",
options = {"py2exe": 
            {   "compressed": 1, 
                "optimize": 2, 
                "includes": includes, 
                "bundle_files": 1 
            } 
          } 
setup(    
    version = "0.1.0", 
    description = "ASWG Check You Internet ENV", 
    name = "aswgCheck", 
    options = options, 
    zipfile=None, 
    windows=[{"script": "aswg.py", "icon_resources": [(1, "./static/images/aswg.ico")] }],   
     
    ) 

#pyinstaller -F -w static/images/aswg.ico aswg.py
#https://blog.csdn.net/u014563989/article/details/80940321