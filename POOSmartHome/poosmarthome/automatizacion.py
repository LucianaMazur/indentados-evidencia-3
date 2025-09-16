from typing import List
from Dispositivo import Dispositivo

class Automatizacion:
    def __init__(self, auto_id: str, nombre: str, condiciones: dict = None, acciones: List[dict] = None):
        self.auto_id = auto_id
        self.nombre = nombre
        self.condiciones = condiciones or {}
        self.acciones = acciones or []
        self.propietario = None
        self.dispositivos: List[Dispositivo] = []

    def agregar_dispositivo(self, dispositivo: Dispositivo):
        self.dispositivos.append(dispositivo)

    def ejecutar(self):
        return {"auto_id": self.auto_id, "ejecutada": True}

    def __repr__(self):
        return f"Automatizacion({self.auto_id}, {self.nombre}"