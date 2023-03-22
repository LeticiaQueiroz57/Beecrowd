n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

qtd = 0

if (n1%2==0):
    qtd += 1
if (n2%2==0):
    qtd += 1
if (n3%2==0):
    qtd += 1
if (n4%2==0):
    qtd += 1
if (n5%2==0):
    qtd += 1

print(f"{qtd} valores pares")
