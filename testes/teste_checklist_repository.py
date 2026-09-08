from repositories.checklist_repository import (
    ChecklistRepository
)

print(
    "\n=== MUNICÍPIOS ==="
)

municipios = (
    ChecklistRepository
    .listar_municipios()
)

for municipio in municipios:

    print(
        municipio.id,
        "-",
        municipio.nome
    )

print(
    "\n=== PERGUNTAS ==="
)

perguntas = (
    ChecklistRepository
    .listar_perguntas()
)

print(
    "Total de perguntas:",
    len(perguntas)
)

print(
    "\n=== CHECKLIST DE RIO DO SUL ==="
)

if municipios:

    municipio = municipios[0]

    checklist = (
        ChecklistRepository
        .listar_checklist_por_municipio(
            municipio.id
        )
    )

    print(
        "Município:",
        municipio.nome
    )

    print(
        "Total de itens:",
        len(checklist)
    )

    for item in checklist:

        print(
            f"\n{item['numero']}. "
            f"{item['pergunta']}"
        )

        print(
            "Resposta:",
            item["resposta"]
        )