risco = input("Qual risco esta Disposto a correr?Baixa(BX)Alta(Al)").lower()
valor = int(input("Qual o valor a ser Investido?"))

if risco== "BX".lower() and valor < 1000:
    print("Voce deve investir Na POUPANÇA!")
elif risco == "BX".lower() and valor >= 1000:
    print("Você deve investir na renda Fixa")
elif risco == "AL".lower() and valor <1000:
    print("Voce deve investir em BTC")
elif risco == "AL".lower() and valor >=1000:
    print("voce deve investir em Ações")

else:
    print("dado invalido")


print("GAbriel Bartholdy")