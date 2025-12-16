'''
import math
print(math.pi)
print(math.e)
print(math.sqrt(16))
print(math.power(2,3))
print(math.ceil(12.3))
print(math.ceil(12.01))
print(math.floor(12.3))
print(math.floor(12.9))
print(math.fabs(-12.3))
print(math.factorial(6))
print(math.gcd(50,100))
print(math.cos(30))
print(math.sin(30))
print(math.tan(60))
print(math.degrees(30))
print(math.radiance(30))
'''
from collections import Counter, defaultdict, deque
s="ruchitha is very beautiful and she is very nice"
print(Counter(s))
print(Counter(s.split()))
l=[1,2,3,4,2,3,5,6]
t=(1,2,3,1,2,3,5,6)
se={1,2,3,4,5,1,2,3,4}
print(Counter(l))
print(Counter(t))
print(Counter(se))

d={}
s="ruchitha is very beautiful and she is very nice"
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

d=defaultdict(int)
s="ruchitha is very beautiful and she is very nice"
for i in s:
    d[i]+=1
print(d)
d=defaultdict(float)
s="ruchitha is very beautiful and she is very nice"
for i in s:
    d[i]+=1
print(d)
d=defaultdict(str)
s="ruchitha is very beautiful and she is very nice"
for i in s:
    d[i]+='1'
print(d)

d=deque([])
d.append(10)
d.append(20)
d.append(30)
d.popleft()
d.popleft()
d.append(80)
d.append(60)
print(d)
from itertools import combinations,permutations
s="abc"
print(list(combinations(s,2)))
print(list(permutations(s,2)))
print(tuple(combinations(s,2)))
print(tuple(permutations(s,2)))
print(set(combinations(s,2)))
print(set(permutations(s,2)))

