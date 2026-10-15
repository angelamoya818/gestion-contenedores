from dataclasses import dataclass

from gestion_contenedores.objetos_valor.lugar import Lugar
from gestion_contenedores.objetos_valor.periodo import Periodo


@dataclass(eq=False)
class Viaje:
    identificador: str
    contenedor: str
    periodo: Periodo
    destino: Lugar
    pedido: str | None = None
