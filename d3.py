# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:06:46 2019

@author: Aditya
"""

import datetime as dt
import time as tm
tm.time()
dtnow = dt.datetime.fromtimestamp(tm.time())
dtnow

dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second

delta = dt.timedelta(days=100)
delta

today = dt.date.today()

today-delta

today>today-delta
