from dataclasses import dataclass


@dataclass(frozen=True)
class Lugar:
    direccion: str
    ciudad: str
    provincia: str
