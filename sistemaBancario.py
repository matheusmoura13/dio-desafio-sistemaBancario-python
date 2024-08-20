menu = """

[0] Depositar
[1] Sacar
[2] Extrato
[Exit] Sair

=> """

saldo = 0
limite_De_Saque = 500
QTDE_DE_SAQUE = 3
saque_Inicial = 0
extrato = ""

while True:

    opcao = input(menu)

    if opcao == "0":

        valor = float(input("Informe o valor do depósito:"))
        
        if valor > 0:

            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            
            print("Deposite um valor válido!")

    elif opcao == "1":

        saque = float(input("Informe o valor a sacar:"))

        excedeu_saldo = saque > saldo
        excedeu_tentativas = saque_Inicial >= QTDE_DE_SAQUE
        excedeu_limite = saque > limite_De_Saque
    
        if excedeu_saldo:

            print("Operação falhou! Saque maior que o saldo em conta.")

        elif excedeu_limite:

            print("Operação falhou! Saque maior que o limite permitido.")

        elif excedeu_tentativas:

            print("Operação falhou! O saque excedeu o número de tentativas.")

        elif saque <= saldo:

            saldo -= saque
            extrato += f"Saque: R$ {valor:.2f}\n"
            saque_Inicial += 1

    elif opcao == "2":

        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "Exit":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
