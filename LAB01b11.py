# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:12:43 2024

@author: NguyenY
"""
chuthuong = input("Nhập 1 ký tự chữ thường: ")
if chuthuong.islower() and len(chuthuong) == 1:
    chuhoa = chuthuong.upper()
    print("Kí tự chữ hoa tương ứng: ", chuhoa)
else:
    print("Vui lòng nhập 1 kí tự là chữ thường")