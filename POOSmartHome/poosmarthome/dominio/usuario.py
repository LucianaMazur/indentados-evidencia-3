from dataclasses import dataclass, field
import re
from typing import Dict, Optional, Tuple

@dataclass
class Usuario:
    id: int
    username: str
    password: str
    nombre: str
    email: str
    role: str = "standard"
    activo: bool = True
    personal_data: Dict[str, str] = field(default_factory=dict)

    def validar_email(self) -> bool:
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, self.email) is not None

    def es_activo(self) -> bool:
        return self.activo

    def is_admin(self) -> bool:
        return self.role == "admin"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "nombre": self.nombre,
            "email": self.email,
            "role": self.role,
            "activo": int(self.activo),
            "personal_data": self.personal_data,
        }

    @staticmethod
    def from_row(row: Optional[Tuple]):
        if row is None:
            return None
        return Usuario(
            id=row[0],
            username=row[1],
            password=row[2],
            nombre=row[3],
            email=row[4],
            role=row[5],
            activo=bool(row[6]),
        )



