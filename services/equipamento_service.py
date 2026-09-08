from models.equipamento import Equipamento
from repositories.equipamento_repository import EquipamentoRepository

class EquipamentoService:

    CATEGORIAS_PERMITIDAS = {
        "",
        "Celular",
        "Computador",
        "Console",
        "Eletrodoméstico",
        "Equipamento Institucional",
        "Impressora",
        "Monitor",
        "Notebook",
        "Periférico",
        "Roteador",
        "Tablet",
        "Televisor",
        "TV Box",
        "Outro"
    }

    MARCAS_PERMITIDAS = {
        "",
        "Acer",
        "Apple",
        "Aquário",
        "Asus",
        "CCE",
        "Dell",
        "HP",
        "Intelbras",
        "Lenovo",
        "LG",
        "Motorola",
        "Multilaser",
        "Philco",
        "Philips",
        "Positivo",
        "Samsung",
        "Sony",
        "Xiaomi",
        "Outra"
    }

    ESTADOS_PERMITIDOS = {
        "",
        "Funcionando",
        "Com defeito",
        "Danificado",
        "Sem funcionamento",
        "Para descarte"
    }

    def __init__(self):
        self.repository = EquipamentoRepository()

    def validar_categoria(
        self,
        categoria
    ):

        if categoria not in self.CATEGORIAS_PERMITIDAS:
            raise ValueError(
                "Categoria de equipamento inválida."
            )

    def validar_marca(
        self,
        marca
    ):

        if marca not in self.MARCAS_PERMITIDAS:
            raise ValueError(
                "Marca de equipamento inválida."
            )

    def validar_estado(
        self,
        estado
    ):

        if estado not in self.ESTADOS_PERMITIDOS:
            raise ValueError(
                "Estado do equipamento inválido."
            )

    def cadastrar(
        self,
        nome,
        categoria="",
        marca="",
        quantidade=1,
        estado="",
        imagem="",
        descricao=""
    ):

        if not nome:
            raise ValueError(
                "O nome do equipamento é obrigatório."
            )

        self.validar_categoria(
            categoria
        )

        self.validar_marca(
            marca
        )

        self.validar_estado(
            estado
        )

        if quantidade is None:
            quantidade = 1

        try:
            quantidade = int(
                quantidade
            )

        except (
            ValueError,
            TypeError
        ):

            raise ValueError(
                "A quantidade deve ser um número inteiro."
            )

        if quantidade < 1:
            raise ValueError(
                "A quantidade deve ser maior que zero."
            )

        equipamento = Equipamento(
            nome=nome,
            categoria=categoria,
            marca=marca,
            quantidade=quantidade,
            estado=estado,
            imagem=imagem,
            descricao=descricao
        )

        return self.repository.salvar(
            equipamento
        )

    def listar(self):

        return self.repository.listar()

    def buscar_por_id(
        self,
        id
    ):

        equipamento = (
            self.repository
            .buscar_por_id(id)
        )

        if equipamento is None:
            raise ValueError(
                "Equipamento não encontrado."
            )

        return equipamento

    def atualizar(
        self,
        id,
        nome,
        categoria="",
        marca="",
        quantidade=1,
        estado="",
        imagem="",
        descricao=""
    ):

        equipamento = (
            self.repository
            .buscar_por_id(id)
        )

        if equipamento is None:
            raise ValueError(
                "Equipamento não encontrado."
            )

        if not nome:
            raise ValueError(
                "O nome do equipamento é obrigatório."
            )

        self.validar_categoria(
            categoria
        )

        self.validar_marca(
            marca
        )

        self.validar_estado(
            estado
        )

        try:
            quantidade = int(
                quantidade
            )

        except (
            ValueError,
            TypeError
        ):

            raise ValueError(
                "A quantidade deve ser um número inteiro."
            )

        if quantidade < 1:
            raise ValueError(
                "A quantidade deve ser maior que zero."
            )

        equipamento.nome = nome
        equipamento.categoria = categoria
        equipamento.marca = marca
        equipamento.quantidade = quantidade
        equipamento.estado = estado
        equipamento.imagem = imagem
        equipamento.descricao = descricao

        return self.repository.atualizar(
            equipamento
        )

    def excluir(
        self,
        id
    ):

        equipamento = (
            self.repository
            .buscar_por_id(id)
        )

        if equipamento is None:
            raise ValueError(
                "Equipamento não encontrado."
            )

        return self.repository.excluir(
            id
        )