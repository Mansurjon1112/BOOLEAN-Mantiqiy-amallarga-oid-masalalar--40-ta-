# -*- coding: utf-8 -*-
"""
Boolean37. Shaxmat doskasining ikkita turli (x1, y1), (x2, y2) koordinalari berilgan (1-8 oraliqda
yotuvchi butun sonlar). Jumlani rostlikka tekshiring: “Shoh bir yurishda bir maydondan ikkinchisiga
o’ta oladi.”

Created on Wed Jun 30 21:08:37 2021

@author: Mansurjon Kamolov
"""

x1=int(input('x1='))
y1=int(input('y1='))
x2=int(input('x2='))
y2=int(input('y2='))

print(x1-1<=x2<=x1+1 and y1-1<=y2<=y1+1)