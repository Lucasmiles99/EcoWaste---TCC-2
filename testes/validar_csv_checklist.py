import csv
import os

def validar_existencia_csv():
    caminho_arquivo = os.path.join("dados", "checklist_ambiental.csv")

    print("=== VALIDAÇÃO DO CSV DO CHECKLIST AMBIENTAL ===")
    print()

    if os.path.exists(caminho_arquivo):
        print("Arquivo CSV encontrado com sucesso.")
        print(f"Caminho: {caminho_arquivo}")
        return caminho_arquivo

    print("ERRO: Arquivo CSV não encontrado.")
    print(f"Caminho esperado: {caminho_arquivo}")
    return None

def validar_colunas_csv(caminho_arquivo):
    colunas_esperadas = [
        "municipio",
        "numero_pergunta",
        "pergunta",
        "resposta"
    ]

    with open(caminho_arquivo, "r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.reader(arquivo, delimiter=";")
        cabecalho = next(leitor, None)

    print()
    print("=== VALIDAÇÃO DAS COLUNAS ===")

    if cabecalho == colunas_esperadas:
        print("Colunas do CSV estão corretas.")
        print(f"Colunas encontradas: {cabecalho}")
        return True

    print("ERRO: As colunas do CSV não estão no formato esperado.")
    print(f"Esperado: {colunas_esperadas}")
    print(f"Encontrado: {cabecalho}")
    return False

def validar_quantidade_rio_do_sul(caminho_arquivo):
    quantidade = 0

    with open(caminho_arquivo, "r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")

        for linha in leitor:
            if linha["municipio"].strip() == "Rio do Sul":
                quantidade += 1

    print()
    print("=== VALIDAÇÃO DE RIO DO SUL ===")
    print(f"Linhas encontradas para Rio do Sul: {quantidade}")

    if quantidade == 40:
        print("Quantidade de perguntas de Rio do Sul está correta.")
        return True

    print("ERRO: Rio do Sul deveria possuir exatamente 40 perguntas.")
    return False

def validar_respostas_rio_do_sul(caminho_arquivo):
    respostas_preenchidas = 0
    respostas_vazias = 0

    with open(caminho_arquivo, "r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")

        for linha in leitor:
            if linha["municipio"].strip() == "Rio do Sul":
                resposta = linha["resposta"]

                if resposta is not None and resposta.strip() != "":
                    respostas_preenchidas += 1
                else:
                    respostas_vazias += 1

    print()
    print("=== VALIDAÇÃO DAS RESPOSTAS DE RIO DO SUL ===")
    print(f"Respostas preenchidas: {respostas_preenchidas}")
    print(f"Respostas vazias: {respostas_vazias}")

    if respostas_preenchidas == 40 and respostas_vazias == 0:
        print("Todas as 40 respostas de Rio do Sul estão preenchidas.")
        return True

    print("ERRO: Existem respostas ausentes em Rio do Sul.")
    return False

def validar_numeracao_rio_do_sul(caminho_arquivo):
    numeros_encontrados = []

    with open(caminho_arquivo, "r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")

        for linha in leitor:
            if linha["municipio"].strip() == "Rio do Sul":
                numero = linha["numero_pergunta"].strip()

                if numero.isdigit():
                    numeros_encontrados.append(int(numero))

    numeros_encontrados.sort()
    numeros_esperados = list(range(1, 41))

    print()
    print("=== VALIDAÇÃO DA NUMERAÇÃO DE RIO DO SUL ===")
    print(f"Numeração encontrada: {numeros_encontrados}")

    if numeros_encontrados == numeros_esperados:
        print("Numeração das perguntas está correta: 1 até 40.")
        return True

    print("ERRO: A numeração das perguntas de Rio do Sul está incorreta.")
    return False

def validar_perguntas_duplicadas_rio_do_sul(caminho_arquivo):
    perguntas = []
    perguntas_duplicadas = []

    with open(caminho_arquivo, "r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")

        for linha in leitor:
            if linha["municipio"].strip() == "Rio do Sul":
                pergunta = linha["pergunta"].strip()

                if pergunta in perguntas and pergunta not in perguntas_duplicadas:
                    perguntas_duplicadas.append(pergunta)

                perguntas.append(pergunta)

    print()
    print("=== VALIDAÇÃO DE PERGUNTAS DUPLICADAS ===")

    if not perguntas_duplicadas:
        print("Nenhuma pergunta duplicada encontrada em Rio do Sul.")
        return True

    print("ERRO: Foram encontradas perguntas duplicadas em Rio do Sul.")
    return False

def validar_quantidade_municipios(caminho_arquivo):
    municipios = set()

    with open(caminho_arquivo, "r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")

        for linha in leitor:
            municipio = linha["municipio"].strip()

            if municipio:
                municipios.add(municipio)

    municipios_ordenados = sorted(municipios)

    print()
    print("=== VALIDAÇÃO DOS MUNICÍPIOS ===")
    print(f"Quantidade de municípios encontrados: {len(municipios_ordenados)}")

    if len(municipios_ordenados) == 28:
        print("Quantidade de municípios está correta: 28.")
        return True

    print("ERRO: A quantidade de municípios deveria ser 28.")
    return False

def validar_40_perguntas_por_municipio(caminho_arquivo):
    contagem_municipios = {}

    with open(caminho_arquivo, "r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")

        for linha in leitor:
            municipio = linha["municipio"].strip()

            if municipio not in contagem_municipios:
                contagem_municipios[municipio] = 0

            contagem_municipios[municipio] += 1

    print()
    print("=== VALIDAÇÃO DE 40 PERGUNTAS POR MUNICÍPIO ===")

    municipios_com_erro = []

    for municipio in sorted(contagem_municipios):
        quantidade = contagem_municipios[municipio]

        if quantidade != 40:
            municipios_com_erro.append(municipio)

    if not municipios_com_erro:
        print("Todos os 28 municípios possuem exatamente 40 perguntas.")
        return True

    print("ERRO: Alguns municípios não possuem exatamente 40 perguntas.")
    return False

def validar_total_registros(caminho_arquivo):
    total_registros = 0

    with open(caminho_arquivo, "r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")

        for _ in leitor:
            total_registros += 1

    total_esperado = 28 * 40

    print()
    print("=== VALIDAÇÃO DO TOTAL DE REGISTROS ===")
    print(f"Registros encontrados: {total_registros}")
    print(f"Registros esperados: {total_esperado}")

    if total_registros == total_esperado:
        print("Total de registros está correto: 1120.")
        return True

    print("ERRO: O CSV não possui os 1120 registros esperados.")
    return False

def validar_situacao_respostas(caminho_arquivo):
    rio_preenchidas = 0
    rio_vazias = 0
    outros_preenchidas = 0
    outros_vazias = 0

    with open(caminho_arquivo, "r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")

        for linha in leitor:
            municipio = linha["municipio"].strip()
            resposta = linha["resposta"]

            resposta_preenchida = (
                resposta is not None
                and resposta.strip() != ""
            )

            if municipio == "Rio do Sul":
                if resposta_preenchida:
                    rio_preenchidas += 1
                else:
                    rio_vazias += 1
            else:
                if resposta_preenchida:
                    outros_preenchidas += 1
                else:
                    outros_vazias += 1

    print()
    print("=== VALIDAÇÃO DA SITUAÇÃO DAS RESPOSTAS ===")
    print(f"Rio do Sul - preenchidas: {rio_preenchidas}")
    print(f"Rio do Sul - vazias: {rio_vazias}")
    print(f"Demais municípios - preenchidas: {outros_preenchidas}")
    print(f"Demais municípios - vazias: {outros_vazias}")

    if (
        rio_preenchidas == 40
        and rio_vazias == 0
        and outros_preenchidas == 0
        and outros_vazias == 1080
    ):
        print("Situação das respostas está correta.")
        return True

    print("ATENÇÃO: A situação das respostas está diferente do esperado.")
    return False

def validar_padronizacao_respostas(caminho_arquivo):
    respostas_nao_nao_padronizadas = []
    respostas_completas_com_nao = 0
    respostas_completas_com_sim = 0
    respostas_padronizadas_nao = 0

    formas_nao_incorretas = {
        "NAO",
        "NÃO",
        "nao",
        "não",
        "Nao",
        "Não".upper()
    }

    with open(caminho_arquivo, "r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo, delimiter=";")

        for linha in leitor:
            resposta = linha["resposta"]

            if resposta is None:
                continue

            resposta = resposta.strip()

            if resposta == "":
                continue

            if resposta == "Não":
                respostas_padronizadas_nao += 1
                continue

            if resposta.upper() in formas_nao_incorretas:
                respostas_nao_nao_padronizadas.append(
                    {
                        "municipio": linha["municipio"],
                        "numero_pergunta": linha["numero_pergunta"],
                        "resposta": resposta
                    }
                )

            if resposta.lower().startswith("não,") or resposta.lower().startswith("nao,"):
                respostas_completas_com_nao += 1

            if resposta.lower().startswith("sim,"):
                respostas_completas_com_sim += 1

    print()
    print("=== VALIDAÇÃO DA PADRONIZAÇÃO DAS RESPOSTAS ===")
    print(f'Respostas exatamente "Não": {respostas_padronizadas_nao}')
    print(
        f"Respostas completas iniciadas com Não: "
        f"{respostas_completas_com_nao}"
    )
    print(
        f"Respostas completas iniciadas com Sim: "
        f"{respostas_completas_com_sim}"
    )

    if not respostas_nao_nao_padronizadas:
        print("Nenhuma resposta isolada fora do padrão foi encontrada.")
        print('Respostas isoladas "NAO"/"NÃO" estão padronizadas como "Não".')
        print("Respostas completas foram preservadas.")
        return True

    print("ERRO: Foram encontradas respostas isoladas fora do padrão.")

    for item in respostas_nao_nao_padronizadas:
        print(
            f'{item["municipio"]} - pergunta '
            f'{item["numero_pergunta"]}: {item["resposta"]}'
        )

    return False

if __name__ == "__main__":
    caminho = validar_existencia_csv()

    if caminho is not None:
        colunas_validas = validar_colunas_csv(caminho)

        if colunas_validas:
            quantidade_valida = validar_quantidade_rio_do_sul(caminho)

            if quantidade_valida:
                respostas_validas = validar_respostas_rio_do_sul(caminho)

                if respostas_validas:
                    numeracao_valida = validar_numeracao_rio_do_sul(caminho)

                    if numeracao_valida:
                        duplicadas_validas = validar_perguntas_duplicadas_rio_do_sul(
                            caminho
                        )

                        if duplicadas_validas:
                            municipios_validos = validar_quantidade_municipios(
                                caminho
                            )

                            if municipios_validos:
                                perguntas_validas = validar_40_perguntas_por_municipio(
                                    caminho
                                )

                                if perguntas_validas:
                                    total_valido = validar_total_registros(
                                        caminho
                                    )

                                    if total_valido:
                                        respostas_validas = validar_situacao_respostas(
                                            caminho
                                        )

                                        if respostas_validas:
                                            validar_padronizacao_respostas(
                                                caminho
                                            )