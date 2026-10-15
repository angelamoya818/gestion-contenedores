from dataclasses import dataclass


class LugarInvalido(ValueError):
    pass


@dataclass(frozen=True)
class Lugar:
    ciudad: str
    provincia: str

    def __post_init__(self) -> None:
        if not self.ciudad.strip() or not self.provincia.strip():
            raise LugarInvalido("La ciudad y la provincia no pueden estar vacías")
