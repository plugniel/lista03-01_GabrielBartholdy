preco_custo = int(input("Qual o valor bruto do item?"))

if preco_custo <= 100:
    preco_com = (preco_custo * 0.45) + preco_custo
    print("O valor comercial do prouto: {}".format(preco_com))
else:
    preco_com = (preco_custo * 0.35) + preco_custo
    print("O valor comercial do prouto: {}".format(preco_com))