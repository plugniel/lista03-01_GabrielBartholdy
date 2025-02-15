candidato = input("Qual o candidato")
voto = int(input("quantos votos foram no candidato"))
maxi = int(input("quantos votos totais no municipio"))

if voto  > (maxi / 2):
    print("O candidato {} teve {} votos e teve a maior de votos e foi eleito".format(candidato,voto))

else:
    print("As votação tera 2° turno")
