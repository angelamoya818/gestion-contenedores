from dataclasses import dataclass, field

from gestion_contenedores.lugar import Lugar
from gestion_contenedores.periodo import Periodo
from gestion_contenedores.tipo_viaje import TipoViaje


@dataclass
class Viaje:
    _identificador: str
    _contenedor: str = field(compare=False)
    _periodo: Periodo = field(compare=False)
    _destino: Lugar = field(compare=False)
    _pedido: str = field(compare=False)
    _tipo: TipoViaje = field(compare=False)