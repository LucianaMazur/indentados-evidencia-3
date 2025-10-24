from abc import ABC, abstractmethod

class IAutomatizacionDAO(ABC):
    # Interfaz para AutomatizacionDAO
    
    @abstractmethod
    def create(self, automatizacion):
        # Crear nueva automatización
        pass
    
    @abstractmethod
    def get_by_id(self, _id):
        # Obtener automatización por ID
        pass
    
    @abstractmethod
    def update(self, automatizacion):
        # Actualizar automatización existente
        pass
    
    @abstractmethod
    def delete(self, _id):
        # Eliminar automatización por ID
        pass
    
    @abstractmethod
    def list_all(self):
        # Listar todas las automatizaciones
        pass