import customtkinter as ct
root = ct.CTk()

class Cat:
    species = "mammal"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #create a function that finds the oldest cat
    def oldest():
        if cat1.age > cat2.age and cat1.age > cat3.age:
            return(f"{cat1.name} is the oldest and {cat1.age} years old " )

        elif cat2.age > cat1.age and cat2.age > cat3.age:
            return(f"{cat2.name} is the oldest and {cat2.age} years old" )

        else:
            return(f"{cat3.name} is the oldest and {cat3.age} years old" )

    #another approach
    def oldest_cat(self,*cats):
        "The oldest cat is x years old."
        return (f" The oldest cat {max(cats)} years old")



cat1 = Cat("bruce", 3)
cat2 = Cat("dino", 1)
cat3 = Cat("mar", 28)
print(Cat.oldest())
print(Cat.oldest_cat(cat1.age, cat2.age, cat3.age))