# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 15:45:00 2019

@author: Aditya
"""

import csv
%precision 2
with open('mpg.csv') as csvfile:
    mpg=list(csv.DictReader(csvfile))
mpg[:3]

len(mpg)

mpg[0].keys()

sum(float(d['cty']) for d in mpg) / len(mpg)
sum(float(d['hwy']) for d in mpg) / len(mpg)

cylinders = set(d['cyl'] for d in mpg)
cylinders

CtyMpgByCyl = []

for c in cylinders:
    summpg = 0
    ctytypecount = 0
    for d in mpg:
        if d['cyl'] == c:
            summpg += 1
            ctytypecount += 1
    CtyMpgByCyl.append((c, summpg/ctytypecount))

CtyMpgByCyl.sort(key= lambda x: x[0])
CtyMpgByCyl
