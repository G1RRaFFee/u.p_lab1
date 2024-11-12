import json;
from .base import Serializer;

class JsonSerializer(Serializer):
    def to_format(self, pet):
        return json.dumps(pet, ensure_ascii=False, indent=4)

    def from_format(self, data):
        pets_data = json.loads(data)
        return pets_data
    
    def get_type(self):
        return 'json'