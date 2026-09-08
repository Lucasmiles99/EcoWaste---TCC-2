from services.equipamento_service import EquipamentoService


service = EquipamentoService()


print("\n===== TESTANDO O SERVIÇO DOS EQUIPAMENTOS =====")


# ==========================================================
# 1. CADASTRAR
# ==========================================================

print("\n1 - Testando cadastro...")

equipamento = service.cadastrar(
    nome="Notebook Acer",
    categoria="Notebook",
    marca="Acer",
    quantidade=2,
    estado="Com defeito",
    imagem="Notebook-Acer.png",
    descricao=(
        "Notebook destinado à análise "
        "para descarte eletrônico."
    )
)

print("Equipamento cadastrado!")
print("ID:", equipamento.id)
print("Nome:", equipamento.nome)
print("Marca:", equipamento.marca)
print("Quantidade:", equipamento.quantidade)
print("Estado:", equipamento.estado)


# ==========================================================
# 2. LISTAR
# ==========================================================

print("\n2 - Testando listagem...")

equipamentos = service.listar()

for item in equipamentos:
    print(
        item.id,
        "-",
        item.nome,
        "-",
        item.categoria,
        "-",
        item.marca,
        "-",
        item.quantidade,
        "-",
        item.estado
    )


# ==========================================================
# 3. BUSCAR
# ==========================================================

print("\n3 - Testando busca...")

encontrado = service.buscar_por_id(
    equipamento.id
)

print("Encontrado:", encontrado.nome)
print("Marca:", encontrado.marca)
print("Estado:", encontrado.estado)


# ==========================================================
# 4. ATUALIZAR
# ==========================================================

print("\n4 - Testando atualização...")

atualizado = service.atualizar(
    id=equipamento.id,
    nome="Notebook Acer Aspire",
    categoria="Notebook",
    marca="Acer",
    quantidade=1,
    estado="Para descarte",
    imagem="Notebook-Acer.png",
    descricao=(
        "Notebook Acer Aspire com defeito "
        "destinado ao descarte eletrônico."
    )
)

print(
    "Nome atualizado:",
    atualizado.nome
)

print(
    "Quantidade atualizada:",
    atualizado.quantidade
)

print(
    "Estado atualizado:",
    atualizado.estado
)


# ==========================================================
# 5. VALIDAR NOME OBRIGATÓRIO
# ==========================================================

print("\n5 - Testando validação do nome...")

try:
    service.cadastrar(
        nome="",
        quantidade=1
    )

except ValueError as erro:
    print(
        "Validação funcionando:",
        erro
    )


# ==========================================================
# 6. VALIDAR QUANTIDADE INVÁLIDA
# ==========================================================

print("\n6 - Testando quantidade inválida...")

try:
    service.cadastrar(
        nome="Televisor",
        quantidade="abc"
    )

except ValueError as erro:
    print(
        "Validação funcionando:",
        erro
    )


# ==========================================================
# 7. VALIDAR QUANTIDADE MENOR QUE 1
# ==========================================================

print("\n7 - Testando quantidade menor que 1...")

try:
    service.cadastrar(
        nome="TV Box",
        quantidade=0
    )

except ValueError as erro:
    print(
        "Validação funcionando:",
        erro
    )


# ==========================================================
# 8. EXCLUIR
# ==========================================================

print("\n8 - Testando exclusão...")

resultado = service.excluir(
    equipamento.id
)

print(
    "Exclusão realizada:",
    resultado
)


# ==========================================================
# 9. CONFIRMAR EXCLUSÃO
# ==========================================================

print("\n9 - Confirmando exclusão...")

try:
    service.buscar_por_id(
        equipamento.id
    )

except ValueError:
    print(
        "Registro removido corretamente!"
    )


print(
    "\n===== TESTE FINALIZADO ====="
)