# -*- coding: utf-8 -*-
"""
Boolean10. Ikkita butun A va B sonlari berilgan. Jumlani rostlikka tekshiring: “A va B sonlarning
faqat bittasi toq son”.

Created on Wed Jun 30 17:48:04 2021

@author: Mansurjon Kamolov
"""

a=int(input('A='))
b=int(input('B='))
#1-usul
print((a%2==1 or b%2==1) and not(a%2==1 and b%2==1))
#2-usul
print((a%2==1) and (b%2==0) or (a%2==0) and (b%2==1))
