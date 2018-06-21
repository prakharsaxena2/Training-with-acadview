''' time()– This function is used to count the number of seconds elapsed since the epoch.
gmtime(sec)– This function returns a structure with 9 values each representing a time attribute in sequence.
It converts seconds into time attributes(days, years, months etc.) till specified seconds from epoch. If no seconds are mentioned, time is calculated till present.
The structure attribute table is given below.

0	tm_year	2008
1	tm_mon	1 to 12
2	tm_mday	1 to 31
3	tm_hour	0 to 23
4	tm_min	0 to 59
5	tm_sec	0 to 61 (60 or 61 are leap-seconds)
6	tm_wday	0 to 6 (0 is Monday)
7	tm_yday	1 to 366 (Julian day)
8	tm_isdst	-1, 0, 1, -1 means library determines DST'''

import time
import math
import datetime
import os
print("Second elapsed since the epoch are",end="")
print(time.time())

print("\n\ntime calculated according to second",end="")
print(time.gmtime())


print("time calculated using asctime",time.asctime(time.gmtime()))

print("time calculated using ctime() is :",end="")
print(time.ctime())

#number = int(input("enter number"))

print("today",datetime.date.today())

number1 = int(input("Enter the no"))
number2 = int(input("Enter the no"))
print(math.factorial(number1))
print(math.gcd(number1,number2))

print("current working directory",os.getcwd())

print("user environment",os._Environ)