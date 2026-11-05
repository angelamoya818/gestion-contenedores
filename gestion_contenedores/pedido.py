from dataclasses import dataclass

from gestion_contenedores.caracteristicas import CaracteristicasCisterna
from gestion_contenedores.lugar import Lugar
from gestion_contenedores.periodo import Periodo
from gestion_contenedores.restriccion import Restriccion
from gestion_contenedores.tipo_servicio import TipoServicio


@dataclass(eq=False)
class Pedido:
    _identificador: str
    _tipo_servicio: TipoServicio
    _periodo: Periodo
    _origen: Lugar
    _destino: Lugar
    _requisitos: CaracteristicasCisterna
    _restriccion: Restriccion | None = None
