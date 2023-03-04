n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

def parImpar(x):
    if (x%2==0):
        return True
    else:
        return False

p = []
p.append(parImpar(n1))
p.append(parImpar(n2))
p.append(parImpar(n3))
p.append(parImpar(n4))
p.append(parImpar(n5))

x = 0
for i in range (5):
    if (p[i]==True):
        x += 1

print(x,"valores pares")
