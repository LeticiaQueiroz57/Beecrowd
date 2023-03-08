n = int(input())
x = []

def div(x):
    y = int(x/2)
    z = [1]

    while (y>1):
        if (x%y < 1):
            z.append(y)
    
        y -= 1
    
    soma = 0
    for i in range(len(z)):
        soma += z[i]
        
    if (soma==x):
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")



for i in range(n):
    a = int(input())
    x.append(a)

for j in range(n):
    div(x[j])
