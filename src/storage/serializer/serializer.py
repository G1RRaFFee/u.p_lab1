from abc import ABC, abstractmethod

from model.pet import Pet

PetsData = dict[str, int | list[Pet]]

class Serializer(ABC):
    
    @abstractmethod
    def to_format(self, pets_data: PetsData) -> str:
        pass

    @abstractmethod
    def from_format(self, file_data: str) -> PetsData:
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass