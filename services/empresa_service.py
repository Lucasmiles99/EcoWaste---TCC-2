from models.empresa import Empresa
from repositories.empresa_repository import EmpresaRepository


class EmpresaService:

    def __init__(self):
        self.repository = EmpresaRepository()


    def cadastrar(self, nome, cidade, segmento="", contato=""):
        nome = nome.strip()
        cidade = cidade.strip()
        segmento = segmento.strip()
        contato = contato.strip()

        if not nome:
            raise ValueError("O nome da empresa é obrigatório.")

        if not cidade:
            raise ValueError("A cidade é obrigatória.")

        empresa = Empresa(
            nome=nome,
            cidade=cidade,
            segmento=segmento,
            contato=contato
        )

        return self.repository.salvar(empresa)


    def listar(self):
        return self.repository.listar()


    def buscar_por_id(self, id):
        return self.repository.buscar_por_id(id)


    def atualizar(
        self,
        id,
        nome,
        cidade,
        segmento="",
        contato=""
    ):
        nome = nome.strip()
        cidade = cidade.strip()
        segmento = segmento.strip()
        contato = contato.strip()

        if not nome:
            raise ValueError(
                "O nome da empresa é obrigatório."
            )

        if not cidade:
            raise ValueError(
                "A cidade é obrigatória."
            )

        empresa = Empresa(
            id=id,
            nome=nome,
            cidade=cidade,
            segmento=segmento,
            contato=contato
        )

        return self.repository.atualizar(empresa)


    def excluir(self, id):
        empresa = self.repository.buscar_por_id(id)

        if empresa is None:
            raise ValueError(
                "Empresa não encontrada."
            )

        return self.repository.excluir(id)