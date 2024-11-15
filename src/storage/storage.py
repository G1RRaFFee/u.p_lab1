import os

from storage.serializer.serializer import Serializer
from utils.constants import FilePathEnum
from storage.serializer.serializer import PetsData

class Storage:
    def __init__(self, serializer: Serializer):
        self.serializer: Serializer = serializer
        self.db_path: str = FilePathEnum.get_path(serializer.get_type())

    def save_to_file(self, pets_data: PetsData) -> None:
        try:
            if not os.path.exists(self.db_path):
                self._create_file(self.db_path)
            with open(self.db_path, 'w', encoding='utf-8') as file:
                file.write(self.serializer.to_format(pets_data))
                print(f"Данные сохранены в файл: {self.db_path}")
        except Exception as error:
            print(f"Ошибка при сохранении данных: {error}")

    def load_from_file(self) -> PetsData:
        try:
            if not os.path.exists(self.db_path):
                self._create_file()
            with open(self.db_path, 'r', encoding='utf-8') as file:
                return self.serializer.from_format(file.read())
        except Exception as error:
            print(f"Ошибка при загрузке данных: {error}")
            return {"total_count": 0, "pets": []}

    def _create_file(self):
        print(f"Создание нового файла: {self.db_path}")
        initial_data: PetsData = {"total_count": 0, "pets": []}
        with open(self.db_path, 'w', encoding='utf-8') as file:
            file.write(self.serializer.to_format(initial_data))