from question3 import PYlruCache
import time
import datetime


curr_time=time.gmtime()
creation_time = datetime.datetime(curr_time.tm_year,curr_time.tm_mon,curr_time.tm_mday,curr_time.tm_hour+1,curr_time.tm_min,curr_time.tm_sec)

cache = PYlruCache([1,2,3],creation_time,3)

for item in cache:
    print(item)
