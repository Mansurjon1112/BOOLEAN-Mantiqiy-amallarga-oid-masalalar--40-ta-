# -*- coding: utf-8 -*-
"""
Boolean31. a, b, c butun sonlari berilgan. Jumlani rostlikka tekshiring: “a, b, c tomonli uchburchak
teng yonli bo’ladi”.

Created on Wed Jun 30 20:33:34 2021

@author: Mansurjon Kamolov
"""

a=int(input('A='))
b=int(input('B='))
c=int(input('C='))
d = (a+b>c and a+c>b and b+c>a) #uchburchak hosil qilish sharti 
print(a==b or b==c or c==a and not (a==b==c) and d)
