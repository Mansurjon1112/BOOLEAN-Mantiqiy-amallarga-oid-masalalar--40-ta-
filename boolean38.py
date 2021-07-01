# -*- coding: utf-8 -*-
"""
Boolean38. Shaxmat doskasining ikkita turli (x1, y1), (x2, y2) koordinalari berilgan (1-8 oraliqda
yotuvchi butun sonlar). Jumlani rostlikka tekshiring: “Fil bir yurishda bir maydondan ikkinchisiga
o’ta oladi”.

Created on Thu Jul  1 15:04:58 2021

@author: Mansurjon Kamolov
"""

x1=int(input('x1='))
y1=int(input('y1='))
x2=int(input('x2='))
y2=int(input('y2='))

print( abs(x2-x1)==abs(y2-y1))