class UsuarioDispositivo:
    def __init__(self, usuario, dispositivo, fecha_asignacion=None):
        self.usuario = usuario
        self.dispositivo = dispositivo
        self.fecha_asignacion = fecha_asignacion

    def desasignar(self):
        self.usuario = None
        self.dispositivo = None

    def __repr__(self):
        return f"UsuarioDispositivo({self.usuario}, {self.dispositivo})"