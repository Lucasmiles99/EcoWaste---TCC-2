from models.material import Material
from repositories.material_repository import MaterialRepository

class MaterialService:

    TIPOS_PERMITIDOS = {
        "Bateria",
        "Cabo",
        "Carregador",
        "Cartucho de Impressora",
        "Controle Remoto",
        "Fonte de Alimentação",
        "HD",
        "Lâmpada",
        "Memória RAM",
        "Pilha",
        "Placa Eletrônica",
        "SSD",
        "Outro"
    }

    CATEGORIAS_PERMITIDAS = {
        "",
        "Acessórios",
        "Armazenamento",
        "Baterias e Pilhas",
        "Cabeamento",
        "Componentes Eletrônicos",
        "Energia",
        "Iluminação",
        "Impressão",
        "Informática",
        "Outro"
    }

    def __init__(self):
        self.repository = MaterialRepository()

    def validar_tipo(
        self,
        nome
    ):

        if nome not in self.TIPOS_PERMITIDOS:
            raise ValueError(
                "Tipo de material inválido."
            )

    def validar_categoria(
        self,
        categoria
    ):

        if categoria not in self.CATEGORIAS_PERMITIDAS:
            raise ValueError(
                "Categoria de material inválida."
            )

    def cadastrar(
        self,
        nome,
        categoria="",
        imagem="",
        descricao=""
    ):

        if not nome or not nome.strip():
            raise ValueError(
                "O nome do Material é obrigatório."
            )

        nome = nome.strip()
        categoria = categoria.strip()
        imagem = imagem.strip()
        descricao = descricao.strip()

        self.validar_tipo(
            nome
        )

        self.validar_categoria(
            categoria
        )

        material = Material(
            nome=nome,
            categoria=categoria,
            imagem=imagem,
            descricao=descricao
        )

        return self.repository.salvar(
            material
        )

    def listar(self):

        return self.repository.listar()

    def buscar_por_id(
        self,
        id
    ):

        material = (
            self.repository
            .buscar_por_id(id)
        )

        if material is None:
            raise ValueError(
                "Material não encontrado."
            )

        return material

    def atualizar(
        self,
        id,
        nome,
        categoria="",
        imagem="",
        descricao=""
    ):

        material = (
            self.repository
            .buscar_por_id(id)
        )

        if material is None:
            raise ValueError(
                "Material não encontrado."
            )

        if not nome or not nome.strip():
            raise ValueError(
                "O nome do Material é obrigatório."
            )

        nome = nome.strip()
        categoria = categoria.strip()
        imagem = imagem.strip()
        descricao = descricao.strip()

        self.validar_tipo(
            nome
        )

        self.validar_categoria(
            categoria
        )

        material.nome = nome
        material.categoria = categoria
        material.imagem = imagem
        material.descricao = descricao

        return self.repository.atualizar(
            material
        )

    def excluir(
        self,
        id
    ):

        material = (
            self.repository
            .buscar_por_id(id)
        )

        if material is None:
            raise ValueError(
                "Material não encontrado."
            )

        return self.repository.excluir(
            id
        )