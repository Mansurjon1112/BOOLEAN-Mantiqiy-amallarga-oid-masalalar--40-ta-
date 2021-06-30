# -*- coding: utf-8 -*-
"""
Boolean18. Jumlani rostlikka tekshiring: “Berilgan uchta butun sonlarning hech bo’lmaganda 2 tasi
bir biriga teng”.

Created on Wed Jun 30 19:32:04 2021

@author: Mansurjon Kamolov
"""

a=int(input('A='))
b=int(input('B='))
c=int(input('C='))
print((a==1 and b==1 and c==1) or (a==1 and b==1 and c!=1) or (a==1 and b!=1 and c==1) or (a!=1 and b==1 and c==1) )   
