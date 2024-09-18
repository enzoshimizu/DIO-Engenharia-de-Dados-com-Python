import os

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    os.system('cls')

    opcao = input(menu)

    if opcao == "d":
        os.system('cls')
        print("Depósito")
        valor = float(input("Informe o valor a ser depositado:\n"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} - Saldo: R$ {saldo:.2f}\n"
        else:
            print("\nValor inválido!")

    elif opcao == "s":
        os.system('cls')
        print("Saque")
        valor = float(input("Informe o valor a ser sacado:\n"))

        if valor <= 0:
            print("\nValor inválido!")
        elif numero_saques >= LIMITE_SAQUES:
            print("\nQuantidade máxima de saques diários atingido.")
        elif valor > saldo:
            print("\nSaldo insuficiente!")
        elif valor > limite:
            print("\nLimite diário de R$ 500,00 atingido!")
        else:
            saldo -= valor
            limite -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f} - Saldo: R$ {saldo:.2f}\n"

    elif opcao == "e":
        os.system('cls')
        print("Extrato")
        print(extrato if extrato else "Não foram realizadas movimentações.")

    elif opcao == "q":
        break

    else:
        os.system('cls')
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    input("\nPressione qualquer tecla para continuar.")
