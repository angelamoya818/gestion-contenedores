from dataclasses import dataclass

from gestion_contenedores.contenedor import Contenedor


@dataclass
class Flota:
    _contenedores: dict[str, Contenedor]