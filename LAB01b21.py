# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:24:03 2024

@author: Vivobook
"""
a = int(input("Nhập 1 số bất kì: "))
list = ["không", 'một', 'hai', 'ba', 'bốn','năm', 'sáu', 'bảy', 'tám', 'chín']
if 0<=a<=9:
    print(list[a])
else:
    print("Không đọc được")