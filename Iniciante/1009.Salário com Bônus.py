nome = input()
salario = float(input())
vendas = float(input())
comissao = vendas*0.15
total = comissao + salario
print("TOTAL = R$","%.2f"%total)