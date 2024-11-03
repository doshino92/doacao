from enum import Enum


class TipoVacina(Enum):
    LEPTOSPIROSE = "leptospirose"
    HEPATITE = "hepatite"
    RAIVA = "raiva"

class TipoPorte(Enum):
    PEQUENO = "pequeno"
    MEDIO = "médio"
    GRANDE = "grande"

class TipoAnimal(Enum):
    CACHORRO = "cachorro"
    GATO = "gato"

class TipoMoradia(Enum):
    APARTAMENTO = "apartamento"
    CASA = "casa"
