

def menu():
    
    menu = """
    ====== Menu ======
    
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar usuário
    [5] Criar conta
    [6] Listar contas
    [0] Sair

    => """

    return input(menu)

def deposito(saldo, valor_deposito, extrato, /):
       
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print(f"Valor depositado em sua conta: R$ {saldo:.2f}!")

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

def saque(*, saldo, valor_saque, extrato, limite, numero_saques, limite_de_saques):
            
    if valor_saque > saldo: 
        print("Operação falhou! Não é possível fazer o saque por falta de saldo.")

    elif valor_saque > limite:
        print("Operação falhou! O valor do saque excede o limite.")
            
    elif numero_saques >= limite_de_saques:
        print("Operação falhou! Limite de saques diários excedido.")
            
    elif valor_saque > 0: 
        saldo -= valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        print(f"Valor do saque: R$ {valor_saque:.2f}")
        numero_saques += 1
    else:
        print("Operação falhou! O valor que foi informado é inválido.")

    return saldo, extrato, numero_saques          
    
def extrato_da_conta(saldo, /, *,extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Sem movimentações na conta!")
            
    else:
        print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuarios(usuarios):
    
    cpf = input("Digite o seu CPF (somente números): ")
    user = filtrar_usuarios(cpf, usuarios)

    if user:
        print("Usuário já cadastrado!")
        return 
    
   
    nome_completo = input("Digite o seu nome completo: ")
    data_de_nascimento = input("Digite sua data de nascimente (dia-mês-ano): ")
    endereco = input("Digite o seu endereço (Rua, Nro - bairro - cidade/UF): ")

    usuarios.append(({"nome_completo": nome_completo, "data_de_nascimento": data_de_nascimento, "cpf": cpf, "endereco": endereco}))

    print("Usuário criado!")


def filtrar_usuarios(cpf, usuarios):
    filtrados = [user for user in usuarios if user["cpf"] == cpf]
    return filtrados[0] if filtrados else None


def criar_contas(agencia, numero_da_conta, usuarios):

    cpf = input("Digite o seu CPF (somente numéros): ")
    user = filtrar_usuarios(cpf, usuarios)

    if user:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_da_conta": numero_da_conta, "user": user}
    
    print("Usuário não foi encontrado!")

def lista_de_contas(contas):
    for conta in contas:
        linhas = f"""Agência: {conta["agencia"]}
            Conta: {conta["numero_da_conta"]}
            Usuário da conta: {conta["user"]["nome_completo"]}
        """
        
def lista_de_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: {conta['agencia']}
            Conta: {conta['numero_da_conta']}
            Usuário da conta: {conta['user']['nome_completo']}
        """
        print(linha)
def main():
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"
    
    
    while True:
        
        opcao = menu()

        if opcao == "1":
            valor_deposito = float(input("Digite o valor que será depositado: "))
    
            saldo, extrato = deposito(saldo, valor_deposito, extrato)

        elif opcao == "2":
            valor_saque = float(input("Digite o valor que deseja sacar: "))

            saldo, extrato, numero_saques = saque(
                saldo=saldo, 
                valor_saque=valor_saque, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                limite_de_saques=LIMITE_SAQUES
                )
        
        elif opcao == "3":
            
            extrato_da_conta(saldo, extrato=extrato)
        
        elif opcao == "4":
            criar_usuarios(usuarios)

        elif opcao == "5":
            numero_de_contas = len(contas) + 1
            conta = criar_contas(AGENCIA, numero_de_contas, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "6":
            lista_de_contas(contas)
        
        elif opcao == "0":
            
            print("Obrigado por usar o nosso sistema, volte sempre!")
            break  
        else:
            print("Operação inválida, por favor escolha uma das opções do menu")
            
main()