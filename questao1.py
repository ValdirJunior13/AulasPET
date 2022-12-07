n = 0
par = []
impar = []
while n < 5:
  num = int(input("Digite um número inteiro: "))
  n = n + 1
  if num%2 == 0:
    par.append(num)
    
    
  elif num%2 == 1:
    impar.append(num)
    

print("a quantidade de números pares foi {} e os números são {}" .format(len(par), par))
print("a quantidade de números pares foi {} e os números são {}" .format(len(impar), impar))