from datetime import datetime

def criar_conta(usuario, contas, numero_conta_sequencial):
    conta = {   
        'agencia': '0001',
        'numero_conta': numero_conta_sequencial,
        'usuario': usuario
    }

    contas.append(conta)
    numero_conta_sequencial += 1
    return numero_conta_sequencial

def adicionar_usuario(usuarios):
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    cpf = input("CPF (somente números): ")

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Já existe um usuário cadastrado com esse CPF.")
            return usuarios 

    logradouro = input("Logradouro: ")
    num = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Sigla do Estado (ex: SP): ")

    endereco = f"{logradouro}, {num} - {bairro} - {cidade}/{estado}"

    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco,
    }
    usuarios.append(usuario)
    print("Usuário cadastrado!")
    return usuarios

def exibir_dados(usuarios, contas):
    if not usuarios:
        print("Nenhum usuário cadastrado!")
    else:
        for usuario in usuarios:
            print(f"""
                Nome: {usuario['nome']}
                Data de Nascimento: {usuario['data_nascimento']}
                CPF: {usuario['cpf']}
                Endereço: {usuario['endereco']}
            """)

            contas_do_usuario = [conta for conta in contas if conta['usuario'] == usuario['nome']]
            if contas_do_usuario:
                for conta in contas_do_usuario:
                    print(f"""
                Agência: {conta['agencia']}
                Número da Conta: {conta['numero_conta']}
                    """)
            else:
                print("    Nenhuma conta associada a este usuário.")

def verificar_saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Você não tem saldo suficiente.")
        return saldo, extrato, numero_saques
    
    if valor > limite:
        print("Você excedeu o limite.")
        return saldo, extrato, numero_saques
    
    if numero_saques >= limite_saques:
        print("Você atingiu o limite de saques.")
        return saldo, extrato, numero_saques
    
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    return saldo, extrato, numero_saques + 1    

def deposito(valor, /, extrato, saldo):
    if valor < 0:
        print("A operação falhou! Tente novamente.")
        return saldo, extrato

    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato

def exibir_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
contas = []
numero_conta_sequencial = 1

menu = """
[ad] Adicionar Usuário
[cc] Cadastrar Conta
[d] Depositar
[s] Sacar
[e] Extrato
[eu] Exibir Usuários e Contas
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 10
usuarios = []

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: ")) 
        saldo, extrato = deposito(valor, extrato, saldo)
        
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = verificar_saque(
            saldo=saldo, valor=valor, extrato=extrato, 
            limite=limite, limite_saques=LIMITE_SAQUES, 
            numero_saques=numero_saques
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "ad":
        usuarios = adicionar_usuario(usuarios)

    elif opcao == 'eu':
        exibir_dados(usuarios, contas)

    elif opcao == "cc":
        usuario_conta = input("Informe o nome do usuário para criar a conta: ")
        numero_conta_sequencial = criar_conta(usuario_conta, contas, numero_conta_sequencial)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
