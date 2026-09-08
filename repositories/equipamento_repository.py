from database.connection import conectar
from models.equipamento import Equipamento


class EquipamentoRepository:

    def salvar(self, equipamento):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO equipamento (
                nome,
                categoria,
                marca,
                quantidade,
                estado,
                imagem,
                descricao
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            equipamento.nome,
            equipamento.categoria,
            equipamento.marca,
            equipamento.quantidade,
            equipamento.estado,
            equipamento.imagem,
            equipamento.descricao
        ))

        conexao.commit()

        equipamento.id = cursor.lastrowid

        conexao.close()

        return equipamento

    def listar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                id,
                nome,
                categoria,
                marca,
                quantidade,
                estado,
                imagem,
                descricao
            FROM equipamento
            ORDER BY id DESC
        """)

        registros = cursor.fetchall()

        equipamentos = []

        for registro in registros:
            equipamento = Equipamento(
                id=registro["id"],
                nome=registro["nome"],
                categoria=registro["categoria"],
                marca=registro["marca"],
                quantidade=registro["quantidade"],
                estado=registro["estado"],
                imagem=registro["imagem"],
                descricao=registro["descricao"]
            )

            equipamentos.append(equipamento)

        conexao.close()

        return equipamentos

    def buscar_por_id(self, id):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                id,
                nome,
                categoria,
                marca,
                quantidade,
                estado,
                imagem,
                descricao
            FROM equipamento
            WHERE id = ?
        """, (id,))

        registro = cursor.fetchone()

        conexao.close()

        if registro is None:
            return None

        return Equipamento(
            id=registro["id"],
            nome=registro["nome"],
            categoria=registro["categoria"],
            marca=registro["marca"],
            quantidade=registro["quantidade"],
            estado=registro["estado"],
            imagem=registro["imagem"],
            descricao=registro["descricao"]
        )

    def atualizar(self, equipamento):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE equipamento
            SET
                nome = ?,
                categoria = ?,
                marca = ?,
                quantidade = ?,
                estado = ?,
                imagem = ?,
                descricao = ?
            WHERE id = ?
        """, (
            equipamento.nome,
            equipamento.categoria,
            equipamento.marca,
            equipamento.quantidade,
            equipamento.estado,
            equipamento.imagem,
            equipamento.descricao,
            equipamento.id
        ))

        conexao.commit()
        conexao.close()

        return equipamento

    def excluir(self, id):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            DELETE FROM equipamento
            WHERE id = ?
        """, (id,))

        conexao.commit()

        quantidade_excluida = cursor.rowcount

        conexao.close()

        return quantidade_excluida > 0