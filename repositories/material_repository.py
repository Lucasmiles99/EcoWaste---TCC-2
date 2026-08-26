from database.connection import conectar
from models.material import Material

class MaterialRepository:

    def salvar(self, material):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO material (
                nome,
                categoria,
                descricao
            )
            VALUES (?, ?, ?)
        """, (
            material.nome,
            material.categoria,
            material.descricao
        ))

        conexao.commit()

        material.id = cursor.lastrowid

        conexao.close()

        return material

    def listar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                id,
                nome,
                categoria,
                descricao
            FROM material
            ORDER BY id DESC
        """)

        registros = cursor.fetchall()

        materiais = []

        for registro in registros:
            material = Material(
                id=registro["id"],
                nome=registro["nome"],
                categoria=registro["categoria"],
                descricao=registro["descricao"]
            )

            materiais.append(material)

        conexao.close()

        return materiais

    def buscar_por_id(self, id):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                id,
                nome,
                categoria,
                descricao
            FROM material
            WHERE id = ?
        """, (id,))

        registro = cursor.fetchone()

        conexao.close()

        if registro is None:
            return None

        return Material(
            id=registro["id"],
            nome=registro["nome"],
            categoria=registro["categoria"],
            descricao=registro["descricao"]
        )

    def atualizar(self, material):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE material
            SET
                nome = ?,
                categoria = ?,
                descricao = ?
            WHERE id = ?
        """, (
            material.nome,
            material.categoria,
            material.descricao,
            material.id
        ))

        conexao.commit()
        conexao.close()

        return material

    def excluir(self, id):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            DELETE FROM material
            WHERE id = ?
        """, (id,))

        conexao.commit()

        quantidade_excluida = cursor.rowcount

        conexao.close()

        return quantidade_excluida > 0