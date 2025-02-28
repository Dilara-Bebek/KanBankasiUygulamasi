# -*- coding: utf-8 -*-
"""
Created on Fri May 24 15:58:42 2024

@author: Dilara Bebek
"""

from PyQt5 import uic

with open('girisUI.py','w',encoding="utf-8") as fout:
    uic.compileUi('giris.ui',fout)
    
with open('anamenuUI.py','w',encoding="utf-8") as fout:
    uic.compileUi('anamenu.ui',fout)    
    
with open('kayitUI.py','w',encoding="utf-8") as fout:
    uic.compileUi('kayit.ui',fout)
