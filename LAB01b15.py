# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:55:55 2024

@author: Vivobook
"""

a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))
a1 = pow(a, 1/3)
b1 = pow(b, 1/3)
c = pow(a * b, 1/3)
print((((a + b) / (a1 + b1 )) - c) / ((a1 - b1) ** 2))