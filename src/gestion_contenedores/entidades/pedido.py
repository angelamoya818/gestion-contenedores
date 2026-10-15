from dataclasses import dataclass

from gestion_contenedores.objetos_valor.caracteristicas import Caracteristicas
from gestion_contenedores.objetos_valor.lugar import Lugar
from gestion_contenedores.objetos_valor.periodo import Periodo
from gestion_contenedores.objetos_valor.restriccion import Restriccion
from gestion_contenedores.objetos_valor.tipo_servicio import TipoServicio


@dataclass(eq=False)
class Pedido:
    identificador: str
    tipo_servicio: TipoServicio
    periodo: Periodo
    origen: Lugar
    destino: Lugar
    requisitos: Caracteristicas
    restriccion: Restriccion | None = None
