# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:19:56 2024

@author: Vivobook
"""

h1 = int(input("Nhập giờ thứ nhất: "))
m1 = int(input("Nhập phút thứ nhất: "))
s1 = int(input("Nhập giây thứ nhất: "))

h2 = int(input("Nhập giờ thứ hai: "))
m2 = int(input("Nhập phút thứ hai: "))
s2 = int(input("Nhập giây thứ hai: "))

if h1 > 24 and m1 > 60 and s1 > 60:
    print("Thời gian không hợp lệ")
if h2 > 24 and m2 > 60 and s2 > 60:
    print("Thời gian không hợp lệ")
    
tonggiayh1 = h1 * 3600
tonggiaym1 = m1 * 60
tong1 = tonggiayh1 + tonggiaym1 + s1

tonggiayh2 = h2 * 3600
tonggiaym2 = m2 * 60
tong2 = tonggiayh2 + tonggiaym2 + s2

if tong1 > tong2:
    ketqua = tong1 - tong2
    gioketqua = ketqua // 3600
    phutketqua = (ketqua % 3600) // 60
    giayketqua = (ketqua % 3600) % 60
    print("Kết quả: ",gioketqua, "giờ", phutketqua, "phút", giayketqua,"giây")
    
else:
    ketqua = tong2 - tong1
    gioketqua = ketqua // 3600
    phutketqua = (ketqua % 3600) // 60
    giayketqua = (ketqua % 3600) % 60
    print("Kết quả: ",gioketqua, "giờ", phutketqua, "phút", giayketqua,"giây")