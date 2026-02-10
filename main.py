clients = {}
accounts = []
historico = []
money = 0

def depositar(money, historico):
    deposit = int(input("Diga o valor do depósito: "))

    if deposit <= 0:
        print("Depósito inválido")
        return money, historico

    money += deposit
    historico.append({
        "type": "depósito",
        "valor": f"+{deposit}"
    })

    print("Depósito realizado. Novo saldo:", money)
    return money, historico


def saque(money, historico):
    print("Saldo atual:", money)
    withdraw = int(input("Digite o valor do saque: "))

    if withdraw <= 0 or withdraw > money:
        print("Saque inválido")
        return money, historico

    money -= withdraw
    historico.append({
        "type": "saque",
        "valor": f"-{withdraw}"
    })

    print("Saque realizado. Novo saldo:", money)
    return money, historico


while True:
    print("\n==========================================")
    print("🏦 Projeto: Sistema Bancário Simples")
    print("1 - Cadastrar cliente")
    print("2 - Criar conta")
    print("3 - Operações bancárias")
    print("4 - Exibir dados da conta")
    print("5 - Encerrar sistema")
    print("==========================================")
    option = input("Escolha uma opção: ")

    if option == "1":
        clients["nome"] = input("Nome do cliente: ")
        cpf = input("CPF do cliente: ")

        cpf_limpo = cpf.replace(".", "").replace("-", "")
        if len(cpf_limpo) == 11 and cpf_limpo.isdigit():
            clients["cpf"] = cpf_limpo
            print("Cliente cadastrado com sucesso.")
            
        else:
            print("CPF inválido.")

    elif option == "2":
        account_number = input("Número da conta: ")
        cpf_account = input("CPF do titular: ")
        money = int(input("Saldo inicial: "))

        historico = []

        accounts.append({
            "numero": account_number,
            "cpf": cpf_account,
            "saldo": money,
            "historico": historico
        })

        print("Conta criada com sucesso.")

    elif option == "3":
        if not accounts:
            print("Nenhuma conta criada.")
            continue
        print("==========================================")
        print("\n1 - Fazer depósito")
        print("2 - Fazer saque")
        print("==========================================")
        bank = input("Escolha uma opção: ")

        conta = accounts[-1]

        if bank == "1":
            money, historico = depositar(conta["saldo"], conta["historico"])
            conta["saldo"] = money

        elif bank == "2":
            money, historico = saque(conta["saldo"], conta["historico"])
            conta["saldo"] = money

    elif option == "4":
        if not accounts:
            print("Nenhuma conta para exibir.")
        else:
            conta = accounts[-1]
            print("\nNúmero da conta:", conta["numero"])
            print("CPF:", conta["cpf"])
            print("Saldo:", conta["saldo"])
            print("Histórico:")
            if not conta["historico"]:
                print("Sem movimentações.")
            else:
                for item in conta["historico"]:
                    print(item["type"], item["valor"])

    elif option == "5":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")
