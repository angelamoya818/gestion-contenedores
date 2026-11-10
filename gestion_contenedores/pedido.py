from dataclasses import dataclass, field

from gestion_contenedores.caracteristicas import CaracteristicasCisterna
from gestion_contenedores.lugar import Lugar
from gestion_contenedores.periodo import Periodo
from gestion_contenedores.restriccion import Restriccion
from gestion_contenedores.tipo_servicio import TipoServicio


@dataclass
class Pedido:
    _identificador: str
    _tipo_servicio: TipoServicio = field(compare=False)
    _periodo: Periodo = field(compare=False)
    _origen: Lugar = field(compare=False)
    _destino: Lugar = field(compare=False)
    _requisitos: CaracteristicasCisterna = field(compare=False)
    _restriccion: Restriccion | None = field(default=None, compare=False)