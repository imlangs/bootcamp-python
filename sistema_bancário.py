# -*- coding: utf-8 -*-
"""sistema_bancário

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tdXkuKY6vU8jCQv129mVoPuL-0U98rX4
"""

saldo = 0
qtd_saque = 0
saques = []

def deposito(valor):
    global saldo
    saldo += valor
    print(f'Depósito de R${valor} realizado. Novo saldo: R${saldo}')

def saque(valor):
    global saldo, qtd_saque, saques
    if valor > saldo:
        print('Saldo insuficiente para saque.')
    elif valor <= 500.00:
        saldo -= valor
        qtd_saque += 1
        saques.append(valor)
        print(f'Saque de R${valor} realizado. Novo saldo: R${saldo}')
    else:
        print("Valor limite por saque é R$500,00. Tente outro valor.")

def extrato():
    global saldo
    print(f'Saldo disponível: R${saldo}')

def main():

    qtd_deposito = 0
    depositos = []
    menu = """ \nSelecione a operação:

    1. Depósito
    2. Saque
    3. Extrato
    4. Sair
    """

    while True:

        print(menu)
        opcao = input('Digite o número da operação desejada: ')

        if opcao == '1':
            valor = float(input('Digite o valor do depósito: '))
            if valor > 0:
                deposito(valor)
                depositos.append(valor)
            else:
                print('Valor inválido. Por favor, digite novamente.')

        elif opcao == '2':
            if qtd_saque < 3:
                valor = float(input('Digite o valor do saque: '))
                saque(valor)
            else:
                print("Limite de saques excedido.")

        elif opcao == '3':
            print("============== EXTRATO ==============")
            if not depositos and not saques:
                print("Nenhuma movimentação financeira realizada.")
            else:
                extrato()
                print("Depósitos realizados: ", end="")
                print(", ".join([f'R${valor:.2f}' for valor in depositos]))
                print("Saques realizados: ", end="")
                print(", ".join([f'R${valor:.2f}' for valor in saques]))

        elif opcao == '4':
            print('Saindo do sistema bancário.')
            break

        else:
            print('Opção inválida. Por favor, digite novamente.')

if __name__ == "__main__":
    main()