from dataclasses import dataclass, field

from gestion_contenedores.caracteristicas import Caracteristicas
from gestion_contenedores.situacion_diaria import SituacionDiaria


@dataclass(eq=False)
class Contenedor:
    _identificador: str
    _caracteristicas: Caracteristicas
    _historial: list[SituacionDiaria] = field(default_factory=list)
