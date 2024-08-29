# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:28:14 2024

@author: NguyenY
"""
hh = int(input("Nhập giờ: "))
mm = int(input("Nhập phút: "))
ss = int(input("Nhập giây: "))
thoigian = input('Nhập vào giờ, phút, giây có định dạng {} : {} : {}'.format(hh, mm, ss))
tonggiay = hh * 3600 + mm * 60 + ss
print("Tổng giây là: ", tonggiay)