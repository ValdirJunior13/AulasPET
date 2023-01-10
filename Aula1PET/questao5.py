def calculaSalario():
  valorBruto = float(input("Digite o valor do seu salário: "))
  salarioINSS = valorBruto - (valorBruto*11)/100 
  print("O seu salário pós desconto do INSS é de: {} " .format(salarioINSS))
  valorDescontadoINSS = (valorBruto*11/100)      
  
  descontoIR = salarioINSS - (salarioINSS*15)/100
  valorDescontadoIR = (salarioINSS*15/100)
  print("O seu salários pós desconto do IR é de: {}" .format(descontoIR))
  
  salarioLiquido = valorBruto - (valorDescontadoIR + valorDescontadoINSS)
  print("o valor do seu salário após os descontos de {} e {} é de: {}" .format(valorDescontadoINSS, valorDescontadoIR, salarioLiquido))

calculaSalario()