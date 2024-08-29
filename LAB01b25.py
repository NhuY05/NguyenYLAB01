# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:44:50 2024

@author: Vivobook
"""

a = input("Nhập 1 chữ cái: ")
if a.islower() and len(a) == 1:
    
    print("Chữ hoa tương ứng: ", a.upper())
if a.upper() and len(a) == 1:
    
    print("Chữ thường: ", a.lower())

    