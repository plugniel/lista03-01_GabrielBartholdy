empre = int (input("Qual sera o valor do emprestimo"))
salario = int(input("Qual seu salario"))
parc = int(input("Em quantas parcelas?"))

if (salario * 0.08) >  (empre / parc):
    print("seu Emprestimo foi concedido")
    print("No valor de {} , em parcelas de {}x".format(empre,parc))
else:
    print("Seu emprestimo não foi concedido")

print("GAbriel Bartholdy")