import sys
import re
x=sys.stdin.readlines()
print(x)

y=(i.split('\n')[0] for i in x)
print(y)

for i in y:
    if re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",i):
        print(i)
