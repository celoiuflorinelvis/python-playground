
def scope_test():
    def do_local():
        spam = "Local value"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal value"

    def do_global():
        global spam
        spam = "global value"

    spam = "test spam"

    do_local()
    print("After local assignment:", spam)

    do_nonlocal()
    print("After nonlocal assignment:", spam)

    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

print("\n\n #### Complex numbers ###\n\n")
class Complex: 

    def __init__(self, realpart = 0, imagpart = 0) -> None:
        self.realpart = realpart
        self.imagpart = imagpart

    def add(self, complex_number):
        return Complex(self.realpart + complex_number.realpart, self.imagpart + complex_number.imagpart)

    def __str__(self) -> str:
        return f"{self.realpart} + {self.imagpart}*I"

print(f"4 + 2*i = {Complex(4, 3)}")

cc_no1 = Complex(4, 2)
cc_no2 = Complex(5, 3)
cc_sum = cc_no1.add(cc_no2)
print(f"Sum = {cc_sum}")
print(f"Complex no. {cc_sum.realpart} + {cc_sum.imagpart} * I")


print("\n\n #### Animals ###\n\n")
class Dog:
    kind = "canine"
    commonTricks = []
    
    def __init__(self, name) -> None:
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)
        self.commonTricks.append(trick)

    def __str__(self) -> str:
        return f"My name is {self.name}, my kind is {self.kind} and I know following common tricks {self.commonTricks} and own tricks {self.tricks}." 

dog_azoler = Dog("azorel")
dog_azoler.add_trick("roll over")
dog_molda = Dog("molda")
dog_molda.add_trick("play dead")

print(f"Azorel: {dog_azoler} / Molda: {dog_molda}")
dog_molda.kind = "cat"
dog_molda.commonTricks = []
dog_molda.add_trick("funny")
print(f"Azorel: {dog_azoler} / Molda: {dog_molda}")


print("\n\n #### Inheritance ###\n\n")
class Base:
    _prv_data = "private data"

    def method(self):
        print("Base")

class Base1(Base) :
    def method(self):
        print("Base1")
    def method_msg(self):
        print("Base1_Msg")

class Base2(Base) :
    def method(self):
        print("Base2")
    def method_msg(self):
        print("Base1_Msg")

class Derived(Base2, Base1):
    def method(self):
        print("Derived")

baseObj = Base()
baseObj.method()

base1Obj = Base1()
base1Obj.method()

base2Obj = Base2()
base2Obj.method()

derivedObj = Derived()
derivedObj.method()
derivedObj.method_msg()

print(f"InstanceOf Derived: {isinstance(derivedObj, Derived)}")
print(f"InstanceOf Base1: {isinstance(derivedObj, Base1)}")
print(f"InstanceOf Base2: {isinstance(derivedObj, Base2)}")
print(f"InstanceOf Base: {isinstance(derivedObj, Base)}")

print(f"IsSubclassOf Derived: {issubclass(Derived, Derived)}")
print(f"IsSubclassOf Base1: {issubclass(Derived, Base1)}")
print(f"IsSubclassOf Base2: {issubclass(Derived, Base2)}")
print(f"IsSubclassOf Base: {issubclass(Derived, Base)}")

print(f"Class Derived: {Derived.__class__}")
print(f"Class derivedObj: {derivedObj.__class__}")


print("\n\n #### dataclasses ###\n\n")

from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    salary: float

emp = Employee("Ion", 123.4)
print(f"Emp. name = {emp.name}; salary = {emp.salary}")
print(f"Employee: {emp}")


print("\n\n #### Iteratores ###\n\n")

try:
    it = iter('abcde')
    print(f"{next(it)}")
    print(f"{next(it)}")
    print(f"{next(it)}")
    print(f"{next(it)}")
    print(f"{next(it)}")
    print(f"{next(it)}")
    print(f"{next(it)}")
except StopIteration:
    print("Stop Iteraction")

class Reverse:
    def __init__(self, data) -> None:
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

for c in Reverse("abcdef"):
    print(f"Char: {c}")


print("\n\n #### Generators ###\n\n")

def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

for ch in reverse("abcdef"):
    print(f"{ch}", end=", ")
print("\n")

print(f"{sum(i * i for i in range(10))}")

xvec = [1, 2, 3]
yvec = [4, 5, 6]
print( sum(x * y for x, y in zip(xvec, yvec)) )

page = """
Some simple generators can be coded 
succinctly as expressions using a syntax 
similar to list comprehensions but with 
parentheses instead of square brackets
"""

unique_words = set(word for line in page.splitlines() for word in line.split())
print(f"Unique words: {unique_words}")



