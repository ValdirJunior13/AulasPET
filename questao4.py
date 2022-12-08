idade = []
i = 0

while i>=0:
  valor = int(input("Digite uma idade: "))
  idade.append(valor)
  i = i + 1 
  if idade[-1] < 0:
      del idade[-1]
      media = sum(idade) // len(idade)
      print("Esses foram as idades digitadas {}, a média entre as idades {} e a quantidade de idades inseridas {}" .format((idade), media, i))
      break    
    
    
