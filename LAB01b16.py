# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:00:18 2024

@author: Vivobook
"""

gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
tonggiay = gio * 3600 + phut * 60 + giay
print("Tổng giây: ",tonggiay, "giây")
