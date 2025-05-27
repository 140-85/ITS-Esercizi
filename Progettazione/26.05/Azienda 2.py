from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional


@dataclass
class Indirizzo:
    via: str
    città: str
    cap: str
    stato: str


@dataclass
class Impiegato:
    nome: str
    cognome: str
    nascita: date
    stipendio: float
    progetti: List["Progetto"] = field(default_factory=list)
    dipartimento: Optional["Dipartimento"] = None


@dataclass
class Dipartimento:
    nome: str
    telefono: List[str]
    indirizzo: Optional[Indirizzo] = None
    direttore: Optional[Impiegato] = None


@dataclass
class Progetto:
    nome: str
    budget: float
    impiegati_coinvolti: List[Impiegato] = field(default_factory=list)


@dataclass
class Afferenza:
    impiegato: Impiegato
    progetto: Progetto
    data_afferenza: date