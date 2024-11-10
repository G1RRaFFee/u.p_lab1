# Добавить виртуальное окружение.
from xml.etree.ElementTree import Element, SubElement, parse, ParseError, ElementTree, tostring
from xml.dom import minidom
from abc import ABC, abstractmethod
from json import load, dump, JSONDecodeError

from pet import Pet, Properties
from constants import JSON_DB_PATH, XML_DB_PATH  

class IFileManager(ABC):
    @abstractmethod
    def _read_file(self) -> None: pass

    @abstractmethod
    def _write_to_file(self) -> None: pass

class IStorage(ABC):

    @abstractmethod
    def create(self, pet: Properties) -> None: pass

    @abstractmethod
    def delete(self, pet_id: int) -> None: pass

    @abstractmethod
    def update(self, pet_id: int, update_pet_properties: Properties) -> None: pass
    
    @abstractmethod
    def get_all_pets(self) -> list[Pet]: pass

    @abstractmethod
    def get_pet(self, id: int) -> Pet: pass

class JSONStorage(IStorage, IFileManager):
    __file_path: str
    __data: Properties

    def __init__(self, file_name: str) -> None:
        self.__file_path = f'{JSON_DB_PATH}{file_name}.db.json'
        self.__data = self.read()

    def create(self, pet: Properties) -> None:
        pet_id = self.__data["total_count"] + 1
        new_pet = {
            "id": pet_id,
            "nickname": pet["nickname"],
            "age": pet["age"],
            "gender": pet["gender"],
            "color": pet["color"],
            "animal_type": pet["animal_type"]
        }
        self.__data["pets"].append(new_pet)
        self.__data["total_count"] += 1
        self._write_to_file()
    
    def delete(self, pet_id: int) -> bool:
        for pet in self.__data["pets"]:
            if pet["id"] == pet_id:
                self.__data["pets"].remove(pet)
                self.__data["total_count"] -= 1
                self._write_to_file()
                return True
        return False

    def update(self, pet_id: int, updates: Properties) -> bool:
        for pet in self.__data["pets"]:
            if pet["id"] == pet_id:
                pet.update(updates)
                self._write_to_file()
                return True
        return False
    
    def get_all_pets(self) -> list[Pet]:
        return self.__data["pets"]

    def _read_file(self) -> Properties:
        try:
            with open(self.__file_path, 'r') as db:
                return load(db)
        except (FileNotFoundError, JSONDecodeError):
            return {"total_count": 0, "pets": []}
        
    def _write_to_file(self) -> None:
        with open(self.__file_path, 'w') as db:
            dump(self.__data, db, indent=4)
    
    def get_pet(self, pet_id: int) -> Pet | None:
        for pet in self.__data["pets"]:
            if pet["id"] == pet_id:
                return pet;
        return None
    
    
class XMLStorage(IStorage, IFileManager):
    __file_path: str
    __data: Properties

    def __init__(self, file_name: str) -> None:
        self.__file_path = f'{XML_DB_PATH}{file_name}.db.xml'
        self.__data = self.read()

    def create(self, pet: Pet) -> None:
        pet_id = self.__data["total_count"] + 1
        new_pet = Element('pet')
        new_pet.set('id', str(pet_id))
        
        for key, value in pet.items():
            child = SubElement(new_pet, key)
            child.text = str(value)
        
        self.__data["pets"].append(new_pet)
        self.__data["total_count"] += 1
        self._write_to_file()

    def delete(self, pet_id: int) -> bool:
        for pet in self.__data["pets"]:
            if int(pet.get('id')) == pet_id:
                self.__data["pets"].remove(pet)
                self.__data["total_count"] -= 1
                self._write_to_file()
                return True
        return False

    def update(self, pet_id: int, updates: Properties) -> bool:
        for pet in self.__data["pets"]:
            if int(pet.get('id')) == pet_id:
                for key, value in updates.items():
                    child = pet.find(key)
                    if child is not None:
                        child.text = str(value)
                self._write_to_file()
                return True
        return False

    def get_all_pets(self) -> list[Pet]:
        return [{child.tag: child.text for child in pet} for pet in self.__data["pets"]]

    def _read_file(self) -> Properties:
        try:
            tree = parse(self.__file_path)
            root = tree.getroot()

            pets = []
            for pet in root.findall('pet'):
                pets.append(pet)
                
            return {
                "total_count": len(pets),
                "pets": pets
            }
        except (FileNotFoundError, ParseError):
            return {"total_count": 0, "pets": []}
        
    def _write_to_file(self) -> None:
        root = Element('pets')
        for pet in self.__data["pets"]:
            root.append(pet)

        xml_str = tostring(root, encoding='utf-8')
        
        pretty_xml_str = minidom.parseString(xml_str).toprettyxml(indent="    ")

        lines = pretty_xml_str.splitlines()
        cleaned_lines = [line for line in lines if line.strip()]
        final_xml_str = '\n'.join(cleaned_lines)

        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(final_xml_str)

    def get_pet(self, pet_id: int) -> Pet | None:
        for pet in self.__data["pets"]:
            if int(pet.get('id')) == pet_id:
                return {child.tag: child.text for child in pet}
        return None