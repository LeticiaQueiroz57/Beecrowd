def arremessos():
    pontos = 0
    for i in range(3):
        x,d = map(int,input().split())
        pontos += x*d
    return pontos

n = int(input())

for i in range(n):
    joao = arremessos()
    maria = arremessos()
    if (maria>joao):
        print('MARIA')
    else:
        print('JOAO')
