from dataclasses import dataclass

from gestion_contenedores.lugar import Lugar
from gestion_contenedores.periodo import Periodo


@dataclass(eq=False)
class Viaje:
    _identificador: str
    _contenedor: str
    _periodo: Periodo
    _destino: Lugar
    _pedido: str | None = None
