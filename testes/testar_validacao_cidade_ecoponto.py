from services.ecoponto_service import EcopontoService

def testar_cidade_valida():
    service = EcopontoService()

    cidade = service.validar_cidade(
        "Rio do Sul"
    )

    print(
        f"Cidade válida aceita corretamente: {cidade}"
    )

def testar_cidade_invalida():
    service = EcopontoService()

    try:
        service.validar_cidade(
            "Florianópolis"
        )

        print(
            "ERRO: cidade inválida foi aceita."
        )

    except ValueError as erro:
        print(
            "Cidade inválida rejeitada corretamente."
        )

        print(
            f"Mensagem: {erro}"
        )

if __name__ == "__main__":
    print(
        "=== TESTE DE VALIDAÇÃO DE CIDADE DO ECOPOINT ==="
    )

    print()

    testar_cidade_valida()

    print()

    testar_cidade_invalida()