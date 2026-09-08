import os
import re
import sys

RAIZ_PROJETO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

if RAIZ_PROJETO not in sys.path:
    sys.path.insert(
        0,
        RAIZ_PROJETO
    )

from database.connection import conectar

ARQUIVO_PERGUNTAS = os.path.join(
    RAIZ_PROJETO,
    "dados",
    "Perguntas do Checklist Ambiental.txt"
)

ARQUIVO_RESPOSTAS = os.path.join(
    RAIZ_PROJETO,
    "dados",
    "Checklist da Prefeitura de Rio do Sul.txt"
)

MUNICIPIO = "Rio do Sul"

def ler_itens(caminho):
    """
    Lê arquivos TXT numerados.

    Exemplos aceitos:

    1- texto
    2- texto

    ou:

    1. texto
    2. texto

    Pontos e hífens existentes dentro do texto
    não interferem mais na identificação do número.

    Retorna:

    {
        1: "texto",
        2: "texto"
    }
    """

    itens = {}

    with open(
        caminho,
        "r",
        encoding="utf-8"
    ) as arquivo:

        linhas = arquivo.readlines()

    for linha in linhas:

        linha = linha.strip()

        if not linha:
            continue

        correspondencia = re.match(
            r"^(\d+)\s*[\.-]\s*(.+)$",
            linha
        )

        if correspondencia:

            numero = int(
                correspondencia.group(1)
            )

            texto = (
                correspondencia
                .group(2)
                .strip()
            )

            itens[numero] = texto

    return itens

def cadastrar_municipio(
    cursor,
    nome
):

    cursor.execute("""
        INSERT OR IGNORE INTO municipio (
            nome
        )
        VALUES (?)
    """, (nome,))

    cursor.execute("""
        SELECT id
        FROM municipio
        WHERE nome = ?
    """, (nome,))

    registro = cursor.fetchone()

    return registro["id"]

def cadastrar_perguntas(
    cursor,
    perguntas
):

    for numero, texto in perguntas.items():

        cursor.execute("""
            SELECT id
            FROM pergunta_checklist
            WHERE numero = ?
        """, (numero,))

        registro = cursor.fetchone()

        if registro is None:

            cursor.execute("""
                INSERT INTO pergunta_checklist (
                    numero,
                    texto
                )
                VALUES (?, ?)
            """, (
                numero,
                texto
            ))

        else:

            cursor.execute("""
                UPDATE pergunta_checklist
                SET texto = ?
                WHERE numero = ?
            """, (
                texto,
                numero
            ))

def cadastrar_respostas(
    cursor,
    municipio_id,
    respostas
):

    for numero, resposta in respostas.items():

        cursor.execute("""
            SELECT id
            FROM pergunta_checklist
            WHERE numero = ?
        """, (numero,))

        pergunta = cursor.fetchone()

        if pergunta is None:

            print(
                f"Pergunta {numero} "
                "não encontrada."
            )

            continue

        pergunta_id = pergunta["id"]

        cursor.execute("""
            SELECT id
            FROM resposta_checklist
            WHERE municipio_id = ?
            AND pergunta_id = ?
        """, (
            municipio_id,
            pergunta_id
        ))

        registro = cursor.fetchone()

        if registro is None:

            cursor.execute("""
                INSERT INTO resposta_checklist (
                    municipio_id,
                    pergunta_id,
                    resposta
                )
                VALUES (?, ?, ?)
            """, (
                municipio_id,
                pergunta_id,
                resposta
            ))

        else:

            cursor.execute("""
                UPDATE resposta_checklist
                SET resposta = ?
                WHERE id = ?
            """, (
                resposta,
                registro["id"]
            ))

def importar_checklist():

    perguntas = ler_itens(
        ARQUIVO_PERGUNTAS
    )

    respostas = ler_itens(
        ARQUIVO_RESPOSTAS
    )

    print(
        f"Perguntas encontradas: "
        f"{len(perguntas)}"
    )

    print(
        f"Respostas encontradas: "
        f"{len(respostas)}"
    )

    if len(perguntas) != 40:

        print(
            "ERRO: eram esperadas "
            "40 perguntas."
        )

        print(
            "Importação cancelada."
        )

        return

    if len(respostas) != 40:

        print(
            "ERRO: eram esperadas "
            "40 respostas."
        )

        print(
            "Importação cancelada."
        )

        return

    conexao = conectar()
    cursor = conexao.cursor()

    municipio_id = cadastrar_municipio(
        cursor,
        MUNICIPIO
    )

    cadastrar_perguntas(
        cursor,
        perguntas
    )

    cadastrar_respostas(
        cursor,
        municipio_id,
        respostas
    )

    conexao.commit()
    conexao.close()

    print(
        "Checklist Ambiental de "
        f"{MUNICIPIO} importado "
        "com sucesso!"
    )

if __name__ == "__main__":
    importar_checklist()