from models.empresa import Empresa
from repositories.empresa_repository import EmpresaRepository


repository = EmpresaRepository()

empresa = Empresa(
    nome="Empresa Teste",
    cidade="Rio do Sul",
    segmento="Tecnologia da Informação",
    contato="teste@empresa.com"
)

empresa_salva = repository.salvar(empresa)

print("Empresa cadastrada:")
print(empresa_salva)

print("\nEmpresas cadastradas:")

empresas = repository.listar()

for item in empresas:
    print(item)