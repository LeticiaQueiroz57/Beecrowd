while True:
    try:
        alunos = int(input())

        epr = 0
        ehd = 0
        intrusos = 0


        for i in range(alunos):
            matricula, curso = input().split()
    
            if (curso=="EPR"):
                epr += 1
            elif (curso=="EHD"):
                ehd += 1
            else:
                intrusos += 1

        print("EPR:", epr)
        print("EHD:",ehd)
        print("INTRUSOS:",intrusos)
    except EOFError:
        break
