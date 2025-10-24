from abc import ABC, abstractmethod

class IDispositivoDAO(ABC):
    # Interfaz para DispositivoDAO
    
    @abstractmethod
    def create(self, dispositivo):
        # Crear nuevo dispositivo
        pass
    
    @abstractmethod
    def get_by_id(self, _id):
        # Obtener dispositivo por ID
        pass
    
    @abstractmethod
    def update(self, dispositivo):
        # Actualizar dispositivo existente
        pass
    
    @abstractmethod
    def delete(self, _id):
        # Eliminar dispositivo por ID
        pass
    
    @abstractmethod
    def list_all(self):
        # Listar todos los dispositivos
        pass
