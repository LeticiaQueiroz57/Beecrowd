n1, n2, n3, n4 = map(float, input().split())
m = (n1*2 + n2*3 + n3*4 + n4)/10

print(f"Media: {m:.1f}")

if (m>=7):
    print("Aluno aprovado.")
elif (m>=5 and m<7):
    print("Aluno em exame.")
    nota = float(input())
    print(f"Nota do exame: {nota:.1f}")
    media = (nota+m)/2
    if (media>=5):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media:.1f}")
else:
    print("Aluno reprovado.")
