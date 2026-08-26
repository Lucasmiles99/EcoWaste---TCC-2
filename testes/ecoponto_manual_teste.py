from models.ecoponto import Ecoponto
from repositories.ecoponto_repository import EcopontoRepository

repository = EcopontoRepository()

print("\n===== TESTE ECOPONTO REPOSITORY =====")


# ==========================================================
# 1. SALVAR ECOPONTO
# ==========================================================

print("\n1 - Testando salvar...")

ecoponto = Ecoponto(
    nome="Ecoponto Teste",
    endereco="Rua Teste, 100",
    cidade="Rio do Sul",
    localizacao_maps="https://maps.google.com/",
    imagem="ecoponto_teste.jpg",
    descricao="Ecoponto criado para testar o EcoWaste."
)

ecoponto = repository.salvar(ecoponto)

print("Ecoponto salvo!")
print("ID:", ecoponto.id)
print("Nome:", ecoponto.nome)


# ==========================================================
# 2. LISTAR ECOPONTOS
# ==========================================================

print("\n2 - Testando listar...")

ecopontos = repository.listar()

for item in ecopontos:
    print(
        item.id,
        "-",
        item.nome,
        "-",
        item.cidade
    )


# ==========================================================
# 3. BUSCAR POR ID
# ==========================================================

print("\n3 - Testando buscar por ID...")

encontrado = repository.buscar_por_id(ecoponto.id)

if encontrado:
    print("Ecoponto encontrado!")
    print("ID:", encontrado.id)
    print("Nome:", encontrado.nome)
    print("Endereço:", encontrado.endereco)
    print("Cidade:", encontrado.cidade)
else:
    print("Ecoponto não encontrado.")


# ==========================================================
# 4. ATUALIZAR
# ==========================================================

print("\n4 - Testando atualizar...")

encontrado.nome = "Ecoponto Teste Atualizado"
encontrado.descricao = "Registro atualizado durante o teste do EcoWaste."

repository.atualizar(encontrado)

atualizado = repository.buscar_por_id(encontrado.id)

print("Nome atualizado:", atualizado.nome)
print("Descrição atualizada:", atualizado.descricao)


# ==========================================================
# 5. EXCLUIR
# ==========================================================

print("\n5 - Testando excluir...")

resultado = repository.excluir(ecoponto.id)

print("Exclusão realizada:", resultado)


# ==========================================================
# 6. CONFIRMAR EXCLUSÃO
# ==========================================================

print("\n6 - Confirmando exclusão...")

busca_final = repository.buscar_por_id(ecoponto.id)

if busca_final is None:
    print("Registro removido corretamente!")
else:
    print("ERRO: o registro ainda existe.")

print("\n===== TESTE FINALIZADO =====")