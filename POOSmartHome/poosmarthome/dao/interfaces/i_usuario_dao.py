from abc import ABC, abstractmethod

class IUsuarioDAO(ABC):
    # Interfaz para UsuarioDAO
    
    @abstractmethod
    def create(self, usuario):
        # Crear nuevo usuario
        pass
    
    @abstractmethod
    def get_by_id(self, _id):
        # Obtener usuario por ID
        pass
    
    @abstractmethod
    def get_by_username(self, username):
        # Obtener usuario por username
        pass
    
    @abstractmethod
    def update(self, usuario):
        # Actualizar usuario existente
        pass
    
    @abstractmethod
    def delete(self, _id):
        # Eliminar usuario por ID
        pass
    
    @abstractmethod
    def list_all(self):
        # Listar todos los usuarios
        pass