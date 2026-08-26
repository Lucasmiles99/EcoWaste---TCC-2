class Ecoponto:

    def __init__(
        self,
        nome,
        endereco,
        cidade,
        localizacao_maps="",
        imagem="",
        descricao="",
        id=None
    ):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.localizacao_maps = localizacao_maps
        self.imagem = imagem
        self.descricao = descricao

    def __str__(self):
        return self.nome