from services.descarte_service import DescarteService
from services.empresa_service import EmpresaService
from services.equipamento_service import EquipamentoService
from services.ecoponto_service import EcopontoService


descarte_service = DescarteService()

empresa_service = EmpresaService()

equipamento_service = EquipamentoService()

ecoponto_service = EcopontoService()


print(
    "\n===== TESTANDO O SERVIÇO DE DESCARTES ====="
)


# ==========================================================
# 1. BUSCAR DADOS NECESSÁRIOS
# ==========================================================

print(
    "\n1 - Buscando empresa, equipamento e ecoponto..."
)

empresas = empresa_service.listar()

equipamentos = equipamento_service.listar()

ecopontos = ecoponto_service.listar()


if not empresas:

    print(
        "Nenhuma empresa cadastrada."
    )

    exit()


if not equipamentos:

    print(
        "Nenhum equipamento cadastrado."
    )

    exit()


empresa = empresas[0]

equipamento = equipamentos[0]

ecoponto = None


if ecopontos:

    ecoponto = ecopontos[0]


print(
    "Empresa:",
    empresa.nome
)

print(
    "Equipamento:",
    equipamento.nome
)


if ecoponto:

    print(
        "Ecoponto:",
        ecoponto.nome
    )

else:

    print(
        "Nenhum ecoponto disponível."
    )


# ==========================================================
# 2. CADASTRAR
# ==========================================================

print(
    "\n2 - Testando cadastro..."
)

descarte = descarte_service.cadastrar(
    empresa_id=empresa.id,
    equipamento_id=equipamento.id,
    ecoponto_id=(
        ecoponto.id
        if ecoponto
        else None
    ),
    quantidade=1,
    data_descarte="2026-09-11",
    status="Planejado",
    observacao=(
        "Teste automático de registro "
        "de descarte eletrônico."
    )
)


print(
    "Descarte cadastrado!"
)

print(
    "ID:",
    descarte.id
)

print(
    "Empresa ID:",
    descarte.empresa_id
)

print(
    "Equipamento ID:",
    descarte.equipamento_id
)

print(
    "Quantidade:",
    descarte.quantidade
)

print(
    "Status:",
    descarte.status
)


# ==========================================================
# 3. LISTAR
# ==========================================================

print(
    "\n3 - Testando listagem..."
)

descartes = (
    descarte_service
    .listar_com_detalhes()
)


for item in descartes:

    print(
        item["id"],
        "-",
        item["empresa_nome"],
        "-",
        item["equipamento_nome"],
        "-",
        item["quantidade"],
        "-",
        item["status"]
    )


# ==========================================================
# 4. BUSCAR POR ID
# ==========================================================

print(
    "\n4 - Testando busca..."
)

encontrado = (
    descarte_service
    .buscar_por_id(
        descarte.id
    )
)


print(
    "Descarte encontrado:",
    encontrado.id
)

print(
    "Status:",
    encontrado.status
)


# ==========================================================
# 5. ATUALIZAR
# ==========================================================

print(
    "\n5 - Testando atualização..."
)

atualizado = (
    descarte_service
    .atualizar(
        id=descarte.id,
        empresa_id=empresa.id,
        equipamento_id=equipamento.id,
        ecoponto_id=(
            ecoponto.id
            if ecoponto
            else None
        ),
        quantidade=2,
        data_descarte="2026-09-12",
        status="Realizado",
        observacao=(
            "Teste de descarte "
            "atualizado com sucesso."
        )
    )
)


print(
    "Quantidade atualizada:",
    atualizado.quantidade
)

print(
    "Status atualizado:",
    atualizado.status
)


# ==========================================================
# 6. VALIDAR QUANTIDADE INVÁLIDA
# ==========================================================

print(
    "\n6 - Testando quantidade inválida..."
)

try:

    descarte_service.cadastrar(
        empresa_id=empresa.id,
        equipamento_id=equipamento.id,
        quantidade=0
    )

except ValueError as erro:

    print(
        "Validação funcionando:",
        erro
    )


# ==========================================================
# 7. VALIDAR EMPRESA INVÁLIDA
# ==========================================================

print(
    "\n7 - Testando empresa inválida..."
)

try:

    descarte_service.cadastrar(
        empresa_id="abc",
        equipamento_id=equipamento.id,
        quantidade=1
    )

except ValueError as erro:

    print(
        "Validação funcionando:",
        erro
    )


# ==========================================================
# 8. VALIDAR EQUIPAMENTO INVÁLIDO
# ==========================================================

print(
    "\n8 - Testando equipamento inválido..."
)

try:

    descarte_service.cadastrar(
        empresa_id=empresa.id,
        equipamento_id="abc",
        quantidade=1
    )

except ValueError as erro:

    print(
        "Validação funcionando:",
        erro
    )


# ==========================================================
# 9. EXCLUIR
# ==========================================================

print(
    "\n9 - Testando exclusão..."
)

resultado = (
    descarte_service
    .excluir(
        descarte.id
    )
)


print(
    "Exclusão realizada:",
    resultado
)


# ==========================================================
# 10. CONFIRMAR EXCLUSÃO
# ==========================================================

print(
    "\n10 - Confirmando exclusão..."
)

try:

    descarte_service.buscar_por_id(
        descarte.id
    )

except ValueError:

    print(
        "Registro removido corretamente!"
    )

print(
    "\n===== TESTE FINALIZADO ====="
)