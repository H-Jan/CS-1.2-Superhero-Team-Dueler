
# dog.py
class Dog: 
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized")
    
    def bark(self):
        print("Woof!")

    #my_dog = Dog("Rex", "SuperDog")

# Instantiation call to create Dog as an objectL
        ##Dog("Rex")

#Now assigning it to the value of my_dog variable

        ##my_dog = Dog("Rex", "SuperDog")
#Python implicitly passes in "self" so we do not need to pass it in when we call the function
        ##my_dog.bark()

        ##print(my_dog.breed)
        ##print(my_dog)
        ##print(my_dog.name)


