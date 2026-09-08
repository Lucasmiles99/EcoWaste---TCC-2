from database.connection import conectar
from models.ecoponto import Ecoponto

class EcopontoRepository:

    def salvar(self, ecoponto):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO ecoponto (
                nome,
                endereco,
                cidade,
                localizacao_maps,
                latitude,
                longitude,
                imagem,
                descricao
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            ecoponto.nome,
            ecoponto.endereco,
            ecoponto.cidade,
            ecoponto.localizacao_maps,
            ecoponto.latitude,
            ecoponto.longitude,
            ecoponto.imagem,
            ecoponto.descricao
        ))

        conexao.commit()

        ecoponto.id = cursor.lastrowid

        conexao.close()

        return ecoponto

    def listar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                id,
                nome,
                endereco,
                cidade,
                localizacao_maps,
                latitude,
                longitude,
                imagem,
                descricao
            FROM ecoponto
            ORDER BY id DESC
        """)

        registros = cursor.fetchall()

        ecopontos = []

        for registro in registros:
            ecoponto = Ecoponto(
                id=registro["id"],
                nome=registro["nome"],
                endereco=registro["endereco"],
                cidade=registro["cidade"],
                localizacao_maps=registro["localizacao_maps"],
                latitude=registro["latitude"],
                longitude=registro["longitude"],
                imagem=registro["imagem"],
                descricao=registro["descricao"]
            )

            ecopontos.append(ecoponto)

        conexao.close()

        return ecopontos

    def buscar_por_id(self, id):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                id,
                nome,
                endereco,
                cidade,
                localizacao_maps,
                latitude,
                longitude,
                imagem,
                descricao
            FROM ecoponto
            WHERE id = ?
        """, (id,))

        registro = cursor.fetchone()

        conexao.close()

        if registro is None:
            return None

        return Ecoponto(
            id=registro["id"],
            nome=registro["nome"],
            endereco=registro["endereco"],
            cidade=registro["cidade"],
            localizacao_maps=registro["localizacao_maps"],
            latitude=registro["latitude"],
            longitude=registro["longitude"],
            imagem=registro["imagem"],
            descricao=registro["descricao"]
        )

    def atualizar(self, ecoponto):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE ecoponto
            SET
                nome = ?,
                endereco = ?,
                cidade = ?,
                localizacao_maps = ?,
                latitude = ?,
                longitude = ?,
                imagem = ?,
                descricao = ?
            WHERE id = ?
        """, (
            ecoponto.nome,
            ecoponto.endereco,
            ecoponto.cidade,
            ecoponto.localizacao_maps,
            ecoponto.latitude,
            ecoponto.longitude,
            ecoponto.imagem,
            ecoponto.descricao,
            ecoponto.id
        ))

        conexao.commit()
        conexao.close()

        return ecoponto

    def excluir(self, id):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            DELETE FROM ecoponto
            WHERE id = ?
        """, (id,))

        conexao.commit()

        quantidade_excluida = cursor.rowcount

        conexao.close()

        return quantidade_excluida > 0