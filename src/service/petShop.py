from storage.storage import Storage
from model.pet import Pet
from utils.constants import PetEnum

class PetShopService:

    def __init__(self, storage: Storage) -> None:
        self.__storage: Storage = storage
        self.__current_id: int = self._get_next_id()
    
    def create_pet(self, species: PetEnum, name: str, age: int) -> None:
        pet = Pet(name=name, species=species, age=age)
        pet.pet_id = self.__current_id
        data = self.__storage.load_from_file()
        data["pets"].append(pet.to_dict())
        data["total_count"] = len(data["pets"])
        self.__current_id += 1
        self.__storage.save_to_file(data)

    def read_all_pets(self) -> list[Pet]:
        data = self.__storage.load_from_file()
        return [Pet.from_dict(pet) for pet in data.get("pets", [])]

    def update_pet(self, species: PetEnum, pet_id: int, name: str, age: int) -> None:
        data = self.__storage.load_from_file()
        pets = data.get("pets", [])
        for i, pet in enumerate(pets):
            if pet["pet_id"] == pet_id:
                updated_pet = Pet(name=name, species=species, age=age)
                updated_pet.pet_id = pet_id
                pets[i] = updated_pet.to_dict()
                data["pets"] = pets
                self.__storage.save_to_file(data)
                print(f"Питомец с id {pet_id} обновлен.")
                return
        print(f"Питомец с id {pet_id} не найден.")

    def delete_pet(self, pet_id: int) -> None:
        data = self.__storage.load_from_file()
        pets = data.get("pets", [])
        new_pets = [pet for pet in pets if pet["pet_id"] != pet_id]
        
        if len(new_pets) == len(pets):
            print(f"Питомец с id {pet_id} не найден.")
            return
        
        data["pets"] = new_pets
        data["total_count"] = len(new_pets)
        self.__storage.save_to_file(data)
        print(f"Питомец с id {pet_id} удален.")

    def _get_next_id(self) -> int:
        data = self.__storage.load_from_file()
        pets = data.get("pets", [])
        if not pets:
            return 1
        return max(pet["pet_id"] for pet in pets) + 1
    