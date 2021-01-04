# -*- coding: utf-8 -*-
"""
Created on Wed May 20 11:11:30 2020

@author: rishi
"""

"""
import datetime 
print(datetime.datetime.now())
"""
#### GMT is timezone and UCT is time standard with which we compare
from datetime import datetime as dt
import pytz

tz = pytz.timezone('Asia/kolkata')
#gives greenwich + time
print(dt.now(tz))
# 2020-05-20 11:16:55.838327+05:30 extra 5:30 gives how much time it is ahead of UCT(grrenwhich time)
# UTC is 0 hours ahead of GMT
print(pytz.all_timezones)
