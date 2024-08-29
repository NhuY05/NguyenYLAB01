# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:10:12 2024

@author: Vivobook
"""
print("Bài 26a: ")
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print("Thứ tự tăng dần: ", a, b, c)

print("Bài 26b: ")
N = input("Nhập số nguyên: ")
dayso = "".join(sorted(N))
print("Dãy số theo thứ tự tăng dần: ", dayso)