x = int(input())
y = int(input())

z = min(x,y)
maximo = max(x,y)
soma = 0
z += 1

while(z<maximo):
    if (z%2==1):
        print(soma)
        soma += z
    z += 1

print(soma)

