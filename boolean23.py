# -*- coding: utf-8 -*-
"""
Boolean23. Uch xonali son berilgan. Jumlani rostlikka tekshiring: “Ushbu sonni chapdan o’qiganda
ham, o’ngdan o’qiganda ham bir xil”.

Created on Wed Jun 30 20:19:14 2021

@author: Mansurjon Kamolov
"""

a=int(input('A='))
r1=a%10
r2=a%100//10
r3=a//100
b=r1*100+r2*10+r3
print(a==b)