from database.connection import conectar

def corrigir_equipamentos(
    cursor
):

    print()
    print("=" * 60)
    print("CORREÇÃO DE EQUIPAMENTOS")
    print("=" * 60)

    cursor.execute("""
        UPDATE equipamento
        SET categoria = ?
        WHERE id = ?
    """, (
        "TV Box",
        2
    ))

    print()
    print(
        "ID 2 - TV Box"
    )
    print(
        "Categoria corrigida:"
    )
    print(
        "Aparelho Eletronico"
        " -> "
        "TV Box"
    )

def corrigir_materiais(
    cursor
):

    print()
    print("=" * 60)
    print("CORREÇÃO DE MATERIAIS")
    print("=" * 60)

    cursor.execute("""
        UPDATE material
        SET
            nome = ?
        WHERE id = ?
    """, (
        "Lâmpada",
        6
    ))

    print()
    print(
        "ID 6 - Lampada"
    )
    print(
        "Tipo corrigido:"
    )
    print(
        "Lampada"
        " -> "
        "Lâmpada"
    )

    cursor.execute("""
        UPDATE material
        SET
            nome = ?,
            categoria = ?
        WHERE id = ?
    """, (
        "Pilha",
        "Baterias e Pilhas",
        7
    ))

    print()
    print(
        "ID 7 - Pilhas Alfacell"
    )
    print(
        "Tipo corrigido:"
    )
    print(
        "Pilhas Alfacell"
        " -> "
        "Pilha"
    )
    print(
        "Categoria corrigida:"
    )
    print(
        "Radiação"
        " -> "
        "Baterias e Pilhas"
    )

    cursor.execute("""
        UPDATE material
        SET
            nome = ?,
            categoria = ?
        WHERE id = ?
    """, (
        "Cabo",
        "Cabeamento",
        8
    ))

    print()
    print(
        "ID 8 - RJ-45"
    )
    print(
        "Tipo corrigido:"
    )
    print(
        "RJ-45"
        " -> "
        "Cabo"
    )
    print(
        "Categoria corrigida:"
    )
    print(
        "Cabo de Rede"
        " -> "
        "Cabeamento"
    )

def corrigir_padronizacao():

    conexao = conectar()

    cursor = conexao.cursor()

    try:

        corrigir_equipamentos(
            cursor
        )

        corrigir_materiais(
            cursor
        )

        conexao.commit()

        print()
        print("=" * 60)
        print(
            "CORREÇÕES SALVAS COM SUCESSO"
        )
        print("=" * 60)

    except Exception as erro:

        conexao.rollback()

        print()
        print("=" * 60)
        print(
            "ERRO DURANTE A CORREÇÃO"
        )
        print("=" * 60)

        print(
            str(erro)
        )

    finally:

        conexao.close()

if __name__ == "__main__":

    corrigir_padronizacao()