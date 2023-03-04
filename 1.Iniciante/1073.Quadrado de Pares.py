n = int(input())
x = 0

while (n>x):
    x += 1
    s = str(x)+"^2"
    if (x%2==0):
        print(s,"=",x**2)