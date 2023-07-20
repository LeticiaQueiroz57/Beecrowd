def resto(c,menor):
    while (menor<len(c)):
        print(c[menor],end='')
        menor += 1
    print()

def juntar(a,b):
    menor = min(len(a),len(b))
    for i in range(menor):
        print(a[i],end='')
        print(b[i],end='')

    if (len(a)>len(b)):
        resto(a,menor)
    elif(len(a)<len(b)):
        resto(b,menor)
    else:
        print()

n = int(input())
for i in range(n):
    a, b = input().split()
    juntar(a,b)
