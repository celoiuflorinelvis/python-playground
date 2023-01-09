from enum import Enum


#inputTxt = int(input("Enter a number: "))
inputTxt = 1

if inputTxt > 0:
    print("Greater then zero")
elif inputTxt == 0:
    print("Equals to 0")
else:
    print("Negative number")

words = ["john", "apples", "red", "green"]
print(words[2:4])

for word in words:
    print('{0} - {1}'.format(word, len(word)))

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

active_users = []
for user, status in users.items():
    if status == 'active':
        print(user)
        active_users.append(user)
print("Active users: {}".format(active_users))

print("Sum.(10) = {}".format(sum(range(10))))

for i in range(1,3):
    print("{}. {}".format(i, words[i]))

class EmptyClass:
    pass

def emptyMethod(arg):
    pass


def http_errors(error):
    match error:
        case 200 | 201 | 202:
            return "Object Created"
        case 400:
            return "Bad request"
        case 404:
            return "Not Found"
        case _:
            return "Other error"

print("{} - {}".format(202, http_errors(202)))
print(f"201 - {http_errors(201)}")
print("{} - {}".format(400, http_errors(400)))
print("{} - {}".format(404, http_errors(404)))
print("{} - {}".format(500, http_errors(500)))


def tuple(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y = {y}")
        case (x, 0):
            print(f"X = {x}")
        case (x, y):
            print(f"X = {x}, Y = {y}")
        case _:
            raise ValueError("Not a point")
tuple((0, 0))
tuple((0, 1))
tuple((2, 0))
tuple((1, 2))
#tuple("error")

class Point:
    x: int
    y: int    
    #def __init__(self, x=None, y=None):
    #    self.x = x
    #    self.y = y

def where_is(point):
    match point:
        case Point(x = 0, y = 0):
            print("Origin")
        case Point(x=0, y = y):
            print(f"Y = {y}")
        case Point(x=x, y=0):
            print(f"X = {x}")
        case Point(x=x, y=y):
            print(f"X = {x}, Y = {y}")
        case Point():
            print("No point")
        case _:
            raise ValueError("Not a point")

print("\nPoints:\n")
where_is(Point())

point = Point()
point.x = 0
point.y = 0
where_is(point)

point = Point()
point.x = 2
point.y = 1
where_is(point)

#where_is(Point(x=0, y=1))
#where_is(Point(0, 1))
#where_is(Point(2, 0))
#where_is(Point(1, 2))
#where_is("error")


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

color = Color("red")
match color:
    case Color.RED:
        print("Rosiu")
    case Color.GREEN:
        print("Verde")
    case _:
        print("XXX")


def method(kind, sex = "M", *args, **kewords):
    print(f"Kind = {kind}")
    print(f"Sex = {sex}")
    
    print("-" * 40)
    for arg in args:
        print(f"Arg = {arg}")
    
    print("-" * 40)
    for kw in kewords:
        print(f"{kw} = {kewords[kw]}")
print("\n\n")
method('type', "F", "aaa", 123, 
    age = 12,
    name = "John"
)
print("#" * 40)
method('type', "aaa", 123, 
    age = 12,
    name = "John"
)


def method_parameters(pos1, pos2, /, pos_and_kw, *, kw1, kw2):
    print(f"pos1 = {pos1}")
    print(f"pos2 = {pos2}")
    print(f"pos_and_kw = {pos_and_kw}")
    print(f"kw1 = {kw1}")
    print(f"kw2 = {kw2}")

print()
method_parameters(1, 2, "pos and kw", kw1 = "par1", kw2 = "kw2")
#method_parameters(1, pos1 = 2, "pos and kw", kw1 = "par1", kw2 = "kw2")
method_parameters(1, 2, pos_and_kw = "pos and kw", kw1 = "par1", kw2 = "kw2")
#method_parameters(1, 2, pos_and_kw = "pos and kw",  "par1", kw2 = "kw2")

def build_incrementer(n):
    return lambda x: x + n

incr10 = build_incrementer(10)
print(f"x + 10 = {incr10(3)}")

pairs = [(3, "three"), (1, "one"), (2, "two")]
pairs.sort(key = lambda pair: pair[0])
print(f"pairs = {pairs}")


