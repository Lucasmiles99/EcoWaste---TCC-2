from models.descarte import Descarte
from repositories.descarte_repository import DescarteRepository

class DescarteService:

    def __init__(self):
        self.repository = DescarteRepository()

    def cadastrar(
        self,
        empresa_id,
        equipamento_id,
        quantidade=1,
        data_descarte="",
        status="",
        observacao="",
        ecoponto_id=None
    ):

        if empresa_id is None:
            raise ValueError(
                "A empresa é obrigatória."
            )

        if equipamento_id is None:
            raise ValueError(
                "O equipamento é obrigatório."
            )

        try:
            empresa_id = int(empresa_id)
        except (TypeError, ValueError):
            raise ValueError(
                "Empresa inválida."
            )

        try:
            equipamento_id = int(equipamento_id)
        except (TypeError, ValueError):
            raise ValueError(
                "Equipamento inválido."
            )

        if ecoponto_id in ("", None):
            ecoponto_id = None
        else:
            try:
                ecoponto_id = int(ecoponto_id)
            except (TypeError, ValueError):
                raise ValueError(
                    "Ecoponto inválido."
                )

        try:
            quantidade = int(quantidade)
        except (TypeError, ValueError):
            raise ValueError(
                "A quantidade deve ser um número inteiro."
            )

        if quantidade < 1:
            raise ValueError(
                "A quantidade deve ser maior que zero."
            )

        descarte = Descarte(
            empresa_id=empresa_id,
            equipamento_id=equipamento_id,
            ecoponto_id=ecoponto_id,
            quantidade=quantidade,
            data_descarte=data_descarte,
            status=status,
            observacao=observacao
        )

        return self.repository.salvar(
            descarte
        )

    def listar(self):
        return self.repository.listar()

    def listar_com_detalhes(self):
        return self.repository.listar_com_detalhes()

    def buscar_por_id(self, id):

        descarte = self.repository.buscar_por_id(
            id
        )

        if descarte is None:
            raise ValueError(
                "Descarte não encontrado."
            )

        return descarte

    def atualizar(
        self,
        id,
        empresa_id,
        equipamento_id,
        quantidade=1,
        data_descarte="",
        status="",
        observacao="",
        ecoponto_id=None
    ):

        descarte = self.repository.buscar_por_id(
            id
        )

        if descarte is None:
            raise ValueError(
                "Descarte não encontrado."
            )

        if empresa_id is None:
            raise ValueError(
                "A empresa é obrigatória."
            )

        if equipamento_id is None:
            raise ValueError(
                "O equipamento é obrigatório."
            )

        try:
            empresa_id = int(empresa_id)
        except (TypeError, ValueError):
            raise ValueError(
                "Empresa inválida."
            )

        try:
            equipamento_id = int(equipamento_id)
        except (TypeError, ValueError):
            raise ValueError(
                "Equipamento inválido."
            )

        if ecoponto_id in ("", None):
            ecoponto_id = None
        else:
            try:
                ecoponto_id = int(ecoponto_id)
            except (TypeError, ValueError):
                raise ValueError(
                    "Ecoponto inválido."
                )

        try:
            quantidade = int(quantidade)
        except (TypeError, ValueError):
            raise ValueError(
                "A quantidade deve ser um número inteiro."
            )

        if quantidade < 1:
            raise ValueError(
                "A quantidade deve ser maior que zero."
            )

        descarte.empresa_id = empresa_id
        descarte.equipamento_id = equipamento_id
        descarte.ecoponto_id = ecoponto_id
        descarte.quantidade = quantidade
        descarte.data_descarte = data_descarte
        descarte.status = status
        descarte.observacao = observacao

        return self.repository.atualizar(
            descarte
        )

    def excluir(self, id):

        descarte = self.repository.buscar_por_id(
            id
        )

        if descarte is None:
            raise ValueError(
                "Descarte não encontrado."
            )

        return self.repository.excluir(
            id
        )