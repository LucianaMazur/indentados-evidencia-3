from typing import List
from .registro_actividad import RegistroActividad

class Dispositivo:
    def __init__(self, device_id: str, tipo: str, ubicacion: str = None):
        self.device_id = device_id
        self.tipo = tipo
        self.ubicacion = ubicacion
        self.registros: List[RegistroActividad] = []

    def agregar_registro(self, registro):
        registro.dispositivo = self
        self.registros.append(registro)

    def __repr__(self):
        return f"Dispositivo({self.device_id}, {self.tipo})"
