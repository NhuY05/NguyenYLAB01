# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:35:29 2024

@author: Vivobook
"""
import random
print("Câu a: ")
songuyena = random.randint(0, 100)
sothuca = random.uniform(0, 100)
print("Số nguyên ngẫu nhiên [0, 100]: ", songuyena)
print("Số thực ngẫu nhiên [0, 100]: ", sothuca)

print("Câu b: ")
songuyenb = random.randint(50, 99)
sothucb = random.uniform(50, 99)
print("Số nguyên ngẫu nhiên [50, 99]: ", songuyenb)
print("Số thực ngẫu nhiên [50, 99]:", sothucb)

print("Câu c: ")
songuyenc = random.randint(-39, 79)
sothucc = random.uniform(-39, 79)
print("Số nguyên ngẫu nhiên [-39, 79]: ", songuyenc)
print("Số thực ngẫu nhiên [-39, 79]: ", sothucc)

print("Câu d: ")
songuyend = random.randint(-79, -39)
sothucd = random.uniform(-79, -39)
print("Số nguyên ngẫu nhiên [-79, -39]: ", songuyend)
print("Số thực ngẫu nhiên [-79, -39]: ", sothucd)