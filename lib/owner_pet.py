class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self,name,pet_type,owner = None):
        self.name = name
        self.owner  = owner
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception("Wrong pet type")
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self,name):
        self.name  = name
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    def add_pet(self,pet):
        if isinstance(pet,Pet):
            pet.owner = self
        else:
            raise Exception("wrong type, instance should be of type Pet")
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
