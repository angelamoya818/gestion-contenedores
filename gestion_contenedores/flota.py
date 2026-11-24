from dataclasses import dataclass

from gestion_contenedores.contenedor import Contenedor
from gestion_contenedores.viaje import Viaje


@dataclass
class Flota:
    _contenedores: dict[str, Contenedor]
    _viajes: dict[str, Viaje]