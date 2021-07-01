# -*- coding: utf-8 -*-
"""
Boolean40. Shaxmat doskasining ikkita turli (x1, y1), (x2, y2) koordinalari berilgan (1-8 oraliqda
yotuvchi butun sonlar). Jumlani rostlikka tekshiring: “Ot bir yurishda bir maydondan ikkinchisiga
o’ta oladi”

Created on Thu Jul  1 15:18:56 2021

@author: Mansurjon Kamolov
"""

x1=3#int(input('x1='))

y1=5#int(input('y1='))
x2=int(input('x2='))
y2=int(input('y2='))

print(abs(x2-x1)==1 and abs(y2-y1)==2 or abs(x2-x1)==2 and abs(y2-y1)==1) 