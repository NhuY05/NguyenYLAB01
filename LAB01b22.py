# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:06:32 2024

@author: Vivobook
"""

a = float(input("Nhập vào a: "))
b = float(input("Nhập vào b: "))

if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -(b/a)
    print("Phương trình có nghiệm duy nhất: ", x)