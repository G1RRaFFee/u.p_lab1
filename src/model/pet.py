from utils.constants import PetEnum


class Pet:
    def __init__(self, species: PetEnum, pet_id: int, name: str, age: int):
        if not PetEnum.is_valid_type(species): 
            raise ValueError(f"Недопустимый тип животного: {species}")
        
        self.__pet_id: int = pet_id
        self.__name: str = name
        self.__species: str = species
        self.__age: int = age
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def species(self) -> str:
        return self.__species

    @property
    def age(self) -> int:
        return self.__age
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @species.setter
    def species(self, species: PetEnum) -> None:
        self.__species = species

    @age.setter
    def age(self, age: int) -> None:
        self.__age = age
    
    def to_dict(self):
        return {
            "species": self.__species,
            "pet_id": self.__pet_id,
            "name": self.__name,
            "age": self.__age
        }

    @staticmethod
    def from_dict(data: dict):
        return Pet(
            pet_id=data["pet_id"],
            name=data["name"],
            species=data["species"],
            age=data["age"]
        )

    def make_sound(self):
        return "This pet makes a sound."

    def __str__(self):
        return f"{self.species} - {self.name}, возраст: {self.age}"

class Dog(Pet):
    def __init__(self, pet_id: int, name: str, age: int, breed: str):
        super().__init__(pet_id, name, "Собака", age)
        self.breed = breed

    def make_sound(self):
        return "Гав-гав!"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["breed"] = self.breed
        return data

class Cat(Pet):
    def __init__(self, pet_id: int, name: str, age: int, color: str):
        super().__init__(pet_id, name, "Кот", age)
        self.color = color

    def make_sound(self):
        return "Мяу!"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["color"] = self.color
        return data

class Bird(Pet):
    def __init__(self, pet_id: int, name: str, age: int, species: str, can_fly: bool):
        super().__init__(pet_id, name, species, age)
        self.can_fly = can_fly

    def make_sound(self):
        return "Чирик-чирик!"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["can_fly"] = self.can_fly
        return data

class Fish(Pet):
    def __init__(self, pet_id: int, name: str, age: int, water_type: str):
        super().__init__(pet_id, name, "Рыба", age)
        self.water_type = water_type  # Например, пресная или соленая вода

    def make_sound(self):
        return "..."

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["water_type"] = self.water_type
        return data

class Hamster(Pet):
    def __init__(self, pet_id: int, name: str, age: int, favorite_food: str):
        super().__init__(pet_id, name, "Хомяк", age)
        self.favorite_food = favorite_food

    def make_sound(self):
        return "Писк-писк!"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["favorite_food"] = self.favorite_food
        return data

# Crud
# C - create
# r - read
# u - update
# d - delete


