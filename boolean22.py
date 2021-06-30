# -*- coding: utf-8 -*-
"""
Boolean22. Uch xonali son berilgan. Jumlani rostlikka tekshiring: “Ushbu sonning raqamlari
ketama-ket o’suvchi bo’lib joylashgan yoki kamayuvchi ketma-ketlikka ega”.

Created on Wed Jun 30 20:02:07 2021

@author: Mansurjon Kamolov
"""

a=int(input('A='))
r1=a%10
r2=a%100//10
r3=a//100

print( r3<r2<r1 or r3>r2>r1 )