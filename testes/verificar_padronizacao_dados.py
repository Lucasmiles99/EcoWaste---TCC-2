from database.connection import conectar
from services.equipamento_service import EquipamentoService
from services.material_service import MaterialService

def verificar_equipamentos():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id,
            nome,
            categoria,
            marca,
            estado
        FROM equipamento
        ORDER BY id
    """)

    registros = cursor.fetchall()

    print()
    print("=" * 60)
    print("VERIFICAÇÃO DE EQUIPAMENTOS")
    print("=" * 60)

    inconsistencias = 0

    for registro in registros:

        problemas = []

        categoria = registro["categoria"] or ""
        marca = registro["marca"] or ""
        estado = registro["estado"] or ""

        if (
            categoria
            not in EquipamentoService.CATEGORIAS_PERMITIDAS
        ):
            problemas.append(
                f"categoria inválida: {categoria}"
            )

        if (
            marca
            not in EquipamentoService.MARCAS_PERMITIDAS
        ):
            problemas.append(
                f"marca inválida: {marca}"
            )

        if (
            estado
            not in EquipamentoService.ESTADOS_PERMITIDOS
        ):
            problemas.append(
                f"estado inválido: {estado}"
            )

        if problemas:

            inconsistencias += 1

            print()
            print(
                f"ID {registro['id']} - "
                f"{registro['nome']}"
            )

            for problema in problemas:
                print(
                    f"  -> {problema}"
                )

    if inconsistencias == 0:

        print()
        print(
            "Todos os equipamentos "
            "estão padronizados."
        )

    else:

        print()
        print(
            "Equipamentos com inconsistências:",
            inconsistencias
        )

    conexao.close()

def verificar_materiais():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id,
            nome,
            categoria
        FROM material
        ORDER BY id
    """)

    registros = cursor.fetchall()

    print()
    print("=" * 60)
    print("VERIFICAÇÃO DE MATERIAIS")
    print("=" * 60)

    inconsistencias = 0

    for registro in registros:

        problemas = []

        nome = registro["nome"] or ""
        categoria = registro["categoria"] or ""

        if (
            nome
            not in MaterialService.TIPOS_PERMITIDOS
        ):
            problemas.append(
                f"tipo inválido: {nome}"
            )

        if (
            categoria
            not in MaterialService.CATEGORIAS_PERMITIDAS
        ):
            problemas.append(
                f"categoria inválida: {categoria}"
            )

        if problemas:

            inconsistencias += 1

            print()
            print(
                f"ID {registro['id']} - "
                f"{registro['nome']}"
            )

            for problema in problemas:
                print(
                    f"  -> {problema}"
                )

    if inconsistencias == 0:

        print()
        print(
            "Todos os materiais "
            "estão padronizados."
        )

    else:

        print()
        print(
            "Materiais com inconsistências:",
            inconsistencias
        )

    conexao.close()

if __name__ == "__main__":

    verificar_equipamentos()

    verificar_materiais()

    print()
    print("=" * 60)
    print("VERIFICAÇÃO CONCLUÍDA")
    print("=" * 60)