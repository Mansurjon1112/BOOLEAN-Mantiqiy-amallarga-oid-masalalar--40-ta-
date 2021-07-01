# -*- coding: utf-8 -*-
"""
Boolean35. Shaxmat doskasining ikkita turli (x1, y1), (x2, y2) koordinalari berilgan (1-8 oraliqda
yotuvchi butun sonlar). Jumlani rostlikka tekshiring: “Berilgan maydonlar bir xil rangda”.

Created on Wed Jun 30 20:44:39 2021

@author: Mansurjon Kamolov
"""

x1=int(input('x1='))
y1=int(input('y1='))
x2=int(input('x2='))
y2=int(input('y2='))
print(x1+y1) % 2 == (x2+y2) % 2 )
