a, b = map(int, input().split())

x = max(a,b)
y = min(a,b)

if (x%y!=0):
    print("Nao sao Multiplos")
else:
    print("Sao Multiplos")