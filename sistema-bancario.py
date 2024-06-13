menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Digite o valor que deseja depositar: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito | R$ {valor:.2f}\n'
            print(f'Deposito de R$ {valor:.2f} foi efetuado com sucesso, saldo total de R$ {saldo:.2f}.')
        else:
            print('Depósito negado! O valor depositado precisa ser maior do que zero.')

    elif opcao == 's':
        valor = float(input('Digite o valor que deseja sacar: '))
        if valor > 0 and valor <= saldo:
            saldo -= valor
            extrato += f'Saldo | R$ {valor:.2f}\n'
            print(f'Saque de R$ {valor:.2f} foi efetuado com sucesso, saldo total de R$ {saldo:.2f}.')
        elif valor > saldo:
            print('Saque negado! Valor de saque excede o valor de saldo disponível.')
        else:
            print('Saque negado! Valor de saque deve ser um número positivo.')
        
    elif opcao == 'e':
        print('Extrato')

    elif opcao == 'q':
        break
    
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
