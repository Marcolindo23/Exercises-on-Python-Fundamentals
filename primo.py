from math import sqrt
from math import asin
from math import cos
from math import sin
from math import radians
print("Hello world")



print(100**700)
print(sqrt(10))

# calcolare la distanza tra Oslo(59.9°N 10.8°E) e Vancouver(49.3°N 123.1°W) 

r = 6371
ϕ1= radians(59.9)
λ1 = radians(10.8)
ϕ2 = radians(49.3)
λ2 = radians(-123.1)
d = 2*r*asin(sqrt(sin(1/2*(ϕ2-ϕ1))**2+cos(ϕ1)*cos(ϕ2)*sin(1/2*(λ2-λ1))**2))
print(d)

"""Definire
- due variabili (i1, i2) di tipo intero
- due variabili (s1, s2) di tipo stringa
- due variabili (f1, f2) di tipo float
- due variabili (b1, b2) di tipo boolean
stampare
i1+i2
s1+s2
f1+f2
b1+b2
i1+s1
s1+i2
i1+f2
f2+i2
i1+b1
f1+b1
s1+b1
b1+i1
b1+s1
b1+f1"""

i1=70
i2=90
s1="buonasera"
s2="buongiorno"
f1=127.9
f2=135.7
b1=True
b2=False

print(i1+i2)
print(s1+s2)
print(f1+f2)
print(b1+b2)
#print(i1+s1)
#print(s1+i2)
print(i1+f2)
print(f2+i2)
print(i1+b1)
print(f1+b1)
#print(s1+b1)
print(b1+i1)
#print(b1+s1)
print(b1+f1)


