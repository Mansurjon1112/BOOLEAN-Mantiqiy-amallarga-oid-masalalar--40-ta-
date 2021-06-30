# -*- coding: utf-8 -*-
"""
Boolean32. a, b, c butun sonlar berilgan. Jumlani rostlikka tekshiring: “a, b, c tomonli uchburchak
to’g’ri burchakli”.

Created on Wed Jun 30 20:35:57 2021

@author: Mansurjon Kamolov
"""

a=int(input('A='))
b=int(input('B='))
c=int(input('C='))
d = (a+b>c and a+c>b and b+c>a) #uchburchak hosil qilish sharti 
print((a*a+b*b==c*c)or (a*a+c*c==b*b) or (b*b+c*c==a*a) and d)