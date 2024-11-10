from abc import ABC, abstractmethod
from enum import Enum

class Gender(Enum):
    male = 'male'
    female = 'female'
    none = 'none'

type Properties = dict[str, str | float]

class IAnimal(ABC):
    @abstractmethod
    def set_age(self, age: float) -> None: pass

    @abstractmethod
    def set_gender(self, gender: Gender) -> None: pass

    @abstractmethod
    def set_color(self, color: str) -> None: pass

    @abstractmethod
    def set_animal_type(self, type: str) -> None: pass

    @abstractmethod
    def get_nickname(self) -> str | None: pass

    @abstractmethod
    def get_age(self) -> float: pass

    @abstractmethod
    def get_gender(self) -> Gender: pass

    @abstractmethod
    def get_color(self) -> str: pass

    @abstractmethod
    def get_animal_type(self) -> str: pass

    @abstractmethod
    def get_properties(self) -> dict: pass


class IPet(ABC):
    @abstractmethod
    def set_nickname(self, nickname: str) -> None: pass

class Pet(IAnimal, IPet):
    __nickname: str | None
    __age: float
    __gender: Gender
    __color: str
    __animal_type: str

    def __init__(self, nickname: str | None, age: float, gender: Gender, color: str, animal_type: str) -> None:
        self.__nickname = nickname
        self.__age = age
        self.__gender = gender
        self.__color = color
        self.__animal_type = animal_type

    def set_nickname(self, nickname: str=None) -> None:
        self.__nickname = nickname

    def set_age(self, age: float) -> None:
        self.__age = age

    def set_gender(self, gender: Gender) -> None:
        self.__gender = gender
         
    def set_color(self, color: str) -> None:
        self.__color = color

    def set_animal_type(self, type: str) -> None:
        self.__animal_type = type

    def get_nickname(self) -> str | None:
        return self.__nickname

    def get_age(self) -> float:
        return self.__age

    def get_gender(self) -> Gender:
        return self.__gender

    def get_color(self) -> str:
        return self.__color
    
    def get_animal_type(self) -> str:
        return self.__animal_type
    
    def get_properties(self) -> dict: 
        return ({
            "nickname": self.__nickname, 
            "age": self.__age, 
            "gender": self.__gender, 
            "color": self.__color,
            "animal_type": self.__animal_type
        })


class IMovingPet(ABC):
    @abstractmethod
    def move(self) -> None: pass

class MovingPet(Pet, IMovingPet):
    def __init__(self, nickname: str, age: float, gender: Gender, color: str, animal_type: str) -> None:
        super().__init__(nickname, age, gender, color, animal_type)

    def move(self) -> None:
        print('This pet is moving')


class FlyingPet(ABC):
    @abstractmethod
    def fly(self) -> None: pass

class FlyingPet(Pet):
    def __init__(self, nickname: str, age: float, gender: Gender, color: str, animal_type: str) -> None:
        super().__init__(nickname, age, gender, color, animal_type)

    def fly(self) -> None:
        print('This pet is flying')
