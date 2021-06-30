# -*- coding: utf-8 -*-
"""
Boolean34. Shaxmat doskasining x, y koordinatalari berilgan (1-8 oraliqda yotuvchi butun sonlar).
Doskaning chap pastki maydoni (1,1) qoraligini hisobga olib, jumlani rostlikka tekshiring: “Berilgan
(x, y) maydon oq”.

Created on Wed Jun 30 20:41:47 2021

@author: Mansurjon Kamolov
"""
x=int(input('x='))
y=int(input('y='))
print(x%2==0 and y%2==0 or x%2==1 and y%2==1)
