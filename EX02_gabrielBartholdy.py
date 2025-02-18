nome = str(input("Qual seu nome?"))
peso = int(input("Qual seu peso?"))

if peso >= 52 and peso <65:
    print("{} sua catogoria é PENA".format(nome))
elif peso >= 65 and peso <72:
    print("{} sua catogoria é LEVE".format(nome))
elif peso >= 72 and peso <= 79:
    print("{} sua catogoria é LIGEIRO".format(nome))
elif peso >= 79 and peso < 86:
    print("{} sua catogoria é MEIO – MEDIO".format(nome))
elif peso >= 86 and peso < 90:
    print("{} sua catogoria é MEDIO".format(nome))
elif peso >= 90 and peso < 100:
    print("{} sua catogoria é MEIO – PESADO".format(nome))
elif peso > 100: 
    print("{} sua catogoria é PESADO".format(nome))
else:
    print("Categoria INVALIDA")

print("GAbriel Bartholdy")