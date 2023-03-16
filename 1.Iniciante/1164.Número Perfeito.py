n = int(input())

for i in range(n):
    x = int(input())
    divisor = int(x/2)
    soma = 0


    while (divisor>0):
        real = x/divisor
        inteiro = int(real)

        if (real == inteiro):
            soma += divisor
    
        divisor -= 1

    if (soma==x):
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")