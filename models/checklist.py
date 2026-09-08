class Municipio:
    """
    Representa um município participante
    do Checklist Ambiental.
    """

    def __init__(
        self,
        id=None,
        nome=None
    ):
        self.id = id
        self.nome = nome

    def __repr__(self):
        return (
            f"Municipio("
            f"id={self.id}, "
            f"nome='{self.nome}'"
            f")"
        )

class PerguntaChecklist:
    """
    Representa uma pergunta do
    Checklist Ambiental.
    """

    def __init__(
        self,
        id=None,
        numero=None,
        texto=None
    ):
        self.id = id
        self.numero = numero
        self.texto = texto

    def __repr__(self):
        return (
            f"PerguntaChecklist("
            f"id={self.id}, "
            f"numero={self.numero}, "
            f"texto='{self.texto}'"
            f")"
        )

class RespostaChecklist:
    """
    Representa a resposta de um município
    para uma pergunta do Checklist Ambiental.
    """

    def __init__(
        self,
        id=None,
        municipio_id=None,
        pergunta_id=None,
        resposta=None
    ):
        self.id = id
        self.municipio_id = municipio_id
        self.pergunta_id = pergunta_id
        self.resposta = resposta

    def __repr__(self):
        return (
            f"RespostaChecklist("
            f"id={self.id}, "
            f"municipio_id={self.municipio_id}, "
            f"pergunta_id={self.pergunta_id}, "
            f"resposta='{self.resposta}'"
            f")"
        )