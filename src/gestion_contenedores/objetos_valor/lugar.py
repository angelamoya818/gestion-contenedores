from dataclasses import dataclass


class LugarInvalido(ValueError):
    pass


@dataclass(frozen=True)
class Lugar:
    direccion: str
    ciudad: str
    provincia: str

    def __post_init__(self) -> None:
        if not self.direccion or not self.ciudad or not self.provincia:
            raise LugarInvalido("Un lugar necesita dirección, ciudad y provincia")   