class Pet:
    # Class attributes
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        
        # Validate pet_type 
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Must be one of {Pet.PET_TYPES}")
        
        self.pet_type = pet_type
        self.owner = owner
        
        # Add to class-level tracking
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        """Returns a list of all pets belonging to this owner"""
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        """Adds a pet to this owner, validating it's a Pet instance"""
        if not isinstance(pet, Pet):
            raise Exception("Must be a Pet instance")
        pet.owner = self
    
    def get_sorted_pets(self):
        """Returns pets sorted alphabetically by name"""
        return sorted(self.pets(), key=lambda pet: pet.name)