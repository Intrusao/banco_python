from datetime import datetime, timedelta

class Usuario:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.conta_bancaria = None

class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.extratos = []
        self.saque_horas = []

    def deposito(self, valor):
        if valor >= 0:
            self.saldo += valor
            self.extratos.append(("Depósito", valor))
            print(f"Depósito de {valor} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")    

    def saque(self, valor):
        if valor >= 0:
            if valor <= 500:
                if valor <= self.saldo:
                    if self.verificar_limite_saques():
                        self.saldo -= valor
                        self.extratos.append(("Saque", valor))
                        self.saque_horas.append(datetime.now())
                        print(f"Saque de {valor} realizado com sucesso.")
                    else:
                        print("Limite de saques excedido, retorne em breve...")
                else:
                    print("Saldo insuficiente.")
            else:
                print("Limite diário excedido.")
        else:
            print("Valor de saque inválido")
            
    def emprestimo(self, valor):
        if valor >= 0:
            if valor <= 1250:
                if self.saldo >= valor:
                    self.saldo -= valor
                    self.extratos.append(("Empréstimo", valor))
                    print(f"Empréstimo de {valor} realizado com sucesso.")
                else:
                    print("Saldo insuficiente para empréstimo.")
            else:
                print("Valor de empréstimo excede o limite permitido.")
        else:
            print("Valor de empréstimo inválido")
            

    def get_saldo(self):
        return self.saldo

    def get_extratos(self):
        return self.extratos

    def verificar_limite_saques(self):
        now = datetime.now()
        limite = timedelta(hours=24)
        saques_recentes = [hora for hora in self.saque_horas if now - hora <= limite]
        return len(saques_recentes) < 3

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ")
    usuario = Usuario(nome, cpf, data_nascimento)
    return usuario

def criar_conta_bancaria(usuario, saldo_inicial=0):
    conta = ContaBancaria(saldo_inicial)
    usuario.conta_bancaria = conta
    return conta

# Programa principal
print("Bem-vindo ao banco X")

usuario = cadastrar_usuario()
conta = criar_conta_bancaria(usuario)

while True:
    print("\nEscolha a ação:")
    print("1. Depósito")
    print("2. Saque")
    print("3. Emprestimo")
    print("4. Saldo")
    print("5. Extratos")
    print("6. Sair")

    escolha = int(input("Digite o número da ação desejada: "))

    if escolha == 1:
        valor = int(input("Digite o valor de depósito: "))
        conta.deposito(valor)
    elif escolha == 2:
        valor = int(input("Digite o valor de saque: "))
        conta.saque(valor)
    elif escolha == 3:
        print(f"Saldo atual: {conta.get_saldo()}")
    elif escolha == 4:
        extratos = conta.get_extratos()
        print("Extratos:")
        for transacao in extratos:
            print(f"{transacao[0]}: {transacao[1]}")
    elif escolha == 5:
        print("Obrigado por usar o banco X")
        break
    else:
        print("Escolha inválida")