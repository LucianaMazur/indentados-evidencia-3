from abc import ABC, abstractmethod

class IAutomatizacionDAO(ABC):

    @abstractmethod
    def crear(self, automatizacion):
        pass

    @abstractmethod
    def obtener_todas(self):
        pass

    @abstractmethod
    def obtener_por_id(self, id_auto):
        pass

    @abstractmethod
    def actualizar(self, automatizacion):
        pass

    @abstractmethod
    def eliminar(self, id_auto):
        pass
