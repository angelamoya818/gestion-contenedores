from dataclasses import dataclass


class CaracteristicasInvalidas(ValueError):
    pass


@dataclass(frozen=True)
class Caracteristicas:
    adr: bool
    csc: bool
    rompeolas: bool
    got: bool
    capacidad: int
    calentar: bool

    def __post_init__(self) -> None:
        if self.capacidad <= 0:
            raise CaracteristicasInvalidas("La capacidad tiene que ser positiva")
