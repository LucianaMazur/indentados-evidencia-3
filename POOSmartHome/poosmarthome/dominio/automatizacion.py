class Automatizacion:
    # Representa una automatización configurada para un dispositivo
    
    def __init__(self, id, nombre, id_dispositivo, activa=True):
        self._id = id
        self._nombre = nombre
        self._id_dispositivo = id_dispositivo
        self._activa = activa
    
    # Getters
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def id_dispositivo(self):
        return self._id_dispositivo
    
    @property
    def activa(self):
        return self._activa
    
    # Setters
    @id.setter
    def id(self, value):
        self._id = value
    
    @nombre.setter
    def nombre(self, value):
        self._nombre = value
    
    @id_dispositivo.setter
    def id_dispositivo(self, value):
        self._id_dispositivo = value
    
    @activa.setter
    def activa(self, value):
        self._activa = value

    def activar(self):
        # Activar automatización
        self._activa = True
    
    def desactivar(self):
        # Desactivar automatización
        self._activa = False
    
    def cambiar_estado(self):
        # Alternar estado de la automatización
        self._activa = not self._activa
    
    @staticmethod
    def from_row(row):
        # Crear objeto desde tupla de base de datos
        if row is None:
            return None
        return Automatizacion(
            id=row[0],
            nombre=row[1],
            id_dispositivo=row[2],
            activa=bool(row[3])
        )