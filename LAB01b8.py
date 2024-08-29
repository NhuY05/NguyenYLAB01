# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:55:55 2024

@author: NguyenY
"""
cannang = float(input("Nhập cân nặng của bạn(kg): "))
chieucao = float(input("Nhập chiều cao của bạn(m): "))
BMI = cannang/(chieucao ** 2)
print("Số đo kiểm tra sức khỏe BMI của bạn: ", BMI)
