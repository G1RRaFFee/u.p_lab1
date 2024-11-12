from abc import ABC, abstractmethod

class Serializer(ABC):
    @abstractmethod
    def to_format(self, pets):
        pass

    @abstractmethod
    def from_format(self, data):
        pass

    @abstractmethod
    def get_type(self):
        pass