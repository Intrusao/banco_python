from datetime import datetime, timedelta

class ContaBancaria:
    def __init__(self):
        self.saldo = 5000
        self.extratos = []
        self.saque_horas = []  # Lista para registrar as horas dos saques

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
                    # Verifica o limite de 3 saques nas últimas 24 horas
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

    def get_saldo(self):
        return self.saldo

    def get_extratos(self):
        return self.extratos

    def verificar_limite_saques(self):
        now = datetime.now()
        limite = timedelta(hours=24)
        saques_recentes = [hora for hora in self.saque_horas if now - hora <= limite]
        return len(saques_recentes) < 3

conta = ContaBancaria()

while True:
    print("Escolha a ação:")
    print("1. Depósito")
    print("2. Saque")
    print("3. Saldo")
    print("4. Extratos")
    print("5. Sair")

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
