class Equipamento:

    def __init__(
        self,
        nome,
        categoria="",
        marca="",
        quantidade=1,
        estado="",
        imagem="",
        descricao="",
        id=None
    ):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.marca = marca
        self.quantidade = quantidade
        self.estado = estado
        self.imagem = imagem
        self.descricao = descricao

    def __str__(self):
        return self.nome