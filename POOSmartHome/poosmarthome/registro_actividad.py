class RegistroActividad:
    def __init__(self, registro_id: str, accion: str, timestamp: float = None):
        self.registro_id = registro_id
        self.accion = accion
        self.timestamp = timestamp
        self.usuario = None
        self.dispositivo = None

    def __repr__(self):
        return f"Registro({self.registro_id}, {self.accion})"
