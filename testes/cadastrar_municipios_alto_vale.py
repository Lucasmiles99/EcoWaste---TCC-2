from database.connection import conectar

MUNICIPIOS_ALTO_VALE = [
    "Agrolândia",
    "Agronômica",
    "Atalanta",
    "Aurora",
    "Braço do Trombudo",
    "Chapadão do Lageado",
    "Dona Emma",
    "Ibirama",
    "Imbuia",
    "Ituporanga",
    "José Boiteux",
    "Laurentino",
    "Lontras",
    "Mirim Doce",
    "Petrolândia",
    "Pouso Redondo",
    "Presidente Getúlio",
    "Presidente Nereu",
    "Rio do Campo",
    "Rio do Oeste",
    "Rio do Sul",
    "Salete",
    "Santa Terezinha",
    "Taió",
    "Trombudo Central",
    "Vidal Ramos",
    "Vitor Meireles",
    "Witmarsum"
]

def cadastrar_municipios():
    conexao = conectar()
    cursor = conexao.cursor()

    inseridos = 0
    existentes = 0

    for nome in MUNICIPIOS_ALTO_VALE:

        cursor.execute("""
            SELECT
                id
            FROM municipio
            WHERE nome = ?
        """, (
            nome,
        ))

        registro = cursor.fetchone()

        if registro is not None:

            existentes += 1

            print(
                f"Já cadastrado: {nome}"
            )

            continue

        cursor.execute("""
            INSERT INTO municipio (
                nome
            )
            VALUES (
                ?
            )
        """, (
            nome,
        ))

        inseridos += 1

        print(
            f"Cadastrado: {nome}"
        )

    conexao.commit()
    conexao.close()

    print()
    print(
        "=== RESULTADO ==="
    )

    print(
        f"Municípios inseridos: {inseridos}"
    )

    print(
        f"Municípios já existentes: {existentes}"
    )

    print(
        f"Total esperado no Alto Vale: "
        f"{len(MUNICIPIOS_ALTO_VALE)}"
    )

if __name__ == "__main__":

    cadastrar_municipios()