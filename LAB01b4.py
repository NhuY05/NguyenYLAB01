# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:20:17 2024

@author: NguyenY
"""

a = int(input("Nhập vào số nguyên a có 2 chữ số: "))
b = a//10
c = a%10
if 10 <= a <= 99:
    print("Tổng các chữ số: ", b + c)
  
else:
    print("Số không hợp lệ")