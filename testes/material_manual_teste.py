from models.material import Material
from repositories.material_repository import MaterialRepository


repository = MaterialRepository()

print("\n===== TESTE MATERIAL REPOSITORY =====")


# ==========================================================
# 1. SALVAR MATERIAL
# ==========================================================

print("\n1 - Testando salvar...")

material = Material(
    nome="Bateria",
    categoria="Resíduo eletrônico",
    descricao="Baterias usadas provenientes de equipamentos eletrônicos."
)

material = repository.salvar(material)

print("Material salvo!")
print("ID:", material.id)
print("Nome:", material.nome)


# ==========================================================
# 2. LISTAR MATERIAIS
# ==========================================================

print("\n2 - Testando listar...")

materiais = repository.listar()

for item in materiais:
    print(
        item.id,
        "-",
        item.nome,
        "-",
        item.categoria
    )


# ==========================================================
# 3. BUSCAR POR ID
# ==========================================================

print("\n3 - Testando buscar por ID...")

encontrado = repository.buscar_por_id(material.id)

if encontrado:
    print("Material encontrado!")
    print("ID:", encontrado.id)
    print("Nome:", encontrado.nome)
    print("Categoria:", encontrado.categoria)
    print("Descrição:", encontrado.descricao)
else:
    print("Material não encontrado.")


# ==========================================================
# 4. ATUALIZAR
# ==========================================================

print("\n4 - Testando atualizar...")

encontrado.nome = "Bateria Eletrônica"
encontrado.descricao = (
    "Baterias usadas de celulares, notebooks "
    "e outros equipamentos eletrônicos."
)

repository.atualizar(encontrado)

atualizado = repository.buscar_por_id(encontrado.id)

print("Nome atualizado:", atualizado.nome)
print("Descrição atualizada:", atualizado.descricao)


# ==========================================================
# 5. EXCLUIR
# ==========================================================

print("\n5 - Testando excluir...")

resultado = repository.excluir(material.id)

print("Exclusão realizada:", resultado)


# ==========================================================
# 6. CONFIRMAR EXCLUSÃO
# ==========================================================

print("\n6 - Confirmando exclusão...")

busca_final = repository.buscar_por_id(material.id)

if busca_final is None:
    print("Registro removido corretamente!")
else:
    print("ERRO: o registro ainda existe.")


print("\n===== TESTE FINALIZADO =====")