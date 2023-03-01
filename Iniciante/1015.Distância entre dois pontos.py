import math

x1, y1 = map(float,input().split())
x2, y2 = map(float,input().split())
soma = (x2-x1)**2 + (y2 - y1)**2
dist = math.sqrt(soma)
print("%.4f"%dist)