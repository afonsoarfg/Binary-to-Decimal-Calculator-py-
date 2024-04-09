
x = int(input("Introduza o valor binário :\n"))
while (x / (10000000)) > 1:
    print("Introduza outra vez\n")
    x = int(input("Introduza o valor binário : \n"))

for j in str(x):
    if j != '0' and j != '1' :
        print("Introduza outra vez")
        x = int(input("Introduza o valor binário : \n"))
x = str(x)
i = len(x) - 1
decimal = 0
for f in x:
    decimal += int(f) * (2 ** i)
    i = i - 1

print("O valor decimal é :" ,decimal)

N = input("Queres continuar? S/N\n")
while True :
    if N == 'S' :
        x = int(input("Introduza o valor binário :\n"))
        while (x / (10000000)) > 1:
            print("Introduza outra vez\n")
            x =int(input("Introduza o valor binário : \n"))

        for j in str(x):
            if j != '0' and j != '1' :
                print("Introduza outra vez")
                x = int(input("Introduza o valor binário : \n"))
        x = str(x)
        i = len(x) - 1
        decimal = 0
        for f in x:
            decimal += int(f) * (2 ** i)
            i = i - 1
        
        print("O valor decimal é :" ,decimal)   
        N = input("Queres continuar? S/N\n")

    elif N == 'N':
        break
    else:
        while N not in 'SN':
            print("Letra inválida, tente outra vez\n")
            N = input("Queres continuar? S/N\n")