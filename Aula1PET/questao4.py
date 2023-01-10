idade = []
valor = int(input("Digite uma idade: "))
i = 0
while valor >= 0:
  valor = int(input("Digite uma idade: "))
  idade.append(valor)
  i += 1

else:
  del idade[-1]
  media = sum(idade) / len(idade)
  print("Esses foram as idades digitadas {}, a média entre as idades é {} e a quantidade de idades inseridas foram {}" .format((idade), media, i))
        
    
    
