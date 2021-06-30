# -*- coding: utf-8 -*-
"""
Boolean15. Uchta A, B, C butun sonlar berilgan. Jumlani rostlikka tekshiring: “A, B, C sonlardan
faqat ikkitasi musbat son”

Created on Wed Jun 30 18:34:45 2021

@author: Mansurjon Kamolov
"""

a=int(input('A='))
b=int(input('B='))
c=int(input('C='))
print((a>0 and b>0 and c<=0) or (a<=0 and b>0 and c>0) or (a>0 and b<=0 and c>0) )   
