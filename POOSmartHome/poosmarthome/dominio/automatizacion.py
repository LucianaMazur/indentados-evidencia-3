class Automatizacion:
   
    def __init__(self, nombre: str, id_dispositivo: int, activa: bool = True, id: int = None):
        self.id = id
        self.nombre = nombre
        self.id_dispositivo = id_dispositivo
        self.activa = activa

    def __str__(self):
    
        estado = "Activa" if self.activa else "Inactiva"
        return f"Automatización [ID: {self.id}] - Nombre: {self.nombre} - Dispositivo: {self.id_dispositivo} ({estado})"




