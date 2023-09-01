from banco import obterConta, banco

def depositar(conta: int, valor: float) -> None:
    cliente = obterConta(conta)
    if valor > 0:
        if cliente:
            cliente['saldo'] += valor
            print("Deposito realizado com sucesso!")
        else:
            print("Cliente não encontrado")
    else:
        print("Valor invalido")

