menu = """

[d] -> Depositar
[s] -> Sacar
[e] -> Ver Extrato
[q] -> Sair

"""

saldo = 0 
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True: 

    opcao = input(menu)

    if opcao == "d":
        
        valor = float(input("Informe o Valor do Deposito "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Déposito: R$ {valor:.2f}\n"
            print(f"Déposito feito: R$ {valor:.2f}\n")
        else:
            print("Valor Invalido, Operação Não Pode Ser Realizada")

    elif opcao == "s":
        
        valor = float(input("Informe o Valor do Saque "))

        exedeu_saldo = valor > saldo

        exedeu_limite = valor > limite

        exedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES

        if exedeu_saldo:
            print("Erro!!! Saldo Insuficiente!")
        
        elif exedeu_limite:
            print("Erro!!! Excedeu o Limite!")
        
        elif exedeu_saques:
            print("Erro!!! Limite Diario Alcançado!")    
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque feito R$ {valor:.2f}\n"
            numero_de_saques += 1
            print(f"Saque feito: R$ {valor:.2f}\n")
        else:
            print("Operação Falhou!!! Valor Invalido!")
    
    elif opcao == "e":
        print("\n========== EXTRATRO ==========")
        print("\nNão Foram Realizadas Movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}\n")
        print("\n==============================")

    elif opcao == "q":
        break

    else:
        print("Operação Invalida!!! Selecione Novamente!")         