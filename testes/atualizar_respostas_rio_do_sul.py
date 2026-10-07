from database.connection import conectar

RESPOSTAS_RIO_DO_SUL = {
    1: (
        "Sim, A Prefeitura possui um departamento responsável pela gestão "
        "de resíduos sólidos. O responsável técnico informado é o engenheiro "
        "sanitarista Emerson Souza."
    ),

    2: (
        "Sim, Segundo o entrevistado, o plano foi atualizado no ano "
        "anterior à entrevista."
    ),

    3: (
        "Sim, Foi informado que existe acompanhamento do plano na prática."
    ),

    4: (
        "Não, Foi informado que não há fiscalização ostensiva regular "
        "sobre o descarte de resíduos."
    ),

    5: (
        "Os resíduos recicláveis são destinados a organizações de "
        "catadores/reciclagem. Foram mencionadas Barra do Trombudo, "
        "ASCARBAT, Associação Recicla Rio do Sul e Reciclagem do Wilson."
    ),

    6: (
        "Foram mencionados como referências a Política Nacional de "
        "Resíduos Sólidos e o Plano Municipal de Resíduos Sólidos."
    ),

    7: (
        "A Ouvidoria disponível no site da Prefeitura pode receber "
        "denúncias relacionadas ao descarte irregular. Segundo o "
        "entrevistado, esse tipo de denúncia ocorre raramente."
    ),

    8: (
        "Não, Essa exigência está relacionada às empresas sujeitas "
        "ao licenciamento ambiental."
    ),

    9: (
        "Foram mencionados o Decreto nº 9.399/2020, especialmente os "
        "artigos 61 e 62, e o Decreto Federal nº 6.514/2008."
    ),

    10: (
        "Não, Foi informado que não existe incentivo fiscal direto "
        "dessa natureza."
    ),

    11: (
        "Segundo o entrevistado, empresas privadas, incluindo empresas "
        "do setor de TIC, encaminham seus resíduos eletrônicos para "
        "empresas especializadas do setor privado, podendo possuir "
        "contratos próprios para essa destinação."
    ),

    12: (
        "Sim, Foi informado que o descarte inadequado ou irregular "
        "ainda ocorre com frequência no município."
    ),

    13: (
        "Foram mencionados rádios, telas de computador, televisores, "
        "liquidificadores e impressoras. Os equipamentos de maior porte "
        "são encaminhados diretamente às organizações responsáveis pela "
        "reciclagem/coleta."
    ),

    14: (
        "Sim. Foram relatados registros em áreas de maior poder aquisitivo. "
        "Nessas regiões, a coleta ocorre pelo menos duas vezes por semana."
    ),

    15: (
        "Não foi relatado registro recente de aplicação de multa "
        "por esse motivo."
    ),

    16: (
        "Não, O município não possui programa próprio exclusivo para "
        "a coleta de resíduos eletrônicos corporativos."
    ),

    17: (
        "Sim, Foi mencionado o programa Penso, Logo Destino (PLD). "
        "Foram citados pontos/localidades na Rua 15 de Novembro, Centro, "
        "Progresso, Canta Galo, Laranjeiras e Avenida Aristiliano Ramos. "
        "Também foram mencionados supermercados como locais de recebimento "
        "de pilhas e baterias, além de ciclos específicos para lâmpadas "
        "e a sede do IMA no bairro Eugênio Schneider."
    ),

    18: (
        "Sim, Os resíduos de maior porte exigem atenção e logística "
        "diferenciadas."
    ),

    19: (
        "Não, Foi informado que não existe taxa específica para "
        "essa finalidade."
    ),

    20: (
        "Ainda não, Foi informada previsão de implantação de Pontos de "
        "Entrega Voluntária (PEVs), incluindo pontos para resíduos "
        "eletrônicos no Parque do Farol e no Parque Ermembergo Pellizzetti, "
        "dentro do planejamento da concessão."
    ),

    21: (
        "Sim, Foi mencionado o Consórcio Riosulense e um planejamento "
        "iniciado em 2025 que prevê a implantação de PEVs ao longo do "
        "período da concessão, informado como sendo de 30 anos."
    ),

    22: (
        "Não, Foi informado que as taxas e os procedimentos não são "
        "uniformes em todos os bairros e setores."
    ),

    23: (
        "Sim, Além do engenheiro sanitarista responsável pela gestão de "
        "resíduos sólidos, foi mencionado Ricardo Payter como outro "
        "profissional que atua diretamente no departamento."
    ),

    24: (
        "Segundo o entrevistado, atualmente o desconhecimento não é "
        "considerado uma das principais causas, pois existe maior facilidade "
        "de acesso às informações e aos meios de destinação."
    ),

    25: (
        "Sim, Foi percebido aumento do empenho das empresas na "
        "gestão ambiental."
    ),

    26: (
        "O principal gargalo apontado está relacionado à infraestrutura "
        "de coleta e armazenamento, especialmente no tratamento de "
        "resíduos volumosos."
    ),

    27: (
        "O principal obstáculo apontado é financeiro."
    ),

    28: (
        "O volume recebido é proveniente principalmente de lojas, "
        "residências e do comércio em geral."
    ),

    29: (
        "Não, Foi informado que não são realizadas campanhas publicitárias "
        "pagas de forma contínua especificamente sobre o descarte de "
        "resíduos eletrônicos."
    ),

    30: (
        "Sim, Foi demonstrado interesse na adoção de novas tecnologias "
        "para controle e mapeamento do descarte."
    ),

    31: (
        "Foram discutidas possibilidades de benefícios associados à "
        "melhoria da infraestrutura e ao descarte adequado. Como referência, "
        "foi mencionada uma iniciativa de São Bento do Sul envolvendo "
        "créditos relacionados ao descarte correto de resíduos eletrônicos. "
        "Segundo o entrevistado, houve tentativa de trazer iniciativa "
        "semelhante para Rio do Sul, mas não houve interesse da instituição "
        "bancária envolvida. Também foram mencionados Retorna Machine, "
        "a Usina Salto Pilão/consórcio empresarial e tentativa de "
        "articulação com a UNIDAVI para 2026."
    ),

    32: (
        "Sim, Segundo o entrevistado, uma gestão mais eficiente pode "
        "beneficiar as associações de catadores, favorecer a economia "
        "circular e gerar impactos econômicos positivos gerando royalties."
    ),

    33: (
        "Sim, Foram mencionadas diversas parcerias com a UNIDAVI, embora "
        "tenha sido relatada dificuldade relacionada ao retorno de contatos. "
        "O projeto “Meu Rio, Nosso Rio” foi citado como exemplo de iniciativa "
        "com participação da instituição."
    ),

    34: (
        "O entrevistado considera esses trabalhos importantes por "
        "possibilitarem a apresentação de ideias e soluções inovadoras. "
        "Também avaliou que o projeto desenvolvido neste TCC pode gerar "
        "contribuição relevante para a região."
    ),

    35: (
        "A orientação é melhorar a separação e a gestão interna dos resíduos, "
        "garantindo sua destinação correta. Foi relatado que a mistura de "
        "materiais recicláveis com resíduos contaminados de Classe I pode "
        "elevar significativamente os custos de destinação."
    ),

    36: (
        "A estrutura atual foi avaliada como adequada."
    ),

    37: (
        "Não foi indicada restrição formal para essa iniciativa."
    ),

    38: (
        "Sim, Foi demonstrado interesse na possibilidade de utilização "
        "do projeto como plano piloto após a conclusão do TCC."
    ),

    39: (
        "Sim, Foi manifestado apoio à continuidade da coleta de dados "
        "e à expansão do estudo."
    ),

    40: (
        "As informações podem ser consultadas no site oficial do Município "
        "de Rio do Sul, na página referente à coleta de lixo orgânico e "
        "reciclável. "
        "(riodosul.atende.net/cidadão/pagina/"
        "coleta-de-lixo-organico-e-reciclavel)"
    )
}

def atualizar_respostas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id
        FROM municipio
        WHERE nome = ?
    """, (
        "Rio do Sul",
    ))

    municipio = cursor.fetchone()

    if municipio is None:
        conexao.close()

        print(
            "ERRO: município Rio do Sul "
            "não foi encontrado."
        )

        return

    municipio_id = municipio["id"]

    atualizadas = 0
    inseridas = 0
    erros = 0

    for numero, resposta in RESPOSTAS_RIO_DO_SUL.items():

        cursor.execute("""
            SELECT
                id
            FROM pergunta_checklist
            WHERE numero = ?
        """, (
            numero,
        ))

        pergunta = cursor.fetchone()

        if pergunta is None:

            print(
                f"ERRO: pergunta {numero} "
                f"não encontrada."
            )

            erros += 1

            continue

        pergunta_id = pergunta["id"]

        cursor.execute("""
            SELECT
                id
            FROM resposta_checklist
            WHERE municipio_id = ?
              AND pergunta_id = ?
        """, (
            municipio_id,
            pergunta_id
        ))

        resposta_existente = cursor.fetchone()

        if resposta_existente is not None:

            cursor.execute("""
                UPDATE resposta_checklist
                SET resposta = ?
                WHERE id = ?
            """, (
                resposta,
                resposta_existente["id"]
            ))

            atualizadas += 1

            print(
                f"Pergunta {numero:02d}: "
                f"resposta atualizada."
            )

        else:

            cursor.execute("""
                INSERT INTO resposta_checklist (
                    municipio_id,
                    pergunta_id,
                    resposta
                )
                VALUES (
                    ?,
                    ?,
                    ?
                )
            """, (
                municipio_id,
                pergunta_id,
                resposta
            ))

            inseridas += 1

            print(
                f"Pergunta {numero:02d}: "
                f"resposta inserida."
            )

    conexao.commit()
    conexao.close()

    print()
    print(
        "=== ATUALIZAÇÃO CONCLUÍDA ==="
    )

    print(
        f"Respostas atualizadas: {atualizadas}"
    )

    print(
        f"Respostas inseridas: {inseridas}"
    )

    print(
        f"Erros encontrados: {erros}"
    )

    print(
        f"Total esperado: {len(RESPOSTAS_RIO_DO_SUL)}"
    )

if __name__ == "__main__":
    atualizar_respostas()