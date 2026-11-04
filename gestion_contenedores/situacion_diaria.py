from dataclasses import dataclass
from datetime import date

from gestion_contenedores.lugar import Lugar


@dataclass(frozen=True)
class SituacionDiaria:
    fecha: date
    lugar: Lugar
    mercancia: str | None = None
    viaje: str | None = None
