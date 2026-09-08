from models.ecoponto import Ecoponto
from repositories.ecoponto_repository import EcopontoRepository

class EcopontoService:

    MUNICIPIOS_PERMITIDOS = {
        "Agrolândia",
        "Agronômica",
        "Atalanta",
        "Aurora",
        "Braço do Trombudo",
        "Chapadão do Lageado",
        "Dona Emma",
        "Ibirama",
        "Imbuia",
        "Ituporanga",
        "José Boiteux",
        "Laurentino",
        "Lontras",
        "Mirim Doce",
        "Petrolândia",
        "Pouso Redondo",
        "Presidente Getúlio",
        "Presidente Nereu",
        "Rio do Campo",
        "Rio do Oeste",
        "Rio do Sul",
        "Salete",
        "Santa Terezinha",
        "Taió",
        "Trombudo Central",
        "Vidal Ramos",
        "Vitor Meireles",
        "Witmarsum"
    }

    def __init__(self):
        self.repository = EcopontoRepository()

    def validar_cidade(self, cidade):
        if cidade is None:
            raise ValueError(
                "A cidade do Ecoponto é obrigatória."
            )

        cidade = cidade.strip()

        if cidade == "":
            raise ValueError(
                "A cidade do Ecoponto é obrigatória."
            )

        if cidade not in self.MUNICIPIOS_PERMITIDOS:
            raise ValueError(
                "A cidade informada não pertence aos "
                "municípios permitidos do Alto Vale do Itajaí."
            )

        return cidade

    def validar_latitude(self, latitude):
        if latitude is None:
            return None

        if isinstance(latitude, str):
            latitude = latitude.strip()

            if latitude == "":
                return None

            latitude = latitude.replace(",", ".")

        try:
            latitude = float(latitude)
        except (ValueError, TypeError):
            raise ValueError(
                "A latitude deve ser um número válido."
            )

        if latitude < -90 or latitude > 90:
            raise ValueError(
                "A latitude deve estar entre -90 e 90."
            )

        return latitude

    def validar_longitude(self, longitude):
        if longitude is None:
            return None

        if isinstance(longitude, str):
            longitude = longitude.strip()

            if longitude == "":
                return None

            longitude = longitude.replace(",", ".")

        try:
            longitude = float(longitude)
        except (ValueError, TypeError):
            raise ValueError(
                "A longitude deve ser um número válido."
            )

        if longitude < -180 or longitude > 180:
            raise ValueError(
                "A longitude deve estar entre -180 e 180."
            )

        return longitude

    def cadastrar(
        self,
        nome,
        endereco,
        cidade,
        localizacao_maps="",
        latitude=None,
        longitude=None,
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

        cidade_validada = self.validar_cidade(
            cidade
        )

        latitude_validada = self.validar_latitude(
            latitude
        )

        longitude_validada = self.validar_longitude(
            longitude
        )

        ecoponto = Ecoponto(
            nome=nome.strip(),
            endereco=endereco.strip(),
            cidade=cidade_validada,
            localizacao_maps=localizacao_maps.strip(),
            latitude=latitude_validada,
            longitude=longitude_validada,
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
        latitude=None,
        longitude=None,
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

        cidade_validada = self.validar_cidade(
            cidade
        )

        latitude_validada = self.validar_latitude(
            latitude
        )

        longitude_validada = self.validar_longitude(
            longitude
        )

        ecoponto.nome = nome.strip()
        ecoponto.endereco = endereco.strip()
        ecoponto.cidade = cidade_validada
        ecoponto.localizacao_maps = localizacao_maps.strip()
        ecoponto.latitude = latitude_validada
        ecoponto.longitude = longitude_validada
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