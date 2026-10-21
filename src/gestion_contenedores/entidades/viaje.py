from gestion_contenedores.objetos_valor.lugar import Lugar
from gestion_contenedores.objetos_valor.periodo import Periodo


class Viaje:
    def __init__(
        self,
        identificador: str,
        contenedor: str,
        periodo: Periodo,
        destino: Lugar,
        pedido: str | None = None,
    ) -> None:
        self._identificador = identificador
        self._contenedor = contenedor
        self._periodo = periodo
        self._destino = destino
        self._pedido = pedido
