from utils.constants import PetEnum

PET_MAP = {
    'Dog': lambda name, age: Dog(name, age, "Корги"),
    'Cat': lambda name, age: Cat(name, age, "black"),
    'Fish': lambda name, age: Fish(name, age, True),
    'Hamster': lambda name, age: Hamster(name, age, "Злаки"),
}

class Pet:

    def __init__(self, species: str, name: str, age: int) -> None:
        if not PetEnum.is_valid_type(species): 
            raise ValueError(f"Недопустимый тип животного: {species}")
        
        self.__pet_id: int = 0
        self.__name: str = name
        self.__species: str = species
        self.__age: int = age
     
    @property
    def pet_id(self) -> str:
        return self.__pet_id
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def species(self) -> str:
        return self.__species

    @property
    def age(self) -> int:
        return self.__age
    
    @pet_id.setter
    def pet_id(self, id: int) -> None:
        self.__pet_id = id
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @species.setter
    def species(self, species: PetEnum) -> None:
        self.__species = species

    @age.setter
    def age(self, age: int) -> None:
        self.__age = age
    
    def to_dict(self) -> dict:
        return {
            "species": self.__species,
            "pet_id": self.__pet_id,
            "name": self.__name,
            "age": self.__age
        }

    @staticmethod
    def from_dict(data: dict) -> "Pet":
        pet = Pet(data["species"], data["name"], data["age"])
        pet.pet_id = data["pet_id"]
        return pet

    def make_sound(self) -> str:
        return "This pet makes a sound."

    def __str__(self) -> str:
        return f"{self.species} - {self.name}, возраст: {self.age}"

class Dog(Pet):
    def __init__(self, name: str, age: int, breed: str) -> None:
        super().__init__(PetEnum.DOG.value, name, age)
        self.breed: str = breed

    def make_sound(self) -> str:
        return "Гав-гав!"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["breed"] = self.breed
        return data

class Cat(Pet):
    def __init__(self, name: str, age: int, color: str) -> None:
        super().__init__(PetEnum.CAT.value, name, age)
        self.color = color

    def make_sound(self) -> str:
        return "Мяу!"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["color"] = self.color
        return data

class Bird(Pet):
    def __init__(self, name: str, age: int, can_fly: bool) -> None:
        super().__init__(PetEnum.BIRD.value, name, age)
        self.can_fly: bool = can_fly

    def make_sound(self) -> str:
        return "Чирик-чирик!"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["can_fly"] = self.can_fly
        return data

class Fish(Pet):
    def __init__(self, name: str, age: int, water_type: str) -> None:
        super().__init__(PetEnum.FISH.value, name, age)
        self.water_type: str = water_type

    def make_sound(self) -> str:
        return "..."

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["water_type"] = self.water_type
        return data

class Hamster(Pet):
    def __init__(self, name: str, age: int, favorite_food: str) -> None:
        super().__init__(PetEnum.HAMSTER.value, name, age)
        self.favorite_food: str = favorite_food

    def make_sound(self) -> str:
        return "Писк-писк!"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["favorite_food"] = self.favorite_food
        return data

class Rabbit(Pet):
    def __init__(self, name: str, age: int, fur_color: str) -> None:
        super().__init__(PetEnum.RABBIT.value, name, age)
        self.fur_color: str = fur_color

    def make_sound(self) -> str:
        return "Хрум-хрум!"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["fur_color"] = self.fur_color
        return data

class Parrot(Pet):
    def __init__(self, name: str, age: int, vocabulary_size: int) -> None:
        super().__init__(PetEnum.PARROT.value, name, age)
        self.vocabulary_size: int = vocabulary_size

    def make_sound(self) -> str:
        return "Привет!"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["vocabulary_size"] = self.vocabulary_size
        return data

class Turtle(Pet):
    def __init__(self, name: str, age: int, shell_size: float) -> None:
        super().__init__(PetEnum.TURTLE.value, name, age)
        self.shell_size: float = shell_size

    def make_sound(self) -> str:
        return "..."

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["shell_size"] = self.shell_size
        return data

class Ferret(Pet):
    def __init__(self, name: str, age: int, favorite_toy: str) -> None:
        super().__init__(PetEnum.FERRET.value, name, age)
        self.favorite_toy: str = favorite_toy

    def make_sound(self) -> str:
        return "Шур-шур!"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["favorite_toy"] = self.favorite_toy
        return data

class Iguana(Pet):
    def __init__(self, name: str, age: int, habitat: str) -> None:
        super().__init__(PetEnum.IGUANA.value, name, age)
        self.habitat: str = habitat

    def make_sound(self) -> str:
        return "Шшшш!"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["habitat"] = self.habitat
        return data
