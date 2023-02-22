n1, n2, n3, n4 = map(float,input().split()) # 2, 3, 4, 1
m = (n1*2 + n2*3 + n3*4 + n4*1)/10

if (m>=7):
    print("Media:","%.1f"%m)
    print("Aluno aprovado.")
elif (m>=5 and m<7):
    nota = float(input())
    print("Media:","%.1f"%m)
    print("Aluno em exame.")
    print("Nota do exame:","%.1f"%nota)
    media = (nota + m)/2
    if (media>=5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final:","%.1f"%media)
else:
    print("Media:","%.1f"%m)
    print("Aluno reprovado.")
