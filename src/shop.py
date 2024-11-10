from abc import ABC, abstractmethod

from storage import IStorage
from pet import Pet, Properties
from service import PetManagementService, IPetManagementService

class IPetShop(ABC):
    @abstractmethod
    def add_pet(self, pet: Pet) -> None: pass

    @abstractmethod
    def get_pet_by_id(self, pet_id: int) -> Pet | None: pass

    @abstractmethod
    def get_all_pets(self) -> list[Pet]: pass

    @abstractmethod
    def delete_pet(self, pet_id: int) -> None: pass
    
    @abstractmethod
    def update_pet(self, pet_id: int, update_pet_properties: Properties) -> None: pass    

class PetShop(IPetShop):
    __service: IPetManagementService

    def __init__(self, storage: IStorage) -> None:
        PetManagementService(storage)

    def add_pet(self, pet: Pet) -> None:
        self.__service.add_pet(pet.get_properties())

    def delete_pet(self, pet_id: int) -> None:
        self.__service.delete_pet(pet_id)
    
    def update_pet(self, pet_id: int, update_pet_properties: Properties) -> None:
        self.__service.update_pet(pet_id, update_pet_properties)

    def get_pet_by_id(self, pet_id: int) -> Pet | None:
        return self.__service.get_pet(pet_id)

    def get_all_pets(self) -> list[Pet] | None: 
        return self.__service.get_all_pets()
