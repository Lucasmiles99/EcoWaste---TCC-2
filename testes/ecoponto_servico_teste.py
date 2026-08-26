from services.ecoponto_service import EcopontoService

service = EcopontoService()

print(
    "\n===== TESTANDO O SERVIÇO DO ECOPONTO ====="
)


# ==========================================================
# 1. CADASTRAR
# ==========================================================

print("\n1 - Testando cadastro...")

ecoponto = service.cadastrar(
    nome="Ecoponto Municipal",
    endereco="Rua Teste, 123",
    cidade="Rio do Sul",
    localizacao_maps="https://maps.google.com/",
    imagem="ecoponto.jpg",
    descricao="Ponto destinado ao descarte de resíduos."
)

print("Ecoponto cadastrado!")
print("ID:", ecoponto.id)
print("Nome:", ecoponto.nome)


# ==========================================================
# 2. LISTAR
# ==========================================================

print("\n2 - Testando listagem...")

ecopontos = service.listar()

for item in ecopontos:
    print(
        item.id,
        "-",
        item.nome,
        "-",
        item.cidade
    )


# ==========================================================
# 3. BUSCAR
# ==========================================================

print("\n3 - Testando busca...")

encontrado = service.buscar_por_id(
    ecoponto.id
)

print("Encontrado:", encontrado.nome)


# ==========================================================
# 4. ATUALIZAR
# ==========================================================

print("\n4 - Testando atualização...")

atualizado = service.atualizar(
    id=ecoponto.id,
    nome="Ecoponto Municipal Atualizado",
    endereco="Rua Teste, 456",
    cidade="Rio do Sul",
    localizacao_maps="https://maps.google.com/",
    imagem="ecoponto_atualizado.jpg",
    descricao="Ecoponto atualizado durante o teste."
)

print(
    "Nome atualizado:",
    atualizado.nome
)


# ==========================================================
# 5. VALIDAR CAMPO OBRIGATÓRIO
# ==========================================================

print(
    "\n5 - Testando validação..."
)

try:
    service.cadastrar(
        nome="",
        endereco="Rua Teste",
        cidade="Rio do Sul"
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
    ecoponto.id
)

print(
    "Exclusão realizada:",
    resultado
)


# ==========================================================
# 7. CONFIRMAR EXCLUSÃO
# ==========================================================

print(
    "\n7 - Confirmando exclusão..."
)

try:
    service.buscar_por_id(
        ecoponto.id
    )

except ValueError:
    print(
        "Registro removido corretamente!"
    )

print(
    "\n===== TESTE FINALIZADO ====="
)