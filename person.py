class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print("say")


john = Person("John")
print(john.name)
john.talk()