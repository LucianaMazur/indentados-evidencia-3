from abc import ABC, abstractmethod
from typing import List, Optional
from poosmarthome.dominio.dispositivo import Dispositivo

class IDispositivoDAO(ABC):
    @abstractmethod
    def create(self, dispositivo: Dispositivo) -> Dispositivo:
        pass

    @abstractmethod
    def get_by_id(self, _id: int) -> Optional[Dispositivo]:
        pass

    @abstractmethod
    def update(self, dispositivo: Dispositivo) -> Dispositivo:
        pass

    @abstractmethod
    def delete(self, _id: int) -> bool:
        pass

    @abstractmethod
    def list_all(self) -> List[Dispositivo]:
        pass

