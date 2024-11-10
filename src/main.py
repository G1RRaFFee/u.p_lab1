from storage import JSONStorage, XMLStorage
from shop import PetShop
from pet import MovingPet, FlyingPet, Gender

xml_storage: XMLStorage = XMLStorage('second')
second_shop: PetShop = PetShop(xml_storage)

parrot: FlyingPet = FlyingPet('Karl', 4, Gender.male.value, 'blue', 'parrot')
second_shop.add_pet(parrot)

# Загрузить в репозиторий

