# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:58:06 2024

@author: Vivobook
"""
a = int(input("Nhập ngày: "))
b = int(input("Nhập tháng: "))
c = int(input("Nhập năm: "))
ngaythangnam = input("Ngày tháng năm: {} {} {}".format(a, b, c))

print(a,"/",b,"/",c)
print(a, "/", b, "/", c%100)
print(c, "/", b, "/",a)