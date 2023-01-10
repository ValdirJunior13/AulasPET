import random


class Conta(): #class Conta
    def __init__(self, numConta):
        self.numero = numConta
        self.saldo = 0
        self.bonificacao = 0

    def deposite(self, valor):
        self.saldo = (self.saldo + valor) - (valor*0.1)/100
        self.bonificacao = (valor*0.01)/100

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return True
        else:
            return False


class Poupanca(Conta): #class Poupanca
    def render(self):
        self.saldo = self.saldo + (self.saldo*0.01)
        
        
class contaBonificada(Conta): #class contaBonificada
  def renderBonificacao(self): #método que recebe a bonificação e depois a zera
    self.saldo += self.bonificacao
    self.bonifacacao = 0
    
class Banco(): #class Banco
    def __init__(self, nome):  
        self.nome = nome
        self.contas = []

    def getNome(self):
        return self.nome

    def criarConta(self): #cria uma conta Corrente utilizando números aleatórios 
        num = random.randint(0, 1000)
        criada = Conta(num)
        self.contas.append(criada)
        return num

    def criarPoupanca(self): #cria uma conta poupança utilizando números aleatórios 
        num = random.randint(0, 1000)
        pronto = Poupanca(num)
        self.contas.append(pronto)
        return num
      
    def criarContaBonificada(self): #cria uma conta para utilizar o método de render bonificação
        num = random.randint(0, 1000)
        molde = contaBonificada(num)
        self.contas.append(molde)
        return num

    def consultaSaldo(self, numConta): #Consulta o saldo da minha conta e caso não tenha criado uma conta, retorno uma mensagem "-1"
        for conta in self.contas:
            if conta.numero == numConta:
                return conta.saldo
              
        return -1
      

    def depositar(self, numConta, valor): #deposita o valor na conta especificada
        for account in self.contas:
            if account.numero == numConta:
                account.deposite(valor)

    def sacar(self, numConta, valor): #saca o valor da conta especificada
        for account in self.contas:
            if account.numero == numConta:
                return account.sacar(valor)

    def renderBonificacao(self, numConta): #caso a conta seja uma conta bonificada, gera o bônus, caso contrário, retorna que a conta não é bonificada
        for account in self.contas:
          if account.numero == numConta and isinstance(account, contaBonificada):
            account.renderBonificacao()
            return True
        return False
      
    def renderPoupanca(self, numConta): #caso a conta seja uma conta poupança, gera o bônus, caso contrário, retorna que a conta não é uma conta poupança
      for account in self.contas:
        if account.numero == numConta and isinstance(account, Poupanca):
          account.render()
          return True
      return False
      