def verificador(n):
    x = str(n)
    igual = False
    for i in range(len(x)):
        y = x[i]
        contador = i
        while (contador<len(x)-1):
            contador += 1
            if (y==x[contador]):
                igual = True
    return igual

while True:
    try:
        n, m = map(int, input().split())
        z = n
        diferentes = 0
        while (n<=m):
            igual = verificador(n)
            if (igual==False):
                diferentes += 1
            n += 1
        print(diferentes)
    except EOFError:
        break

