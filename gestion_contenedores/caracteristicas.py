from dataclasses import dataclass


@dataclass(frozen=True)
class Caracteristicas:
    adr: bool
    csc: bool
    rompeolas: bool
    got: bool
    capacidad: int
    calentar: bool
