x = int(input())
y = int(input())

z = min(x,y)
soma = 0
z += 1

while(z<max(x,y)):
    if (z%2==1):
        soma += z
    z += 1

print(soma)

