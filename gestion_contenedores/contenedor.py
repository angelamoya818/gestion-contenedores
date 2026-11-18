from dataclasses import dataclass, field

from gestion_contenedores.caracteristicas import CaracteristicasCisterna
from gestion_contenedores.situacion_diaria import SituacionDiaria


@dataclass
class Contenedor:
    _identificador: str
    _caracteristicas: CaracteristicasCisterna = field(compare=False)
    _historial: list[SituacionDiaria] = field(default_factory=list, compare=False)