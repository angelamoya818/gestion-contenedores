from dataclasses import dataclass
from datetime import date

from gestion_contenedores.objetos_valor.lugar import Lugar


class SituacionDiariaInvalida(ValueError):
    pass


@dataclass(frozen=True)
class SituacionDiaria:
    fecha: date
    lugar: Lugar
    cargado: bool
    mercancia: str | None = None
    viaje: str | None = None

    def __post_init__(self) -> None:
        if self.cargado and self.mercancia is None:
            raise SituacionDiariaInvalida(
                "Un contenedor cargado tiene que llevar una mercancía"
            )
        if not self.cargado and self.mercancia is not None:
            raise SituacionDiariaInvalida(
                "Un contenedor vacío no puede llevar mercancía"
            )
