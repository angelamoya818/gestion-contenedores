from dataclasses import dataclass


@dataclass(frozen=True)
class CaracteristicasCisterna:
    certificado_adr: bool
    certificado_csc: bool
    dispone_rompeolas: bool
    capacidad: int
    calentar: bool
