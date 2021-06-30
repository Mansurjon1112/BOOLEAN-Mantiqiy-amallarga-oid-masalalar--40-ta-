# -*- coding: utf-8 -*-
"""
Boolean24. A, B, C sonlar beilgan (A soni noldan farqli). D=B2-4AC diskerminantdan foydalanib,
jumlani rostlikka tekshiring: “Ax2+Bx+C=0 kvadrat tenglama haqiqiy ildizga ega”.

Created on Wed Jun 30 20:20:15 2021

@author: Mansurjon Kamolov
"""

a=int(input('A='))
b=int(input('B='))
c=int(input('C='))
d=b*b-4*a*c
print(d>=0)