from enum import Enum


class TipoVacina(Enum):
    LEPTOSPIROSE = "leptospirose"
    HEPATITE = "hepatite"
    RAIVA = "raiva"

class TipoPorte(Enum):
    pequeno = "pequeno"
    medio = "médio"
    grande = "grande"

class TipoAnimal(Enum):
    CACHORRO = "cachorro"
    GATO = "gato"

class TipoMoradia(Enum):
    APARTAMENTO = "apartamento"
    CASA = "casa"