from gestion_contenedores.caracteristicas import Caracteristicas
from gestion_contenedores.situacion_diaria import SituacionDiaria


class Contenedor:
    def __init__(
        self,
        identificador: str,
        caracteristicas: Caracteristicas,
        historial: list[SituacionDiaria] | None = None,
    ) -> None:
        self._identificador = identificador
        self._caracteristicas = caracteristicas
        self._historial = list(historial) if historial else []
