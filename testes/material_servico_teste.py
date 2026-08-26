from services.material_service import MaterialService

service = MaterialService()

print("\n===== TESTANDO O SERVIÇO DOS MATERIAIS =====")


# ==========================================================
# 1. CADASTRAR
# ==========================================================

print("\n1 - Testando cadastro...")

material = service.cadastrar(
    nome="Bateria",
    categoria="Resíduo eletrônico",
    descricao="Baterias usadas de equipamentos eletrônicos."
)

print("Material cadastrado!")
print("ID:", material.id)
print("Nome:", material.nome)


# ==========================================================
# 2. LISTAR
# ==========================================================

print("\n2 - Testando listagem...")

materiais = service.listar()

for item in materiais:
    print(
        item.id,
        "-",
        item.nome,
        "-",
        item.categoria
    )


# ==========================================================
# 3. BUSCAR
# ==========================================================

print("\n3 - Testando busca...")

encontrado = service.buscar_por_id(
    material.id
)

print("Encontrado:", encontrado.nome)


# ==========================================================
# 4. ATUALIZAR
# ==========================================================

print("\n4 - Testando atualização...")

atualizado = service.atualizar(
    id=material.id,
    nome="Bateria Eletrônica",
    categoria="Resíduo eletrônico",
    descricao=(
        "Baterias usadas de celulares, notebooks "
        "e outros equipamentos."
    )
)

print(
    "Nome atualizado:",
    atualizado.nome
)


# ==========================================================
# 5. VALIDAR CAMPO OBRIGATÓRIO
# ==========================================================

print("\n5 - Testando validação...")

try:
    service.cadastrar(
        nome=""
    )

except ValueError as erro:
    print(
        "Validação funcionando:",
        erro
    )


# ==========================================================
# 6. EXCLUIR
# ==========================================================

print("\n6 - Testando exclusão...")

resultado = service.excluir(
    material.id
)

print(
    "Exclusão realizada:",
    resultado
)


# ==========================================================
# 7. CONFIRMAR EXCLUSÃO
# ==========================================================

print("\n7 - Confirmando exclusão...")

try:
    service.buscar_por_id(
        material.id
    )

except ValueError:
    print(
        "Registro removido corretamente!"
    )

print(
    "\n===== TESTE FINALIZADO ====="
)