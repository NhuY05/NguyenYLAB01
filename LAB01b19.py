# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:11:54 2024

@author: Vivobook
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
d = int(input("Nhập số d: "))
nhonhat = a
if b < nhonhat:
    nhonhat = b
if c < nhonhat:
    nhonhat = c
if d < nhonhat:
    nhonhat = d
print("Số có giá trị nhỏ nhất là: ", nhonhat)
    
    
    