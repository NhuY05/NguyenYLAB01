# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:15:30 2024

@author: Vivobook
"""

a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
lonnhat = a
if b > lonnhat:
    lonnhat = b
if c > lonnhat:
    lonnhat = c
print("Số có giá trị lớn nhất:", lonnhat)