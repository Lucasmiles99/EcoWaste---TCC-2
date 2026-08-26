class Empresa:
    def __init__(self, nome, cidade, segmento="", contato="", id=None):
        self.id = id
        self.nome = nome
        self.cidade = cidade
        self.segmento = segmento
        self.contato = contato

    def __str__(self):
        return f"Empresa(id={self.id}, nome='{self.nome}', cidade='{self.cidade}')"