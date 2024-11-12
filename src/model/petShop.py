from storage.storage import Storage
from model.pet import Pet
from utils.constants import PetEnum

class PetShop:
    def __init__(self, storage: Storage):
        self.storage = storage
        self.current_id = self._get_next_id()

    def _get_next_id(self) -> int:
        data = self.storage.load_from_file()
        pets = data.get("pets", [])
        if not pets:
            return 1
        return max(pet["pet_id"] for pet in pets) + 1
    
    def create_pet(self, name: str, species: PetEnum, age: int):
        pet = Pet(pet_id=self.current_id, name=name, species=species, age=age)
        data = self.storage.load_from_file()
        data["pets"].append(pet.to_dict())
        data["total_count"] = len(data["pets"])
        self.current_id += 1
        self.storage.save_to_file(data)

    def read_all_pets(self):
        data = self.storage.load_from_file()
        return [Pet.from_dict(pet) for pet in data.get("pets", [])]

    def update_pet(self, pet_id: int, name: str, species: PetEnum, age: int):
        data = self.storage.load_from_file()
        pets = data.get("pets", [])
        for i, pet in enumerate(pets):
            if pet["pet_id"] == pet_id:
                pets[i] = Pet(pet_id=pet_id, name=name, species=species, age=age).to_dict()
                data["pets"] = pets
                self.storage.save_to_file(data)
                print(f"Питомец с id {pet_id} обновлен.")
                return
        print(f"Питомец с id {pet_id} не найден.")

    def delete_pet(self, pet_id: int):
        data = self.storage.load_from_file()
        pets = data.get("pets", [])
        new_pets = [pet for pet in pets if pet["pet_id"] != pet_id]
        if len(new_pets) == len(pets):
            print(f"Питомец с id {pet_id} не найден.")
            return
        data["pets"] = new_pets
        data["total_count"] = len(new_pets)
        self.storage.save_to_file(data)
        print(f"Питомец с id {pet_id} удален.")