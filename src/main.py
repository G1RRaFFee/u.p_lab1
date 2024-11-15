from storage.storage import Storage
from storage.serializer.jsonSerializer import JsonSerializer
from storage.serializer.xmlSerializer import XmlSerializer
from service.petShop import PetShopService
from exception.exception import InvalidFileTypeException
from utils.constants import PetEnum

def choose_serializer():
    file_types = {
        'json': JsonSerializer(),
        'xml': XmlSerializer()
    }

    while True:
        file_type = input("Выберите формат данных (json/xml): ").strip().lower()
        if file_type not in file_types:
            raise InvalidFileTypeException(file_type)
        return file_types[file_type]
    
def choose_action():
    print("\nДоступные действия:")
    print("1 - Добавить питомца")
    print("2 - Просмотреть всех питомцев")
    print("3 - Обновить данные питомца")
    print("4 - Удалить питомца")
    print("0 - Выход")
    
    while True:
        try:
            choice = int(input("Введите номер действия: "))
            if choice in [0, 1, 2, 3, 4]:
                return choice
            else:
                print("Неверный выбор. Попробуйте снова.")
        except ValueError:
            print("Введите число.")

def input_pet_data():
    while True:
        species = input("Введите тип питомца (Собака, Кот, Рыба, Хомяк) и т.д: ").strip().capitalize()
        if not PetEnum.is_valid_type(species):
            print("Недопустимый тип питомца. Попробуйте снова.")
        else:
            break

    name = input("Введите имя питомца: ").strip()
    
    while True:
        try:
            age = int(input("Введите возраст питомца: "))
            if age >= 0:
                break
            else:
                print("Возраст не может быть отрицательным.")
        except ValueError:
            print("Введите корректное число для возраста.")

    return species, name, age

def main():
    serializer = choose_serializer()
    storage = Storage(serializer)
    service = PetShopService(storage)

    while True:
        action = choose_action()

        if action == 0:
            print("Выход из программы.")
            break

        elif action == 1:  # Создание питомца
            species, name, age = input_pet_data()
            service.create_pet(species, name, age)
            print("Питомец успешно добавлен.")

        elif action == 2:  # Чтение всех питомцев
            pets = service.read_all_pets()
            if not pets:
                print("Нет добавленных питомцев.")
            else:
                for pet in pets:
                    print(pet)

        elif action == 3:  # Обновление питомца
            try:
                pet_id = int(input("Введите ID питомца для обновления: "))
                species, name, age = input_pet_data()
                service.update_pet(species, pet_id, name, age)
            except ValueError:
                print("Некорректный ввод ID.")

        elif action == 4:  # Удаление питомца
            try:
                pet_id = int(input("Введите ID питомца для удаления: "))
                service.delete_pet(pet_id)
            except ValueError:
                print("Некорректный ввод ID.")

if __name__ == "__main__":
    main()


