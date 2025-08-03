saldo: float = 0.0
usuarios: list[str] = []
contas: list[str] = []

def exibir_menu() -> None:
    print("1. Cadastrar Usuário")
    print("2. Criar Conta Bancária")
    print("3. Depositar Dinheiro")
    print("4. Sacar Dinheiro")
    print("5. Verificar Saldo")
    print("6. Listar Usuários")
    print("7. Sair")

def cadastrar_usuario(nome: str, idade: int, cpf: str, endereco: str) -> None:
    print(f"Usuário {nome} cadastrado com sucesso!")

def criar_conta_bancaria(agencia: int, numero_conta: int, cpf: str) -> None:
    print(f"Conta bancária criada com CPF {cpf}.")

def depositar_saldo(valor: float) -> None:
    global saldo
    saldo += valor
    print("Depósito realizado com sucesso!", saldo)

def sacar_saldo(valor: float) -> None:
    global saldo
    if valor > saldo:
        print("Saldo insuficiente!")
    else:
        saldo -= valor
        print("Saque realizado com sucesso!", saldo)

def verificar_saldo() -> None:
    print("Saldo atual: ", saldo)

def listar_usuarios() -> None:
    print(f"Lista de usuários: {usuarios}")

def sair() -> None:
    print("Saindo do programa...")

while True:
    exibir_menu()
    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            nome = input("Digite o nome do usuário: ")
            idade = int(input("Digite a idade do usuário: "))
            cpf = input("Digite o CPF do usuário: ")
            endereco = input("Digite o endereço do usuário: ")
            cadastrar_usuario(nome, idade, cpf, endereco)
            usuarios.append(f"Nome: {nome}, Idade: {idade}, CPF: {cpf}, Endereço: {endereco}")
        case 2: 
            agencia = int(input("Digite o número da agência: "))
            numero_conta = int(input("Digite o número da conta: "))
            cpf = input("Digite o CPF do usuário: ")
            criar_conta_bancaria(agencia, numero_conta, cpf)
            contas.append(f"Agência: {agencia}, Conta: {numero_conta}, CPF: {cpf}")
        case 3: 
            valor = float(input("Digite o valor a depositar: "))
            depositar_saldo(valor)
        case 4:
            valor = float(input("Digite o valor a sacar: "))
            sacar_saldo(valor)
        case 5:
            verificar_saldo()
        case 6:
            listar_usuarios()
        case 7:
            sair()
            break;
        case _:
            print("Opção inválida. Tente novamente.")