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
