'''What are Built-in Modules?

Built-in (standard library) modules are pre-installed modules in Python—no need to install them.
1. os module:
File, directory operations
OS interaction
2.sys module: (system module)      
Python runtime control
3.subprocess module:
External command execution
Run system commands

👉 Example 1: File handling
👉 Example 2: Running terminal commands

3..math & numeric modules:
1. math module: 
Mathematical functions
2. random module:       
Random number generation
3. statistics module:
Statistical functions

4...date & time modules:
1. datetime module:
Date and time manipulation
2. time module:
Time-related functions

5..data handlimg modules:
1. json module:
JSON data handling
2. csv module:
CSV file handling
3. pickle module:
Object serialization

6...file &compression modules:
1. zipfile module:  
ZIP file handling
2. tarfile module:
TAR file handling
3. gzip module:
GZIP file handling
'''




'''import sys

print(sys.argv)
print(sys.path)
print(sys.version)
print('start')
sys.exit()
print('end')
'''
'''
#platform module
import platform
print(platform.system())
print(platform.release())   
print(platform.processor())
'''
'''
#math module
import math
print(math.pi)
print(math.e)
print(math.sqrt(36))
print(math.pow(3,4))
print(math.factorial(5))
print(math.gcd(48,18))
print(math.ceil(12.000001))
print(math.factorial(5))
print(math.floor(12.999999))
print(math.fabs(-12))
print(round(12.3456789, 2))
print(abs(-12))

print(math.log(2,2))
print(math.sin(30))
print(math.cos(30)) 
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))



import random
l=[9,2,3,4,5,6]
random.shuffle(1)
print(l)
'''

'''collections module
1. Counter: Count occurrences of elements in a collection.
2. defaultdict: Dictionary with default values for missing keys.
3. namedtuple: Factory function for creating tuple subclasses with named fields.


import collections
s='python programming'  
l=[1,2,3,12,34,1,1,2,3,4,2,3]
r='hello world'.split()
res= collections.Counter(s)
res1=collections.Counter(l)
res2=collections.Counter(r)
print(res)
print(res1)
print(res2)
'''
'''
s='python programming'
res ={}
for i in s:
    if i in res:
        res[i]+=1
    else:
        res[i]=1
print(res)
'''
'''collections module
1. Counter: Count occurrences of elements in a collection.
import collections

q=collections.deque([])

q.append(20)
q.append(30)
q.append(60)
q.append(70)
q.popleft()
q.popleft()
q.popleft()
q.append(10)
q.append(40)

print(q)
'''
'''
from itertools import combinations, permutations

s='abc'
print(list(combinations(s, 3)))
print(list(permutations(s, 3)))
'''
'''datetime module
from datetime import date,time,datetime

today = date.today()

print(today)

print("year:", today.year)
print("month:", today.month)
print("day:", today.day)
print(today.weekday())
print(today.isoweekday())
'''
'''
from datetime import date,time,datetime

now = time(21,56,18)

print(now)
print(now.hour)
print(now.minute)
print(now.second)
'''
'''
from datetime import date,time,datetime

now = datetime.now()

print(now)
'''
'''
from datetime import date,time,datetime
now = datetime.now()
print(now.strftime("%d/%m/%y  %H:%M:%S"))
print(now.strftime("%d/%m/%y %I:%M:%S"))
print(now.strftime("%d/%b/%y %I:%M:%S %p"))
print(now.strftime("%d/%B/%y %I:%M:%S %p"))
'''

from datetime import date,time,datetime, timedelta

today = date.today()
now = datetime.now()

today_7 = today-timedelta(days=7)
print(today_7)

now_30 = now+timedelta(minutes=30)
print(now_30)

