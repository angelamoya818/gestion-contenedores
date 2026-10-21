from dataclasses import dataclass
from datetime import date


class PeriodoInvalido(ValueError):
    pass


@dataclass(frozen=True)
class Periodo:
    carga: date
    descarga: date

    def __post_init__(self) -> None:
        if self.descarga < self.carga:
            raise PeriodoInvalido(
                f"La descarga ({self.descarga}) es anterior a la carga ({self.carga})"
            )
