from dataclasses import dataclass, field

from gestion_contenedores.objetos_valor.caracteristicas import Caracteristicas
from gestion_contenedores.objetos_valor.situacion_diaria import SituacionDiaria


@dataclass(eq=False)
class Contenedor:
    identificador: str
    caracteristicas: Caracteristicas
    historial: list[SituacionDiaria] = field(default_factory=list)
