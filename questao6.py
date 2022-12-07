def valorPagamento(valorPrestacao, diasAtraso):     
    
  if diasAtraso == 0:
    print("Como não houve dias de atraso, não será cobrada a multa")
    print("Esse é o valor da prestação a ser pago: {} " .format(valorPrestacao))
        

  if diasAtraso >= 1:
    valorPrestacao = (valorPrestacao*3)/100 + (((valorPrestacao*0.1)/100)*diasAtraso + valorPrestacao)
    print("Como houve atraso no pagamento da prestação, você irá pagar 3% de multa + 0.1 por dia de atraso. Então o valor a ser pago da prestação é de {} " .format(valorPrestacao))
        

while True:
  valorPrestacao = float(input("Digite o valor da prestação: "))
  diasAtraso = int(input("Digite os dias atrasados: "))
  relatorioPrestacao = []
  relatorioPrestacao.append(valorPrestacao)
  
  for i in range(len(relatorioPrestacao)):
    if valorPrestacao != 0:
        valorPagamento(valorPrestacao, diasAtraso)

    elif valorPrestacao == 0:
       print("Esse foi o valor das prestações {} e a soma dos ganhos {} " .format(relatorioPrestacao, sum(relatorioPrestacao)))
    