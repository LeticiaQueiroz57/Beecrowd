n = int(input())
z = []

for i in range(n):
    w = input()
    z.insert(i,w)

for i in range(n):
    x = z[i]
    y = 0
    for j in range(len(x)):
        if x[j] == "1":
            y += 2
        elif x[j]=="2" or x[j]=="3" or x[j]=="5":
            y +=5
        elif x[j]=="4":
            y += 4
        elif x[j]=="6" or x[j]=="9" or x[j]=="0":
            y += 6
        elif x[j]=="7":
            y += 3
        elif x[j]=="8":
            y += 7

    print(f"{y} leds")
