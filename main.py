from banco import *
from operacoes.depostito import depositar
from operacoes.saque import sacar
from operacoes.consulta import consultarSaldo
from operacoes.tranferencia import transferir


def menu():
    while True:
        print("----Sistema Bancário----")
        opcao = int(input("1 - ADICIONAR CONTA \n"
                          "2 - EDITAR CONTA \n"
                          "3 - CONSULTAR CONTA \n"
                          "4 - APAGAR CONTA \n"
                          "5 - LISTAR CONTAS \n"
                          "6 - REALIZAR SAQUE \n"
                          "7 - REALIZAR DEPOSITO \n"
                          "8 - TRANFERENCIA\n"
                          "9 - CONSULTA SALDO\n"
                          "10 - SAIR  \n"
                          "ESCOLHA UMA OPÇÃO = > "
                          ))

        if opcao == 1:
            nome = input("Digite o nome do cliente: ")
            saldo = float(input("Digite o saldo: "))
            adicionarConta(nome, saldo)

        elif opcao == 2:
            conta = int(input("Digite o núme da conta: "))
            nome = input("Digite o novo nome do cliente: ")
            editarNome(conta, nome)

        elif opcao == 3:
            conta = int(input("Digite o número da conta: "))
            buscarCliente(conta)

        elif opcao == 4:
            conta = int(input("Digite o numero da conta: "))
            removerConta(conta)

        elif opcao == 5:
            listarTodos()

        elif opcao == 6:
            conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor do saque"))
            sacar(conta, valor)

        elif opcao == 7:
            conta = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor do saque"))
            depositar(conta, valor)

        elif opcao == 8:
            contaOrigem = int(input("Informe a conta de origem: "))
            contaDestino = int(input("Informe a conta de destino: "))
            valor = float(input("Digite o valor que deseja tranferir: "))
            transferir(contaOrigem, contaDestino, valor)
        elif opcao == 9:
            conta = int(input("Digite o número da conta: "))
            consultarSaldo(conta)

        elif opcao == 10:
            print("---VC SAIU DO PROGRAMA---")
            break

        else:
            print("Opção Invalida")

menu()
