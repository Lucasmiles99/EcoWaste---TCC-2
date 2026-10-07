from services.relatorio_service import RelatorioService

def testar_exportacao_checklist():
    print("=== TESTE DE EXPORTAÇÃO DO CHECKLIST AMBIENTAL ===")

    caminho_arquivo = RelatorioService.gerar_csv_checklist()

    print()
    print("Arquivo CSV gerado com sucesso.")
    print(f"Caminho: {caminho_arquivo}")

if __name__ == "__main__":
    testar_exportacao_checklist()