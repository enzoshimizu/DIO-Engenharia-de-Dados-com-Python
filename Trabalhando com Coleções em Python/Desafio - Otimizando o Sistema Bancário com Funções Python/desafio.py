import os
from datetime import datetime

def depositar(saldo, valor, extrato):
    if valor > 0:
        extrato.append({
            "data": datetime.now(),
            "operacao": "D",
            "valor": valor,
        })
        saldo += valor
        
        print(f"Depósito de R$ {valor:.2f} realizado.")
    else:
        print("\nValor inválido!")
        
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, limite_saques):
    saque_diario = 1
    valor_diario = valor
    
    for transacao in extrato:
        if transacao['data'].date() == datetime.now().date() and transacao['operacao'] == "S":
            saque_diario += 1
            valor_diario += transacao['valor']
            
    if valor <= 0:
        print("\nValor inválido!")
    elif valor > saldo:
        print("\nSaldo insuficiente!")
    elif saque_diario > limite_saques:
        print("\nQuantidade máxima de saques diários atingida.")
    elif valor_diario > limite:
        print("\nLimite diário de R$ 500,00 atingido!")
    else:
        saldo -= valor
        extrato.append({
            "data": datetime.now(),
            "operacao": "S",
            "valor": valor,
        })
        
    return saldo, extrato

def listar_extrato(extrato):
    if not extrato:
        print("Não houveram transações nesta conta.")
    else:
        for transacao in extrato:        
            print(f"Data: {transacao['data']:%d/%m/%y %H:%M} - Operação: {'Depósito' if transacao['operacao'] == "D" else 'Saque'} - Valor: R$ {transacao['valor']:.2f}")

def criar_usuario(usuarios, nome, data_nascimento, cpf, logradouro, numero, bairro, cidade):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print('Usuário já cadastrado')
            return usuarios
    
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'logradouro': logradouro,
        'numero': numero,
        'bairro': bairro,
        'cidade': cidade,
    })
    
    return usuarios

def criar_conta_corrente(contas_correntes, usuarios, agencia, cpf_usuario):
    usuario_existe = False
    
    for usuario in usuarios:
        if usuario['cpf'] == cpf_usuario:
            usuario_existe = True
    
    if not usuario_existe:
        print('Usuário inexistente.')
        return contas_correntes
   
    numero = len(contas_correntes) + 1
             
    contas_correntes.append({
        'agencia': agencia,
        'numero': numero,
        'usuario': usuario,
    })
    
    return contas_correntes

menu = """

[c] Cadastrar Usuário
[cc] Cadastrar Conta Corrente
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

usuarios = []
contas_correntes = []

LIMITE = 500
LIMITE_SAQUES = 3
saldo = 0
extrato = []

while True:
    os.system('cls')

    opcao = input(menu)

    if opcao == "c":
        os.system('cls')
        print("Cadastrar Usuário")
        nome = input("Informe o nome:\n")
        data_nascimento = datetime.strptime(input("Informe a data de nascimento (dd/mm/aaaa):\n"), '%d/%m/%Y') 
        cpf = int(input("Informe o CPF (apenas números):\n"))
        logradouro = input("Informe o logradouro:\n")
        numero = int(input("Informe o número:\n"))
        bairro = input("Informe o bairro:\n")
        cidade = input("Informe a cidade/UF:\n")
        
        criar_usuario(usuarios, nome, data_nascimento, cpf, logradouro, numero, bairro, cidade)
        
    elif opcao == "cc":
        os.system('cls')
        print("Cadastrar Conta Corrente")
        agencia = int(input("Informe a agência:\n"))
        cpf_usuario = int(input("Informe o CPF (apenas números):\n"))
        
        criar_conta_corrente(contas_correntes, usuarios, agencia, cpf_usuario)
        
    elif opcao == "d":
        os.system('cls')
        print("Depósito")
        valor = float(input("Informe o valor a ser depositado:\n"))

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        os.system('cls')
        print("Saque")
        valor = float(input("Informe o valor a ser sacado:\n"))
        
        saldo, extrato = sacar(saldo, valor, extrato, LIMITE, LIMITE_SAQUES)

    elif opcao == "e":
        os.system('cls')
        print("Extrato")
        listar_extrato(extrato)

    elif opcao == "q":
        break

    else:
        os.system('cls')
        print("Operação inválida, por favor selecione novamente a operação desejada.")

    input("\nPressione qualquer tecla para continuar.")
