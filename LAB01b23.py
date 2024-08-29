# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:12:28 2024

@author: Vivobook
"""
import math
a = float(input("Nhập vào a: "))
b = float(input("Nhập vào b: "))
c = float(input("Nhập vào c: "))
delta=float()
delta = (b**2) - (4*a*c)
if a == 0:
    print("Phương trình không phải pt bậc 2")
elif delta > 0:
    x1 = -b + math.sqrt(delta) / 2*a
    x2 = -b - math.sqrt(delta) / 2*a
    print("Phương trình có 2 nghiệm là: ",x1, x2)
elif delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x1=x2=", -b/2*a)