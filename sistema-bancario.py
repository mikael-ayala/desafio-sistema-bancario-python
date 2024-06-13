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
            print('O valor depositado precisa ser maior do que zero')

    elif opcao == 's':
        print('Saque')
        
    elif opcao == 'e':
        print('Extrato')

    elif opcao == 'q':
        break
    
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
