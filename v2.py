
import textwrap

def menu():
    menu = '''\n
    ============= menu =============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tLista de contas
    [nu]\tNovo Usuario
    [q]\tSair
    '''
    return input(textwrap.dedent(menu))
  
def cadastrar_pessoas(usuarios):
    nome =  input('Digite o nome:\t')
    data_nacimento = input('Digite a data de nascimento:\t')
    cpf = input('Digite o cpf:\t')
    endereço = input('Digite o endereço:\t')
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print('=== ja existe usuario com esse cpf! ===')
    
    usuarios.append({"nome":f"{nome}","data_nascimento:":f"{data_nacimento}","cpf" :f"{cpf}"})
    print('=== Usuario criaco com sucesso ===')
    
def conta_bancaria():
    numero = []
    num = 1087315
    numero.append(num+1)
    return print(numero[0])

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
        print('\n=== Depósito realizado com sucesso! ===')
        
    else:
        print('\n### A operação falhou! O valor informado é invalido. ###')
        
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saque, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saque >= limite_saques
    if excedeu_saldo:
        print('### A operação falhou! Voce não tem sado o suficiente! ###')
    
    elif excedeu_limite:
        print('### A operação falhou! Valor de saque excedeu o limite! ###')
        
    elif excedeu_saque:
        print('### A operação falhou! numero de saque excedido! ###')
    
    elif valor > 0:
        saldo -= valor
        num_saque += 1
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
        numero_saque += 1
        print(f'Saque: R${valor:.2f}\n')

    else:
        print('### A operação falhou! ###')
        
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
        print("============= Extrato =============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo:\t\t{saldo:.2f}")
        print("===================================")     
              
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia,numero_conta,usuarios):
    cpf = input('informe o CPF: ')
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print('\n=== Conta criada com sucesso ===')
        return {'agencia':agencia, 'numero_conta':numero_conta,'usuario':usuario}
    
    print('\n### Usuario não encontrado ###')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            agencia:\t{conta['agencia']}
            c\c:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("=" + str(100))
        print(textwrap.dedent(linha))
        
def main():
    saldo = 0
    num_saque = 0
    lim_saque = 3
    limite = 500
    extrato = ""
    usuarios = []
    contas = []
    AGENCIA = "0001"
    
    while True:
        opção = menu()
        
        if opção == 'd' :
            valor = int(input('Digite um valor: '))
            if valor > 0:
                saldo += valor
                extrato += f'Depósito:\tR$ {valor:.2f}\n'
                print('\n=== Depósito realizado com sucesso! ===')
                
            else:
                print('\n=== A operação falhou! O valor informado é invalido. ===')
                
        elif opção == 's':
            valor = int(input('Digite um valor: '))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saque = num_saque >= lim_saque
            
            if excedeu_saldo:
                print('A operação falhou! Voce não tem sado o suficiente!')
                
            
            elif excedeu_limite:
                print('A operação falhou! Valor de saque excedeu o limite!')
                
            
            elif excedeu_saque:
                print('A operação falhou! numero de saque excedido!')
                
            
            elif valor > 0:
                saldo -= valor
                num_saque += 1
                print(f'Saque: R${valor:.2f}\n')
                
        
            else:
                print('A operação falhou!!')     
                
        elif opção == 'e':
            if saldo >= 0:
                print('========= Extrato =========\n')
                if saldo == 0: 
                    print(f'Não houve movimentação\n')
                else:
                    print(f'Saldo: R$ {saldo:.2f}\n')
                    
                print('===========================')
        
        elif opção == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                
        elif opção == 'lc':
            listar_contas(contas)
        
        elif opção == 'nu':
            cadastrar_pessoas(usuarios)
            
        else:
            print("\n=== Opção invalida ===")
            

main()