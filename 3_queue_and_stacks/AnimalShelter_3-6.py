class Animal:
    def __init__(self, name):
        self.name = name
        self.order = 0
        
    def setOrder(self, order):
        self.order = order
        
    def isOlderThan(self, animal):
        return self.order < animal.order

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

class AnimalShelter:
    def __init__(self):
        self.order = 0
        self.cats = []
        self.dogs = []
    
    def isEmpty(self):
        return len(self.cats) == 0 and len(self.dogs) == 0
    
    def enqueue(self, animal: Animal) -> bool:
        animal.setOrder(self.order)
        self.order += 1
        
        if type(animal) == Dog:
            self.dogs.append(animal)
        if type(animal) == Cat:
            self.cats.append(animal)
                        
        return True
        
    
    def dequeueAny(self):
        if self.isEmpty():
            raise IndexError("Empty!")

        if len(self.cats) == 0:
            return self.dogs.pop(0)
        
        if len(self.dogs) == 0:
            return self.cats.pop(0)
        
        lastDog: Dog = self.dogs[0]
        lastCat: Cat = self.cats[0]
        
        if (lastCat.isOlderThan(lastDog)):
            return self.cats.pop(0)
        
        return self.dogs.pop(0)
        
    
    def dequeueDog(self):
        return self.dogs.pop(0)
    
    def dequeueCat(self):
        return self.cats.pop(0)



shelter = AnimalShelter()

d1 = Dog("Rex")      # 0
c1 = Cat("Mimi")     # 1
d2 = Dog("Bolt")     # 2
c2 = Cat("Luna")     # 3
d3 = Dog("Max")      # 4
c3 = Cat("Nina")     # 5
d4 = Dog("Thor")     # 6

shelter.enqueue(d1)
shelter.enqueue(c1)
shelter.enqueue(d2)
shelter.enqueue(c2)
shelter.enqueue(d3)
shelter.enqueue(c3)
shelter.enqueue(d4)

# Mais antigo geral: d1
assert shelter.dequeueAny() is d1

# Remove gato mais antigo: c1
assert shelter.dequeueCat() is c1

# Restantes:
# Dogs: d2(2), d3(4), d4(6)
# Cats: c2(3), c3(5)

# Mais antigo geral: d2
assert shelter.dequeueAny() is d2

# Remove cachorro mais antigo: d3
assert shelter.dequeueDog() is d3

# Restantes:
# Dogs: d4(6)
# Cats: c2(3), c3(5)

# Mais antigo geral: c2
assert shelter.dequeueAny() is c2

# Mais antigo geral: c3
assert shelter.dequeueAny() is c3

# Só resta d4
assert shelter.dequeueAny() is d4

assert shelter.isEmpty()