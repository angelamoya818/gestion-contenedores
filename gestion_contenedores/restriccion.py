from dataclasses import dataclass


@dataclass(frozen=True)
class Restriccion:
    mercancia_prohibida: str
    cargas_anteriores: int
