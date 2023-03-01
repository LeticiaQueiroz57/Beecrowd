def mult():
    if (y==x):
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")

a, b = map(float,input().split())

if (a>b):
    x = a/b
    y = int(x)
    mult()
else:
    x = b/a
    y = int(x)
    mult()

if (a==b): 
    print("Sao Multiplos")
