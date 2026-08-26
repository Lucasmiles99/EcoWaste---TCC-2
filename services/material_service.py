from models.material import Material
from repositories.material_repository import MaterialRepository

class MaterialService:

    def __init__(self):
        self.repository = MaterialRepository()

    def cadastrar(
        self,
        nome,
        categoria="",
        descricao=""
    ):
        if not nome or not nome.strip():
            raise ValueError(
                "O nome do Material é obrigatório."
            )

        material = Material(
            nome=nome.strip(),
            categoria=categoria.strip(),
            descricao=descricao.strip()
        )

        return self.repository.salvar(material)

    def listar(self):
        return self.repository.listar()

    def buscar_por_id(self, id):
        material = self.repository.buscar_por_id(id)

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
        descricao=""
    ):
        material = self.repository.buscar_por_id(id)

        if material is None:
            raise ValueError(
                "Material não encontrado."
            )

        if not nome or not nome.strip():
            raise ValueError(
                "O nome do Material é obrigatório."
            )

        material.nome = nome.strip()
        material.categoria = categoria.strip()
        material.descricao = descricao.strip()

        return self.repository.atualizar(material)

    def excluir(self, id):
        material = self.repository.buscar_por_id(id)

        if material is None:
            raise ValueError(
                "Material não encontrado."
            )

        return self.repository.excluir(id)