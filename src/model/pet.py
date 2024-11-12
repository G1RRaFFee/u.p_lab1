from utils.constants import PetEnum

class Pet:
    def __init__(self, pet_id: int, name: str, species: PetEnum, age: int):
        if not PetEnum.is_valid_type(species):
            raise ValueError(f"Недопустимый тип животного: {species}")
        self.pet_id = pet_id
        self.name = name
        self.species = species
        self.age = age

    def to_dict(self):
        return {
            "pet_id": self.pet_id,
            "name": self.name,
            "species": self.species,
            "age": self.age
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
