def resposta():
    print(x,"ano(s)")
    print(y,"mes(es)")
    print(z,"dia(s)")

i = int(input())
ano = i/365
x = int(ano)
y = 0
z = 0

if (ano==x):
    resposta()
else:
    i -= 365*x
    meses = i/30
    y = int(meses)

    if (meses==y):
        resposta()
    else:
        i -= 30*y
        z = i
        resposta()
