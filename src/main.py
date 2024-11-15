from storage.storage import Storage
from storage.serializer.jsonSerializer import JsonSerializer
from storage.serializer.xmlSerializer import XmlSerializer
from model.pet import Pet
from model.petShop import PetShop
from utils.constants import PetEnum

if __name__ == "__main__":
    serializer = XmlSerializer()
    storage = Storage(serializer)
    pet_shop = PetShop(storage)
    
    # Создаем питомцев
    pet_shop.create_pet(name="РЫЖИК", species=PetEnum.CAT.value, age=7)
    pet_shop.create_pet(name="Шарик", species=PetEnum.FISH.value, age=90)

    # # Читаем всех питомцев
    # pets = pet_shop.read_all_pets()
    # print("Сохраненные питомцы: ")
    # for pet in pets:
    #     print(pet.to_dict())

    # # Обновляем питомца
    # pet_shop.update_pet(pet_id=1, name="Барсик", species=PetEnum.CAT.value, age=4)

    # # Удаляем питомца
    # pet_shop.delete_pet(pet_id=2)

    # # Читаем всех питомцев после удаления
    # pets = pet_shop.read_all_pets()
    # for pet in pets:
    #     print(pet.to_dict())
