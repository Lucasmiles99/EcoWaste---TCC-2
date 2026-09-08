class Material:

    def __init__(
        self,
        nome,
        categoria="",
        imagem="",
        descricao="",
        id=None
    ):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.imagem = imagem
        self.descricao = descricao

    def __str__(self):
        return self.nome