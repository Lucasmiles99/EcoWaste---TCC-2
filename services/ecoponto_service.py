from models.ecoponto import Ecoponto
from repositories.ecoponto_repository import EcopontoRepository

class EcopontoService:

    def __init__(self):
        self.repository = EcopontoRepository()

    def cadastrar(
        self,
        nome,
        endereco,
        cidade,
        localizacao_maps="",
        imagem="",
        descricao=""
    ):
        if not nome or not nome.strip():
            raise ValueError(
                "O nome do Ecoponto é obrigatório."
            )

        if not endereco or not endereco.strip():
            raise ValueError(
                "O endereço do Ecoponto é obrigatório."
            )

        if not cidade or not cidade.strip():
            raise ValueError(
                "A cidade do Ecoponto é obrigatória."
            )

        ecoponto = Ecoponto(
            nome=nome.strip(),
            endereco=endereco.strip(),
            cidade=cidade.strip(),
            localizacao_maps=localizacao_maps.strip(),
            imagem=imagem.strip(),
            descricao=descricao.strip()
        )

        return self.repository.salvar(ecoponto)

    def listar(self):
        return self.repository.listar()

    def buscar_por_id(self, id):
        ecoponto = self.repository.buscar_por_id(id)

        if ecoponto is None:
            raise ValueError(
                "Ecoponto não encontrado."
            )

        return ecoponto

    def atualizar(
        self,
        id,
        nome,
        endereco,
        cidade,
        localizacao_maps="",
        imagem="",
        descricao=""
    ):
        ecoponto = self.repository.buscar_por_id(id)

        if ecoponto is None:
            raise ValueError(
                "Ecoponto não encontrado."
            )

        if not nome or not nome.strip():
            raise ValueError(
                "O nome do Ecoponto é obrigatório."
            )

        if not endereco or not endereco.strip():
            raise ValueError(
                "O endereço do Ecoponto é obrigatório."
            )

        if not cidade or not cidade.strip():
            raise ValueError(
                "A cidade do Ecoponto é obrigatória."
            )

        ecoponto.nome = nome.strip()
        ecoponto.endereco = endereco.strip()
        ecoponto.cidade = cidade.strip()
        ecoponto.localizacao_maps = localizacao_maps.strip()
        ecoponto.imagem = imagem.strip()
        ecoponto.descricao = descricao.strip()

        return self.repository.atualizar(ecoponto)

    def excluir(self, id):
        ecoponto = self.repository.buscar_por_id(id)

        if ecoponto is None:
            raise ValueError(
                "Ecoponto não encontrado."
            )

        return self.repository.excluir(id)