from dataclasses import dataclass, field

from gestion_contenedores.lugar import Lugar
from gestion_contenedores.periodo import Periodo


@dataclass
class Viaje:
    _identificador: str
    _contenedor: str = field(compare=False)
    _periodo: Periodo = field(compare=False)
    _destino: Lugar = field(compare=False)
    _pedido: str | None = field(default=None, compare=False)