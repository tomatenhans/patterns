class Component:
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        print("Original!")

class Decorator(Component):
    def __init__(self, c: Component):
        self.c= c
    def operation(self):
        self.c.operation()

class DecoratorA(Decorator):
    def __init(self, c):
        super().__init__(c)

    def operation(self):
        print("extended before!")
        super().operation()

class DecoratorB(Decorator):
    def __init__(self, c):
        super().__init__(c)

    def operation(self):
        print("extended after!")

undec= ConcreteComponent()
#undec.operation()

decorated= DecoratorA(ConcreteComponent())
decorated.operation()
