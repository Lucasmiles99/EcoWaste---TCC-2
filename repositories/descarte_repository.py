from database.connection import conectar
from models.descarte import Descarte

class DescarteRepository:

    def salvar(self, descarte):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO descarte (
                empresa_id,
                equipamento_id,
                ecoponto_id,
                quantidade,
                data_descarte,
                status,
                observacao
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            descarte.empresa_id,
            descarte.equipamento_id,
            descarte.ecoponto_id,
            descarte.quantidade,
            descarte.data_descarte,
            descarte.status,
            descarte.observacao
        ))

        conexao.commit()

        descarte.id = cursor.lastrowid

        conexao.close()

        return descarte

    def listar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                id,
                empresa_id,
                equipamento_id,
                ecoponto_id,
                quantidade,
                data_descarte,
                status,
                observacao
            FROM descarte
            ORDER BY id DESC
        """)

        registros = cursor.fetchall()

        descartes = []

        for registro in registros:
            descarte = Descarte(
                id=registro["id"],
                empresa_id=registro["empresa_id"],
                equipamento_id=registro["equipamento_id"],
                ecoponto_id=registro["ecoponto_id"],
                quantidade=registro["quantidade"],
                data_descarte=registro["data_descarte"],
                status=registro["status"],
                observacao=registro["observacao"]
            )

            descartes.append(descarte)

        conexao.close()

        return descartes

    def listar_com_detalhes(self):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                descarte.id,
                descarte.empresa_id,
                empresa.nome AS empresa_nome,

                descarte.equipamento_id,
                equipamento.nome AS equipamento_nome,

                descarte.ecoponto_id,
                ecoponto.nome AS ecoponto_nome,

                descarte.quantidade,
                descarte.data_descarte,
                descarte.status,
                descarte.observacao

            FROM descarte

            INNER JOIN empresa
                ON empresa.id = descarte.empresa_id

            INNER JOIN equipamento
                ON equipamento.id = descarte.equipamento_id

            LEFT JOIN ecoponto
                ON ecoponto.id = descarte.ecoponto_id

            ORDER BY descarte.id DESC
        """)

        registros = cursor.fetchall()

        descartes = []

        for registro in registros:

            descartes.append({
                "id": registro["id"],

                "empresa_id": registro["empresa_id"],
                "empresa_nome": registro["empresa_nome"],

                "equipamento_id": registro["equipamento_id"],
                "equipamento_nome": registro["equipamento_nome"],

                "ecoponto_id": registro["ecoponto_id"],
                "ecoponto_nome": registro["ecoponto_nome"],

                "quantidade": registro["quantidade"],
                "data_descarte": registro["data_descarte"],
                "status": registro["status"],
                "observacao": registro["observacao"]
            })

        conexao.close()

        return descartes

    def buscar_por_id(self, id):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                id,
                empresa_id,
                equipamento_id,
                ecoponto_id,
                quantidade,
                data_descarte,
                status,
                observacao
            FROM descarte
            WHERE id = ?
        """, (id,))

        registro = cursor.fetchone()

        conexao.close()

        if registro is None:
            return None

        return Descarte(
            id=registro["id"],
            empresa_id=registro["empresa_id"],
            equipamento_id=registro["equipamento_id"],
            ecoponto_id=registro["ecoponto_id"],
            quantidade=registro["quantidade"],
            data_descarte=registro["data_descarte"],
            status=registro["status"],
            observacao=registro["observacao"]
        )

    def atualizar(self, descarte):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE descarte
            SET
                empresa_id = ?,
                equipamento_id = ?,
                ecoponto_id = ?,
                quantidade = ?,
                data_descarte = ?,
                status = ?,
                observacao = ?
            WHERE id = ?
        """, (
            descarte.empresa_id,
            descarte.equipamento_id,
            descarte.ecoponto_id,
            descarte.quantidade,
            descarte.data_descarte,
            descarte.status,
            descarte.observacao,
            descarte.id
        ))

        conexao.commit()
        conexao.close()

        return descarte

    def excluir(self, id):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            DELETE FROM descarte
            WHERE id = ?
        """, (id,))

        conexao.commit()

        quantidade_excluida = cursor.rowcount

        conexao.close()

        return quantidade_excluida > 0