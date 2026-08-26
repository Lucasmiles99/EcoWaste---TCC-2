from services.ecoponto_service import EcopontoService
from services.material_service import MaterialService
from services.ecoponto_material_service import (
    EcopontoMaterialService
)

ecoponto_service = EcopontoService()
material_service = MaterialService()
relacao_service = EcopontoMaterialService()

print(
    "\n===== TESTE ECOPONTO x MATERIAL ====="
)


# ==========================================================
# 1. CRIAR ECOPONTO
# ==========================================================

print("\n1 - Criando Ecoponto...")

ecoponto = ecoponto_service.cadastrar(
    nome="Ecoponto Municipal",
    endereco="Rua Teste, 100",
    cidade="Rio do Sul",
    descricao="Ecoponto utilizado no teste."
)

print(
    "Ecoponto criado:",
    ecoponto.id,
    "-",
    ecoponto.nome
)


# ==========================================================
# 2. CRIAR MATERIAIS
# ==========================================================

print("\n2 - Criando materiais...")

lampada = material_service.cadastrar(
    nome="Lâmpada",
    categoria="Resíduo eletrônico",
    descricao="Lâmpadas destinadas ao descarte adequado."
)

bateria = material_service.cadastrar(
    nome="Bateria",
    categoria="Resíduo eletrônico",
    descricao="Baterias de equipamentos eletrônicos."
)

print(
    "Material:",
    lampada.id,
    "-",
    lampada.nome
)

print(
    "Material:",
    bateria.id,
    "-",
    bateria.nome
)


# ==========================================================
# 3. ASSOCIAR
# ==========================================================

print("\n3 - Associando materiais ao Ecoponto...")

resultado1 = relacao_service.associar(
    ecoponto.id,
    lampada.id
)

resultado2 = relacao_service.associar(
    ecoponto.id,
    bateria.id
)

print(
    "Lâmpada associada:",
    resultado1
)

print(
    "Bateria associada:",
    resultado2
)


# ==========================================================
# 4. LISTAR MATERIAIS DO ECOPONTO
# ==========================================================

print(
    "\n4 - Materiais aceitos pelo Ecoponto..."
)

materiais = (
    relacao_service.listar_materiais_do_ecoponto(
        ecoponto.id
    )
)

for material in materiais:
    print(
        material["id"],
        "-",
        material["nome"]
    )


# ==========================================================
# 5. LISTAR ECOPONTOS QUE ACEITAM UM MATERIAL
# ==========================================================

print(
    "\n5 - Ecopontos que aceitam Lâmpada..."
)

ecopontos = (
    relacao_service.listar_ecopontos_do_material(
        lampada.id
    )
)

for item in ecopontos:
    print(
        item["id"],
        "-",
        item["nome"],
        "-",
        item["cidade"]
    )


# ==========================================================
# 6. REMOVER ASSOCIAÇÃO
# ==========================================================

print(
    "\n6 - Removendo associação da Lâmpada..."
)

resultado = relacao_service.remover_associacao(
    ecoponto.id,
    lampada.id
)

print(
    "Associação removida:",
    resultado
)


# ==========================================================
# 7. CONFIRMAR
# ==========================================================

print(
    "\n7 - Conferindo materiais restantes..."
)

materiais = (
    relacao_service.listar_materiais_do_ecoponto(
        ecoponto.id
    )
)

for material in materiais:
    print(
        material["id"],
        "-",
        material["nome"]
    )


# ==========================================================
# 8. LIMPEZA
# ==========================================================

print("\n8 - Limpando registros de teste...")

relacao_service.remover_associacao(
    ecoponto.id,
    bateria.id
)

material_service.excluir(
    lampada.id
)

material_service.excluir(
    bateria.id
)

ecoponto_service.excluir(
    ecoponto.id
)

print(
    "Registros de teste removidos."
)

print(
    "\n===== TESTE FINALIZADO ====="
)