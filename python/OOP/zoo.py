class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    
    def add_animal(self):
        self.animals.append(Animal())
    
    def add_tiger(self, name):
        self.animals.append( Tiger(name) )
    
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

class Animal: #Each animal should at least have a name, an age, a health level, and happiness level
    def __init__(self,name='no_name',age=5,health=0,happiness=0):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
    
    def display_info(self): #Animal class should have a display_info method that shows the animal's name, health, and happiness.
        print("Animal's name:",self.name,"health:",self.health,"happiness:",self.happiness)
    
    def feed(self): #It should also have a feed method that increases health and happiness by 10.
        self.health += 10
        self.happiness +=10
        return self

class Tiger(Animal):
    def __init__(self,name,color='green',health=10,happiness=10):
        super().__init__(name,health,happiness)
        self.color=color
    
    def feed(self): #It should also have a feed method that increases health and happiness by 20.
        health+=20
        happiness+=20
        return self
    
    def display_tiger_info(self):
        super().display_info()
        print("Color:",self.color)

class Lion(Animal):
    def __init__(self,name,age,bit,health=20,happiness=20):
        super().__init__(name,age,health,happiness)
        self.bit=bit
    
    def feed(self): #It should also have a feed method that increases health and happiness by 25.
        health+=25
        happiness+=25
        return self
    
    def display_lion_info(self):
        super().display_info()
        print("Bits:",self.bit)

class Bear(Animal):
    def __init__(self,name,age,hibernate,health=2,happiness=2):
        super().__init__(name,age,health,happiness)
        self.hibernate=hibernate
    
    def feed(self): #It should also have a feed method that increases health and happiness by 25.
        health+=12
        happiness+=12
        return self
    
    def display_bear_info(self):
        super().display_info()
        print("Hibernates:",self.hibernate)


#puppy=Animal('puppy',20)
tiger=Tiger('Tiger',21,'orange')
tiger.display_tiger_info()
lion = Lion('Lion',30,True)
lion.display_lion_info()
print("hi",type(tiger).__name__)
bear = Bear('Bear',21,True)
bear.display_bear_info()

zoo1 = Zoo("John's Zoo")
zoo1.animals.append(tiger)
zoo1.animals.append(bear)

# zoo1.add_tiger("Rajah")
# zoo1.add_animal()
# zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()
