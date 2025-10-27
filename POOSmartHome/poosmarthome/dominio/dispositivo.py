class Dispositivo:
    # Representa un dispositivo inteligente del hogar
    
    def __init__(self, id=0, nombre='', tipo='', esencial=True):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.esencial = esencial
    
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
        if not row:
            return None
        # Compatibilidad si la tabla aún no tiene el campo
        if len(row) == 3:
            return Dispositivo(id=row[0], nombre=row[1], tipo=row[2], esencial=True)
        else:
            return Dispositivo(id=row[0], nombre=row[1], tipo=row[2], esencial=bool(row[3]))

    def __str__(self):
        tipo = "Esencial" if self.esencial else "No esencial"
        return f"[{self.id}] {self.nombre} - {self.tipo} ({tipo})"