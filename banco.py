from typing import Optional

banco = [
    {"conta": 1, "cliente": "Marcos", "saldo": 150.50},
    {"conta": 2, "cliente": "Mariana", "saldo": 320.00}
]

conta_atual = 2


def adicionarConta(nome: str, saldo: float) -> None:
    global conta_atual
    conta_atual += 1
    conta = {
        "conta": conta_atual,
        "cliente": nome,
        "saldo": saldo
    }
    banco.append(conta)
    print("Conta cadastrada com sucesso!")


def obterConta(conta: int) -> Optional[dict or None]:
    for cliente in banco:
        if cliente['conta'] == conta:
            return cliente
    return None


def buscarCliente(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:

        print(f"N. Conta: {cliente['conta']}")
        print(f"Nome: {cliente['cliente']}")
        print(f"Saldo: {cliente['saldo']}")
    else:
        print('Cliente não existe!')


def listarTodos() -> None:
    for cliente in banco:
        buscarCliente(cliente['conta'])
        print('---------------')


def editarNome(conta: int, novo_nome: str) -> None:
    cliente = obterConta(conta)
    if cliente:
        cliente['cliente'] = novo_nome
        print('Dados alterados com sucesso!')
    else:
        print('Cliente não encontrado!')


def removerConta(conta: int) -> None:
    cliente = obterConta(conta)
    if cliente:
        banco.remove(cliente)
        print('Cliente removido com sucesso!')
    else:
        print('Cliente não encontrado!')
