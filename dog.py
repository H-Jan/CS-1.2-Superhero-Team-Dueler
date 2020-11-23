
# dog.py
class Dog: 
    
    def bark(self):
        print("Woof!")

my_dogs = list()
my_dogs.append(Dog())
my_dogs.append(Dog())

for dog in my_dogs:
    dog.bark()

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


