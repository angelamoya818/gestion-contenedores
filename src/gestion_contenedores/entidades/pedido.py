from gestion_contenedores.objetos_valor.caracteristicas import Caracteristicas
from gestion_contenedores.objetos_valor.lugar import Lugar
from gestion_contenedores.objetos_valor.periodo import Periodo
from gestion_contenedores.objetos_valor.restriccion import Restriccion
from gestion_contenedores.objetos_valor.tipo_servicio import TipoServicio


class Pedido:
    def __init__(
        self,
        identificador: str,
        tipo_servicio: TipoServicio,
        periodo: Periodo,
        origen: Lugar,
        destino: Lugar,
        requisitos: Caracteristicas,
        restriccion: Restriccion | None = None,
    ) -> None:
        self._identificador = identificador
        self._tipo_servicio = tipo_servicio
        self._periodo = periodo
        self._origen = origen
        self._destino = destino
        self._requisitos = requisitos
        self._restriccion = restriccion