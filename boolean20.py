# -*- coding: utf-8 -*-
"""
Boolean20. Uch xonali son berilgan. Jumlani rostlikka tekshiring: “Ushbu sonning barcha raqamlari
xar xil”.

Created on Wed Jun 30 19:58:02 2021

@author: Mansurjon Kamolov
"""

a=int(input('A='))
r1=a%10
r2=a%100//10
r3=a//100

print( r1!=r2 and r1!=r3 and r2!=r3 )