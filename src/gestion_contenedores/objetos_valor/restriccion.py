from dataclasses import dataclass


class RestriccionInvalida(ValueError):
    pass


@dataclass(frozen=True)
class Restriccion:
    mercancia_prohibida: str
    cargas_anteriores: int

    def __post_init__(self) -> None:
        if self.cargas_anteriores <= 0:
            raise RestriccionInvalida("Hay que revisar al menos una carga anterior")
