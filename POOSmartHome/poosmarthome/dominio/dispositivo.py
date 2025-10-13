from dataclasses import dataclass, field
from typing import Dict, Optional, Tuple

@dataclass
class Dispositivo:
    id: int
    nombre: str
    tipo: str
    estado: Dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {"id": self.id, "nombre": self.nombre, "tipo": self.tipo, "estado": self.estado}

    @staticmethod
    def from_row(row: Optional[Tuple]):
        if row is None:
            return None
        return Dispositivo(id=row[0], nombre=row[1], tipo=row[2])
