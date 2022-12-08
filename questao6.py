def valorPagamento(valorPrestacao, diasAtraso):
  taxa = (valorPrestacao*3)/100
  taxa2 = (valorPrestacao*0.1)/100 * diasAtraso 
  
  if diasAtraso == 0:
    print("\nComo não houve dias de atraso, não será cobrada a multa")
    print("\nEsse é o valor da prestação a ser pago: {} ".format(valorPrestacao))
    relatorioPrestacao.append(valorPrestacao)

  elif diasAtraso > 0:
    valorPrestacao = taxa + taxa2 + valorPrestacao
    print("\nComo houve atraso no pagamento da prestação, você irá pagar 3% de multa + 0.1 por dia de atraso. Então o valor a ser pago da prestação é de {} " .format(valorPrestacao))
    relatorioPrestacao.append(valorPrestacao) 

valorPrestacao = 1
relatorioPrestacao = []
contador = 0

while valorPrestacao != 0:
  valorPrestacao = float(input("\nDigite o valor da prestação: "))  
  diasAtraso = int(input("\nDigite os dias atrasados: "))
  valorPagamento(valorPrestacao, diasAtraso)
  contador += 1
    
else:
  relatorioPrestacao.append(valorPrestacao)
  del relatorioPrestacao[-1]
  print("\nEsse foram os valor das prestações {}, a soma dos ganhos {} e a quantidade de prestações pagas {}\n".format(relatorioPrestacao, sum(relatorioPrestacao), contador - 1))

