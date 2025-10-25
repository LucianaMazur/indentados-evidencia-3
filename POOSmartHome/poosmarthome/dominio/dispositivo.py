class Dispositivo:
    # Representa un dispositivo inteligente del hogar
    
    def __init__(self, id, nombre, tipo):
        self._id = id
        self._nombre = nombre
        self._tipo = tipo
    
    # Getters
    @property
    def id(self):
        return self._id
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def tipo(self):
        return self._tipo
    
    # Setters
    @id.setter
    def id(self, value):
        self._id = value
    
    @nombre.setter
    def nombre(self, value):
        self._nombre = value
    
    @tipo.setter
    def tipo(self, value):
        self._tipo = value
    
    @staticmethod
    def from_row(row):
        # Crear objeto desde tupla de base de datos
        if row is None:
            return None
        return Dispositivo(id=row[0], nombre=row[1], tipo=row[2])