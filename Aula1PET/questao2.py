horarioInicial = []
horaInicial = int(input("Digite a hora inicial: "))
minInicial = int(input("Digite os minutos iniciais: "))

horarioInicial.append(horaInicial)
horarioInicial.append(minInicial)

horarioFinal = []
horaFinal = int(input("Digite a hora final: "))
minFinal = int(input("Digite os minutos finais: "))
horarioFinal.append(horaFinal)
horarioFinal.append(minFinal)


duracao = ((horarioFinal[0]*60) + horarioFinal[1] - ((horarioInicial[0]*60) + horarioInicial[1]))
if duracao <= 0:
    duracao += 24*60

hora = duracao // 60
minuto = duracao % 60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)" .format(hora, minuto))