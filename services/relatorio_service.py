import csv
import os

from repositories.checklist_repository import ChecklistRepository

class RelatorioService:
    """
    Responsável pela geração de relatórios
    e exportação dos dados do EcoWaste.
    """

    PASTA_DADOS = "dados"
    ARQUIVO_CHECKLIST = "checklist_ambiental.csv"

    @staticmethod
    def padronizar_resposta(resposta):
        """
        Padroniza somente respostas negativas
        que possuem apenas a palavra "não",
        sem qualquer complemento.

        Respostas descritivas são preservadas.

        Perguntas ainda não respondidas
        permanecem vazias.
        """

        if resposta is None:
            return ""

        resposta = resposta.strip()

        if not resposta:
            return ""

        resposta_normalizada = resposta.upper()

        if resposta_normalizada in ("NÃO", "NAO"):
            return "Não"

        return resposta

    @staticmethod
    def gerar_csv_checklist():
        """
        Gera um arquivo CSV contendo os dados
        do Checklist Ambiental de todos os municípios.

        Cada linha representa uma pergunta
        referente a um município.

        Estrutura:

        municipio
        numero_pergunta
        pergunta
        resposta

        Municípios sem respostas também aparecem
        no arquivo, pois todas as perguntas são
        mantidas para futura coleta de dados.
        """

        os.makedirs(
            RelatorioService.PASTA_DADOS,
            exist_ok=True
        )

        caminho_arquivo = os.path.join(
            RelatorioService.PASTA_DADOS,
            RelatorioService.ARQUIVO_CHECKLIST
        )

        municipios = (
            ChecklistRepository.listar_municipios()
        )

        with open(
            caminho_arquivo,
            mode="w",
            newline="",
            encoding="utf-8-sig"
        ) as arquivo:

            campos = [
                "municipio",
                "numero_pergunta",
                "pergunta",
                "resposta"
            ]

            escritor = csv.DictWriter(
                arquivo,
                fieldnames=campos,
                delimiter=";"
            )

            escritor.writeheader()

            for municipio in municipios:

                checklist = (
                    ChecklistRepository
                    .listar_checklist_por_municipio(
                        municipio.id
                    )
                )

                for item in checklist:

                    resposta = (
                        RelatorioService
                        .padronizar_resposta(
                            item["resposta"]
                        )
                    )

                    escritor.writerow({
                        "municipio":
                            municipio.nome,

                        "numero_pergunta":
                            item["numero"],

                        "pergunta":
                            item["pergunta"],

                        "resposta":
                            resposta
                    })

        return caminho_arquivo