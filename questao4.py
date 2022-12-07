idade = []
i = 0
valor = int(input("Digite um número: "))
while True:
  idade.append(valor)
  for i in range(len(idade)):
    print(idade)
    if idade[-1] >= 0:
      print("Não há um número negativo no final")
      media = sum(idade) / len(idade)
      print("Essa é a média da idade dos individuos", media)
    elif idade[-1] < 0:
      del idade[-1]
      media = sum(idade) / len(idade)
      print(media)

