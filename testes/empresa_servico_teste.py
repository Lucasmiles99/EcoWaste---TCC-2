from services.empresa_service import EmpresaService


service = EmpresaService()

empresa = service.cadastrar(
    nome="Empresa Service",
    cidade="Rio do Sul",
    segmento="Tecnologia",
    contato="service@empresa.com"
)

print("Empresa cadastrada pelo Service:")
print(empresa)

print("\nEmpresas cadastradas:")

for item in service.listar():
    print(item)