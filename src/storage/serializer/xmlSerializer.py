from xml.etree.ElementTree import Element, SubElement, tostring, fromstring
from xml.dom.minidom import parseString

from storage.serializer.serializer import Serializer
from .serializer import PetsData

class XmlSerializer(Serializer):

    def to_format(self, pets_data: PetsData) -> str:
       root = Element("pets")
       total_count = SubElement(root, "total_count")
       total_count.text = str(pets_data.get("total_count", 0))
       pets_element = SubElement(root, "pets_list")

       for pet in pets_data.get("pets", []):
           pet_element = SubElement(pets_element, "pet")
           for key, value in pet.items():
               child = SubElement(pet_element, key)
               child.text = str(value)
       
       raw_xml = tostring(root, encoding='unicode')
       
       dom = parseString(raw_xml)
       pretty_xml = dom.toprettyxml(indent="    ")
       return pretty_xml

    def from_format(self, file_data: str) -> PetsData:
        root = fromstring(file_data)
        pets = []
        total_count = int(root.find("total_count").text)

        for pet_element in root.find("pets_list"):
            pet_data = {child.tag: child.text for child in pet_element}
            pet_data["pet_id"] = int(pet_data["pet_id"])
            pet_data["age"] = int(pet_data["age"])
            pets.append(pet_data)

        return {"total_count": total_count, "pets": pets}

    def get_type(self) -> str:
        return 'xml'