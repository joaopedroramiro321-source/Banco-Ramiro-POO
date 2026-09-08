from conta import Conta
conta1 = Conta('', '', 0, 0)

print('Bem vindo ao Banco Ramiro!\n')
escolha = 4

while escolha != 3:
    print('MENU:\n     (1) Criar conta\n     (2) Acessar conta\n     (3) Encerrar')
    escolha = int(input('Digite o número do que deseja fazer: '))

    if escolha == 1:
        conta1.set_titular(input('Informe seu nome: '))
        conta1.set_saldo(int(input('informe quanto deseja depositar inicialmente: ')))
        conta1.set_numero(123-4)
        conta1.set_limite(conta1.get_saldo() * 2)
        print('Conta criada!')
        print('Obrigado por escolher o Banco Ramiro!')

    elif escolha == 2:
        print(f'Bem vindo {conta1.get_titular}!')
        print('    (1) Consultar saldo\n    (2) Depositar\n    (3) sacar\n    (4) Encerrar')
        escolha2 = int(input('Digite o que deseja fazer: '))
        if escolha2 == 1:
            print(f'Você tem {conta1.get_saldo()} de saldo')
        elif escolha2 == 2:
            conta1.deposito(int(input('Informe quanto deseja depositar: ')))
            print(f'Deposito realizado!\nAgora você tem {conta1.get_saldo()} de saldo')
        elif escolha2 == 3:
            conta1.saque(int(input('Informe quanto deseja sacar: ')))
            print(f'Saque realizado, agora você tem {conta1.get_saldo()} de saldo')
        elif escolha2 == 4:
            break
        else:
            print('O número digitado é invalido')

    elif escolha == 3:
        print('Encerrando operação...')
        break

    else:
        print('O número digitado é invalido')
    




"""
conta1.extrato()

conta1.deposito(50)
conta1.extrato()

conta1.saque(20)
conta1.extrato()

print(conta1.numero)
print(conta1.titular)
print(conta1.saldo)
print(conta1.limite)
"""