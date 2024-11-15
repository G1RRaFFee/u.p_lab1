import json

from .serializer import Serializer, PetsData
from model.pet import Pet

class JsonSerializer(Serializer):
    
    def to_format(self, pets_data: Pet) -> str:
        return json.dumps(pets_data, ensure_ascii=False, indent=4)

    def from_format(self, file_data: str) -> PetsData:
        pets_data = json.loads(file_data)    
        return pets_data
    
    def get_type(self) -> str:
        return 'json'