from database.connection import conectar
from models.checklist import (
    Municipio,
    PerguntaChecklist,
    RespostaChecklist
)

class ChecklistRepository:
    """
    Responsável pelo acesso aos dados
    do Checklist Ambiental.
    """

    @staticmethod
    def listar_municipios():
        """
        Retorna todos os municípios
        cadastrados em ordem alfabética.
        """

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                id,
                nome
            FROM municipio
            ORDER BY nome ASC
        """)

        registros = cursor.fetchall()

        conexao.close()

        municipios = []

        for registro in registros:

            municipio = Municipio(
                id=registro["id"],
                nome=registro["nome"]
            )

            municipios.append(
                municipio
            )

        return municipios

    @staticmethod
    def buscar_municipio_por_id(
        municipio_id
    ):
        """
        Busca um município pelo ID.
        """

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                id,
                nome
            FROM municipio
            WHERE id = ?
        """, (
            municipio_id,
        ))

        registro = cursor.fetchone()

        conexao.close()

        if registro is None:
            return None

        return Municipio(
            id=registro["id"],
            nome=registro["nome"]
        )

    @staticmethod
    def listar_perguntas():
        """
        Retorna todas as perguntas
        do Checklist Ambiental
        na ordem numérica.
        """

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                id,
                numero,
                texto
            FROM pergunta_checklist
            ORDER BY numero ASC
        """)

        registros = cursor.fetchall()

        conexao.close()

        perguntas = []

        for registro in registros:

            pergunta = PerguntaChecklist(
                id=registro["id"],
                numero=registro["numero"],
                texto=registro["texto"]
            )

            perguntas.append(
                pergunta
            )

        return perguntas

    @staticmethod
    def listar_respostas_por_municipio(
        municipio_id
    ):
        """
        Retorna todas as respostas
        de um município.
        """

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                id,
                municipio_id,
                pergunta_id,
                resposta
            FROM resposta_checklist
            WHERE municipio_id = ?
            ORDER BY pergunta_id ASC
        """, (
            municipio_id,
        ))

        registros = cursor.fetchall()

        conexao.close()

        respostas = []

        for registro in registros:

            resposta = RespostaChecklist(
                id=registro["id"],
                municipio_id=registro["municipio_id"],
                pergunta_id=registro["pergunta_id"],
                resposta=registro["resposta"]
            )

            respostas.append(
                resposta
            )

        return respostas

    @staticmethod
    def listar_checklist_por_municipio(
        municipio_id
    ):
        """
        Retorna perguntas e respostas
        de um município em uma única consulta.

        Mesmo que ainda não exista resposta
        para uma pergunta, ela continuará
        aparecendo no resultado.
        """

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                p.id AS pergunta_id,
                p.numero AS numero,
                p.texto AS pergunta,
                r.id AS resposta_id,
                r.resposta AS resposta
            FROM pergunta_checklist p

            LEFT JOIN resposta_checklist r
                ON r.pergunta_id = p.id
                AND r.municipio_id = ?

            ORDER BY p.numero ASC
        """, (
            municipio_id,
        ))

        registros = cursor.fetchall()

        conexao.close()

        checklist = []

        for registro in registros:

            checklist.append({
                "pergunta_id":
                    registro["pergunta_id"],

                "numero":
                    registro["numero"],

                "pergunta":
                    registro["pergunta"],

                "resposta_id":
                    registro["resposta_id"],

                "resposta":
                    registro["resposta"]
            })

        return checklist