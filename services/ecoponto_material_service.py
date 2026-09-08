from repositories.ecoponto_material_repository import (
    EcopontoMaterialRepository
)

from repositories.ecoponto_repository import EcopontoRepository
from repositories.material_repository import MaterialRepository


class EcopontoMaterialService:

    def __init__(self):
        self.repository = EcopontoMaterialRepository()

        self.ecoponto_repository = EcopontoRepository()
        self.material_repository = MaterialRepository()

    def associar(self, ecoponto_id, material_id):
        ecoponto = self.ecoponto_repository.buscar_por_id(
            ecoponto_id
        )

        if ecoponto is None:
            raise ValueError(
                "Ecoponto não encontrado."
            )

        material = self.material_repository.buscar_por_id(
            material_id
        )

        if material is None:
            raise ValueError(
                "Material não encontrado."
            )

        return self.repository.associar(
            ecoponto_id,
            material_id
        )

    def remover_associacao(
        self,
        ecoponto_id,
        material_id
    ):
        return self.repository.remover_associacao(
            ecoponto_id,
            material_id
        )

    def remover_todas_associacoes(
        self,
        ecoponto_id
    ):
        ecoponto = self.ecoponto_repository.buscar_por_id(
            ecoponto_id
        )

        if ecoponto is None:
            raise ValueError(
                "Ecoponto não encontrado."
            )

        return self.repository.remover_todas_associacoes(
            ecoponto_id
        )

    def listar_materiais_do_ecoponto(
        self,
        ecoponto_id
    ):
        return self.repository.listar_materiais_do_ecoponto(
            ecoponto_id
        )

    def listar_ecopontos_do_material(
        self,
        material_id
    ):
        return self.repository.listar_ecopontos_do_material(
            material_id
        )