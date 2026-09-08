class Ecoponto:

    def __init__(
        self,
        nome,
        endereco,
        cidade,
        localizacao_maps="",
        latitude=None,
        longitude=None,
        imagem="",
        descricao="",
        id=None
    ):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.localizacao_maps = localizacao_maps
        self.latitude = latitude
        self.longitude = longitude
        self.imagem = imagem
        self.descricao = descricao

    def __str__(self):
        return self.nome