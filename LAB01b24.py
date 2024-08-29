# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:11:29 2024

@author: Vivobook
"""
print("b24")
a = int(input("Nhập số giờ: "))
b = int(input("Nhập phút: "))
c = int(input("Nhập giây: "))
if a < 24 and b < 60 and c < 60:
    print("Thời gian hợp lệ")
else: 
    print("Thời gian không hợp lệ")