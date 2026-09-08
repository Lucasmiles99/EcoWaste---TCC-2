from services.checklist_service import (
    ChecklistService
)

print(
    "\n=== MUNICÍPIOS ==="
)

municipios = (
    ChecklistService
    .listar_municipios()
)

for municipio in municipios:

    print(
        municipio.id,
        "-",
        municipio.nome
    )

print(
    "\n=== CHECKLIST ==="
)

if municipios:

    municipio = municipios[0]

    resultado = (
        ChecklistService
        .obter_checklist_municipio(
            municipio.id
        )
    )

    print(
        "Município:",
        resultado[
            "municipio"
        ].nome
    )

    print(
        "Total de perguntas:",
        resultado[
            "total_perguntas"
        ]
    )

    print(
        "Total respondidas:",
        resultado[
            "total_respondidas"
        ]
    )

    print(
        "Percentual respondido:",
        resultado[
            "percentual"
        ],
        "%"
    )