class Descarte:

    def __init__(
        self,
        empresa_id,
        equipamento_id,
        quantidade=1,
        data_descarte="",
        status="",
        observacao="",
        ecoponto_id=None,
        id=None
    ):
        self.id = id
        self.empresa_id = empresa_id
        self.equipamento_id = equipamento_id
        self.ecoponto_id = ecoponto_id
        self.quantidade = quantidade
        self.data_descarte = data_descarte
        self.status = status
        self.observacao = observacao

    def __str__(self):
        return (
            f"Descarte {self.id} - "
            f"Empresa {self.empresa_id} - "
            f"Equipamento {self.equipamento_id}"
        )