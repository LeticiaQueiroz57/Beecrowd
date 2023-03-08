numero = int(input())
b = []


def verificador(x,n):
    primo = True
    while (n>1):
        y = x%n
        if y==0:
            primo = False
        
        n -= 1
    return primo

for i in range(numero):
    a = int(input())
    b.append(a)

for i in range (numero):
    n = int(b[i]/2)
    p = verificador (b[i],n)

    if (p==False):
        print(f"{b[i]} nao eh primo")
    else:
        print(f"{b[i]} eh primo")