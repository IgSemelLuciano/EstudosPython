#define a senha
defsenha=input('Escolha sua senha: ')
#inicio da interface de uso
nomeusuario=input('Digite seu Nome: ')
for i in range(1,10):
    print('''
          ''')
print('        Olá!', nomeusuario)
print('')
#inserir senha, caso haja 5 tentativas, o programa fecha
i=0
while True:
    if i==5:
        exit()
    tentativasenha=input('     Insira sua Senha para entrar: ')
    if tentativasenha==defsenha:
        break
    else:
        i+=1
        print('   Senha Incorreta, tente novamente, você tem '+ str(5-i)+ ' tentativas.')
        print('''
              ''')
#abre a interface do usuário        
def menu():
    for i in range(1,10):
        print('''
              ''')
    print('''
    _____________________________________
    1 - Consultar Saldo
    2 - Depositar
    3 - Sacar
    4 - Sair
    _____________________________________
    ''')
menu()
#dá inicio as operações
saldo=0.0
while True:
    operacao=int(input('Qual Operação deve ser feita?: '))
    if operacao==1:
        menu()
        print('Seu saldo é:',str(saldo))
    elif operacao==2:
       deposito=float(input('Qual o valor que você deseja depositar?: '))
       saldo=deposito+saldo
       menu()
       print(' O valor de',deposito,'foi depositado com sucesso! ')
    elif operacao==3:
        retirada=float(input('Quanto deseja sacar?: '))
        if saldo<retirada:
            menu()
            print(' Saldo Insuficiente! ')
        else:
            saldo = saldo-retirada
            menu()
            print('O valor de',retirada,'foi retirado com sucesso!')
    elif operacao == 4:
        print('Finalizado com Sucesso')
        break
    else:
        operacao != 1 or 2 or 3 or 4
        menu()
        print('Por favor, escolha apenas valores de 1 a 4')
exit()