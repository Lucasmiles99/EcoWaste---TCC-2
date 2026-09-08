from database.connection import conectar


class EcopontoMaterialRepository:

    def associar(self, ecoponto_id, material_id):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT OR IGNORE INTO ecoponto_material (
                ecoponto_id,
                material_id
            )
            VALUES (?, ?)
        """, (
            ecoponto_id,
            material_id
        ))

        conexao.commit()

        quantidade_inserida = cursor.rowcount

        conexao.close()

        return quantidade_inserida > 0

    def remover_associacao(
        self,
        ecoponto_id,
        material_id
    ):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            DELETE FROM ecoponto_material
            WHERE ecoponto_id = ?
            AND material_id = ?
        """, (
            ecoponto_id,
            material_id
        ))

        conexao.commit()

        quantidade_excluida = cursor.rowcount

        conexao.close()

        return quantidade_excluida > 0

    def remover_todas_associacoes(
        self,
        ecoponto_id
    ):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            DELETE FROM ecoponto_material
            WHERE ecoponto_id = ?
        """, (
            ecoponto_id,
        ))

        conexao.commit()

        quantidade_excluida = cursor.rowcount

        conexao.close()

        return quantidade_excluida

    def listar_materiais_do_ecoponto(
        self,
        ecoponto_id
    ):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                m.id,
                m.nome,
                m.categoria,
                m.imagem,
                m.descricao
            FROM material m
            INNER JOIN ecoponto_material em
                ON em.material_id = m.id
            WHERE em.ecoponto_id = ?
            ORDER BY m.nome
        """, (
            ecoponto_id,
        ))

        registros = cursor.fetchall()

        conexao.close()

        return registros

    def listar_ecopontos_do_material(
        self,
        material_id
    ):
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                e.id,
                e.nome,
                e.endereco,
                e.cidade,
                e.localizacao_maps,
                e.imagem,
                e.descricao
            FROM ecoponto e
            INNER JOIN ecoponto_material em
                ON em.ecoponto_id = e.id
            WHERE em.material_id = ?
            ORDER BY e.nome
        """, (
            material_id,
        ))

        registros = cursor.fetchall()

        conexao.close()

        return registros