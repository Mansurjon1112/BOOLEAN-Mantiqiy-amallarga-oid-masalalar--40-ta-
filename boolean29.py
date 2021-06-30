# -*- coding: utf-8 -*-
"""
Boolean29. (x, y), (x1, y1), (x2, y2) sonlari berilgan. Jumlani rostlikka tekshiring: “Koordinatalari
(x,y) bo’lgan nuqta, chap yuqori cho’qqisi (x1,y1) koordinatalarga ega bo’lgan va o’ng pastikisi
(x2,y2) bo’lgan, tomonlari esa koordinata o’qlariga parallel bo’lgan to’rtburchak ichida yotadi”.

Created on Wed Jun 30 20:24:47 2021

@author: Mansurjon Kamolov
"""

x=int(input('X='))
y=int(input('Y='))

x1=int(input('X1='))
y1=int(input('Y1='))

x2=int(input('X2='))
y2=int(input('Y2='))

print(x1<x<x2 and y2<y<y1)

