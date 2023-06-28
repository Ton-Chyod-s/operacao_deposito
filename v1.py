
# depósito, saque e exato

menu = {
    "1": "deposito",
    "2": "Saque",
    "3": "Extrato",
    "4": "Sair"
    }

saldo = 0
num_saque = 0
lim_saque = 3
limite = 500

print(f"1-{menu['1']}")
print(f"2-{menu['2']}")
print(f"3-{menu['3']}")
print(f"4-{menu['4']}")


while True:
    
    opção = input('Digite uma opção: ')

    if opção in menu:
        opção = menu[opção]
    else:
        print("Opção inválida")
        continue
        
    while True:
        
        if opção == 'deposito' :
            valor = int(input('Digite um valor: '))
            if valor > 0:
                saldo += valor
                print(f'Deposito: R${valor:.2f}\nTotal:    R${saldo}')
                break
            else:
                print('A operação falhou!!')
                break
            
        elif opção == 'Saque':
            valor = int(input('Digite um valor: '))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saque = num_saque >= lim_saque
            
            if excedeu_saldo:
                print('A operação falhou! Voce não tem sado o suficiente!')
                break
            
            elif excedeu_limite:
                print('A operação falhou! Valor de saque excedeu o limite!')
                break
            
            elif excedeu_saque:
                print('A operação falhou! numero de saque excedido!')
                break
            
            elif valor > 0:
                saldo -= valor
                num_saque += 1
                print(f'Saque: R${valor:.2f}\nTotal:    R${saldo}')
                break
        
            else:
                print('A operação falhou!!')
                break
                
        elif opção == 'Extrato':
            if saldo >= 0:
                print('========= Estrato =========\n')
                if saldo == 0: 
                    print(f'Não houve movimentação\n')
                else:
                    print(f'Saldo: R$ {saldo:.2f}\n')
                    
                print('===========================')
                break
        
        else:
            print("Fim do programa")
            break
    
        
