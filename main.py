menu = """
        Movimentação de Conta Corrente

            Selecione uma opção:
            [d] Depositar
            [s] Sacar
            [e] Extrato
            [q] Sair

=> """

limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3


def saldo(extrato):
    return sum(extrato)

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Entre com o valor do depósito: "))
        if valor > 0:
            extrato.append(valor)
        else:
            print('Valor não pode ser negativo')
    elif opcao == 's':
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Entre com o valor de saque: "))
            if valor > limite:
                print(f'Valor excede limite de saque. Limite: R$ {limite}')
            elif valor < 0:
                print('Valor não pode ser negativo')        
            else:
                if valor <= saldo(extrato): 
                    extrato.append(-valor)
                    numero_saques += 1
                else:
                    print(f'Saldo insuficiente para saque. Total em conta: R$ {saldo(extrato)}')
        else:
            print('Limite de saques diários atingido (Máximo 3)')
    elif opcao == 'e':
        if extrato == []:
            print('Não foram realizadas movimentações!')
        else:
            for item in extrato:
                if item >= 0:
                    print(f'C R$ {item}')
                else:
                    print(f'D R$ {item}')
            print(f'Saldo: R$ {saldo(extrato)}')

    elif opcao == 'q':
        break
    else:
        print("Opção inválida!")
