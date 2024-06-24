# -*- coding: utf-8 -*-
"""sistema_bancário.v3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d8vlYNKMhwQFBRKoQZZkbXCh-FOICFsF
"""

import textwrap

class Menu:
    @staticmethod
    def exibir_menu():
        menu = """\n
        ================ MENU ================
        [d]\tDepositar
        [s]\tSacar
        [e]\tExtrato
        [nc]\tNova conta
        [lc]\tListar contas
        [nu]\tNovo usuário
        [q]\tSair
        => """
        return input(textwrap.dedent(menu))

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class Conta:
    LIMITE_SAQUES = 3
    LIMITE_SAQUE = 500

    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.extrato = ""
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def sacar(self, valor):
        if valor > self.saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif valor > self.LIMITE_SAQUE:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        elif valor > 0:
            self.saldo -= valor
            self.extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            self.numero_saques += 1
            print("\n=== Saque realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("==========================================")

class Banco:
    AGENCIA = "0001"

    def __init__(self):
        self.usuarios = []
        self.contas = []

    def criar_usuario(self):
        cpf = input("Informe o CPF (somente número): ")
        if self.filtrar_usuario(cpf):
            print("\n@@@ Já existe usuário com esse CPF! @@@")
            return

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        usuario = Usuario(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(usuario)
        print("=== Usuário criado com sucesso! ===")

    def filtrar_usuario(self, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None

    def criar_conta(self):
        cpf = input("Informe o CPF do usuário: ")
        usuario = self.filtrar_usuario(cpf)
        if not usuario:
            print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
            return

        numero_conta = len(self.contas) + 1
        conta = Conta(self.AGENCIA, numero_conta, usuario)
        self.contas.append(conta)
        print("\n=== Conta criada com sucesso! ===")

    def listar_contas(self):
        for conta in self.contas:
            print("=" * 100)
            print(f"Agência:\t{conta.agencia}")
            print(f"C/C:\t\t{conta.numero_conta}")
            print(f"Titular:\t{conta.usuario.nome}")

    def executar(self):
        while True:
            opcao = Menu.exibir_menu()
            if opcao == "d":
                conta_numero = int(input("Informe o número da conta: "))
                valor = float(input("Informe o valor do depósito: "))
                self.contas[conta_numero - 1].depositar(valor)
            elif opcao == "s":
                conta_numero = int(input("Informe o número da conta: "))
                valor = float(input("Informe o valor do saque: "))
                self.contas[conta_numero - 1].sacar(valor)
            elif opcao == "e":
                conta_numero = int(input("Informe o número da conta: "))
                self.contas[conta_numero - 1].exibir_extrato()
            elif opcao == "nu":
                self.criar_usuario()
            elif opcao == "nc":
                self.criar_conta()
            elif opcao == "lc":
                self.listar_contas()
            elif opcao == "q":
                break
            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    banco = Banco()
    banco.executar()