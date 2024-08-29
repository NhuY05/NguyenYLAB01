# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:05:26 2024

@author: NguyenY
"""
print("Cách 1: ")
soxe = input("Nhập số xe của bạn: ")
if len(soxe) == 4 and soxe.isdigit():
    tong = sum(int(chuso) for chuso in soxe)
    sonut = tong % 10
    print("Tổng số nút là: ", sonut)
else:
    print("Vui lòng nhập 4 số: ")

print("Cách 2: ")
soxe = input("Nhập số xe của bạn: ")
if len(soxe) == 4 and soxe.isdigit():
    tong = sum(int(chuso) for chuso in soxe)
    a = tong // 10
    b = tong % 10
    sonut = a + b
    print("Tổng số nút: ", sonut)
else:
    print("Vui lòng nhập 4 số: ")