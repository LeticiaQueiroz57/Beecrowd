x = []
verificador = True

while (verificador==True):
    y = int(input())
    if y>0:
        x.append(y)
    else:
        verificador = False

soma = 0
for i in range(len(x)):
    soma += x[i]

z = soma/len(x)
print(f"{z:.2f}")