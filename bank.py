saldo: float = 0.0

def exibir_menu() -> None:
    print("1. Depositar Dinheiro")
    print("2. Sacar Dinheiro")
    print("3. Verificar Saldo")
    print("4. Sair")

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

def sair() -> None:
    print("Saindo do programa...")

while True:
    exibir_menu()
    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1:
            valor = float(input("Digite o valor a depositar: "))
            depositar_saldo(valor)
        case 2: 
            valor = float(input("Digite o valor a sacar: "))
            sacar_saldo(valor)
        case 3: 
            verificar_saldo()
        case 4:
            sair()
            break
        case _:
            print("Opção inválida. Tente novamente.")