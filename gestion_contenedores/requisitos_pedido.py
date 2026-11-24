from dataclasses import dataclass


@dataclass(frozen=True)
class RequisitosPedido:
    necesita_adr: bool
    necesita_csc: bool
    necesita_rompeolas: bool
    capacidad_minima: int
    necesita_calentar: bool
