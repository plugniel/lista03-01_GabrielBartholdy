nome = input("Qual seu nome ?")
idade = int(input("Qual sua Idade?"))
sexo = str(input("Qual seu sexo?"))

if sexo == "f".lower() and idade >= 21 and idade <= 34:
    print("voce passou para servir")


elif sexo == "m".lower() and idade >= 18 and idade <= 39:
        print("você passou")

        
else:
    print("Você não foi convocado")