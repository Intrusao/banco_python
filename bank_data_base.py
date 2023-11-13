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

def cadastrar_usuario(usuarios):
    cpf = input("Digite o CPF do usuário: ")

    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("CPF já cadastrado. Não é permitido mais de um cadastro com o mesmo CPF.")
            return None

    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ")
    usuario = Usuario(nome, cpf, data_nascimento)
    usuarios.append(usuario)
    return usuario

def criar_conta_bancaria(usuario, saldo_inicial=0):
    conta = ContaBancaria(saldo_inicial)
    usuario.conta_bancaria = conta
    return conta

print("Bem-vindo ao banco X")

usuarios = []
conta = ContaBancaria()  # Corrija a linha que cria uma instância de ContaBancaria

while True:
    print("\nEscolha a ação:")
    print("1. Cadastrar Usuário")
    print("2. Depósito")
    print("3. Saque")
    print("4. Empréstimo")
    print("5. Saldo")
    print("6. Extratos")
    print("7. Sair")

    escolha = int(input("Digite o número da ação desejada: "))

    if escolha == 1:
        usuario = cadastrar_usuario(usuarios)
        if usuario:
            criar_conta_bancaria(usuario)
            print("Usuário cadastrado com sucesso.")
    elif escolha == 2:
        valor = int(input("Digite o valor de depósito: "))
        conta.deposito(valor)
    elif escolha == 3:
        valor = int(input("Digite o valor de saque: "))
        conta.saque(valor)
    elif escolha == 4:
        valor = int(input("Digite o valor do empréstimo: "))
        conta.emprestimo(valor)
    elif escolha == 5:
        print(f"Saldo atual: {conta.get_saldo()}")
    elif escolha == 6:
        extratos = conta.get_extratos()
        print("Extratos:")
        for transacao in extratos:
            print(f"{transacao[0]}: {transacao[1]}")
    elif escolha == 7:
        print("Obrigado por usar o banco X")
        break
    else:
        print("Escolha inválida")


