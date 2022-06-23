from animal_shelter import AnimalShelter

username = "aacuser"
password = "useraac"

# Create the object from the class
shelter = AnimalShelter(username, password)

data = {
    "age_upon_outcome" : "1.7 years",
    "animal_type" : "cat",
    "breed" : "Siamese Mix",
    "color" : "Seal Point",
    "date_of_birth" : "2016-01-25",
    "name" : "Kitty",
    "outcome_subtype" : "",
    "outcome_type" : "Adoption",
    "sex_upon_outcome" : "Intact Female"
}

if shelter.create(data):
    print("Animal added.")
    
if shelter.read(data):
    print("Animal read.")
    
if shelter.update(data):
    print("Animal updated.")
    
if shelter.delete(data):
    print("Animal deleted.")
    
    
    
    
