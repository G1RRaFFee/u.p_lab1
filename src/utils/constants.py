from enum import Enum

JSON_DB_PATH = '../db/json/db.json'
XML_DB_PATH = '../db/xml/db.xml'

class FilePathEnum(Enum):
    JSON = JSON_DB_PATH
    XML = XML_DB_PATH

    @staticmethod
    def get_path(data_format: str) -> str:
        try:
            return FilePathEnum[data_format.upper()].value
        except KeyError:
            raise ValueError(f"Недопустимый формат файла: {data_format}. Доступные форматы: {', '.join([f.name.lower() for f in FilePathEnum])}")

class PetEnum(Enum):
    CAT = "Кот"
    DOG = "Собака"
    PARROT = "Попугай"
    FISH = "Рыба"
    HAMSTER = "Хомяк"

    @staticmethod
    def is_valid_type(value: str) -> bool:
        return value in [pet_type.value for pet_type in PetEnum]
