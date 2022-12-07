idade = []
i = 0

while i>=0:
  valor = int(input("Digite um número: "))
  idade.append(valor)
  for i in range(len(idade)):      
    if idade[-1] < 0:
      del idade[-1]
      media = sum(idade) / len(idade)
      print("Esses foram as idades digitadas {} e a média entre as idades {}" .format((idade), media))
      break
  
