# -*- coding: utf-8 -*-
"""
Boolean11. Ikkita butun A va B sonlari berilgan. Jumlani rostlikka tekshiring: “A va B sonlarining
har ikkalasi ham yoki toq son yoki juft son”.

Created on Wed Jun 30 17:57:58 2021

@author: Mansurjon Kamolov
"""

a=int(input('A='))
b=int(input('B='))
print((a%2==1 and b%2==1) or (a%2==0 and b%2==0))
