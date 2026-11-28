from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Periodo:
    carga: date
    descarga: date
