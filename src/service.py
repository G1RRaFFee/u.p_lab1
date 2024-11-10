from abc import ABC, abstractmethod

from pet import Pet, Properties
from storage import IStorage

class IPetManagementService(ABC):
    @abstractmethod
    def add_pet(self, pet_properties: Properties) -> None: pass
    
    @abstractmethod
    def get_pet(self, pet_id: int) -> Pet | None: pass

    @abstractmethod
    def get_all_pets(self) -> list[Pet]: pass

    @abstractmethod
    def update_pet(self, pet_id: int, pet_properties: Properties) -> None: pass

    @abstractmethod
    def delete_pet(self, pet_id: int) -> None: pass

class PetManagementService(IPetManagementService):
    
    def __init__(self, storage: IStorage) -> None:
        self.__storage: IStorage = storage

    def add_pet(self, pet_properties: Properties) -> None:
        self.__storage.create(pet_properties)

    def delete_pet(self, pet_id) -> None:
        self.__storage.delete(pet_id)

    def update_pet(self, pet_id: int, pet_properties: Properties) -> None:
        self.__storage.update(pet_id, pet_properties)
    
    def get_all_pets(self) -> list[Pet]:
        return self.__storage.get_all_pets()

    def get_pet(self, pet_id: int) -> Pet | None:
        return self.__storage.get_pet(pet_id)