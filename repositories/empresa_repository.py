from database.connection import conectar
from models.empresa import Empresa

class EmpresaRepository:

    def salvar(self, empresa):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO empresa (
                nome,
                cidade,
                segmento,
                contato
            )
            VALUES (?, ?, ?, ?)
        """, (
            empresa.nome,
            empresa.cidade,
            empresa.segmento,
            empresa.contato
        ))

        conexao.commit()

        empresa.id = cursor.lastrowid

        conexao.close()

        return empresa

    def listar(self):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                id,
                nome,
                cidade,
                segmento,
                contato
            FROM empresa
            ORDER BY id DESC
        """)

        registros = cursor.fetchall()

        empresas = []

        for registro in registros:
            empresa = Empresa(
                id=registro["id"],
                nome=registro["nome"],
                cidade=registro["cidade"],
                segmento=registro["segmento"],
                contato=registro["contato"]
            )

            empresas.append(empresa)

        conexao.close()

        return empresas

    def buscar_por_id(self, id):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                id,
                nome,
                cidade,
                segmento,
                contato
            FROM empresa
            WHERE id = ?
        """, (id,))

        registro = cursor.fetchone()

        conexao.close()

        if registro is None:
            return None

        return Empresa(
            id=registro["id"],
            nome=registro["nome"],
            cidade=registro["cidade"],
            segmento=registro["segmento"],
            contato=registro["contato"]
        )

    def atualizar(self, empresa):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE empresa
            SET
                nome = ?,
                cidade = ?,
                segmento = ?,
                contato = ?
            WHERE id = ?
        """, (
            empresa.nome,
            empresa.cidade,
            empresa.segmento,
            empresa.contato,
            empresa.id
        ))

        conexao.commit()
        conexao.close()

        return empresa

    def excluir(self, id):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            DELETE FROM empresa
            WHERE id = ?
        """, (id,))

        conexao.commit()

        quantidade_excluida = cursor.rowcount

        conexao.close()

        return quantidade_excluida > 0