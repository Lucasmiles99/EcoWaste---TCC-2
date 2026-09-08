from repositories.checklist_repository import (
    ChecklistRepository
)

class ChecklistService:
    """
    Camada de serviço responsável
    pelas regras de negócio do
    Checklist Ambiental.
    """

    @staticmethod
    def listar_municipios():
        """
        Retorna todos os municípios
        cadastrados.
        """

        return (
            ChecklistRepository
            .listar_municipios()
        )

    @staticmethod
    def buscar_municipio(
        municipio_id
    ):
        """
        Busca um município pelo ID.
        """

        if municipio_id is None:
            return None

        return (
            ChecklistRepository
            .buscar_municipio_por_id(
                municipio_id
            )
        )

    @staticmethod
    def listar_perguntas():
        """
        Retorna todas as perguntas
        do Checklist Ambiental.
        """

        return (
            ChecklistRepository
            .listar_perguntas()
        )

    @staticmethod
    def obter_checklist_municipio(
        municipio_id
    ):
        """
        Retorna o checklist completo
        de um município.

        Inclui:
        - município
        - perguntas
        - respostas
        - quantidade de respostas
        - percentual respondido
        """

        municipio = (
            ChecklistRepository
            .buscar_municipio_por_id(
                municipio_id
            )
        )

        if municipio is None:
            return None

        checklist = (
            ChecklistRepository
            .listar_checklist_por_municipio(
                municipio_id
            )
        )

        total_perguntas = len(
            checklist
        )

        total_respondidas = 0

        for item in checklist:

            resposta = item[
                "resposta"
            ]

            if (
                resposta is not None
                and resposta.strip()
            ):

                total_respondidas += 1

        percentual = 0

        if total_perguntas > 0:

            percentual = round(
                (
                    total_respondidas
                    / total_perguntas
                )
                * 100,
                1
            )

        return {
            "municipio":
                municipio,

            "checklist":
                checklist,

            "total_perguntas":
                total_perguntas,

            "total_respondidas":
                total_respondidas,

            "percentual":
                percentual
        }