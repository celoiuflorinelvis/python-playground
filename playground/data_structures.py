from collections import deque


# Lists / Stacks
stack  = []
stack.append(1)
stack.append(2)
stack.append(3)
print(f"stack = {stack}")

print(stack.pop())
print(stack.pop())
print(f"stack = {stack}")


# Queues
print()
queue = deque([1, 2, 3])
print(f"queue = {queue}")

print(queue.popleft())
print(queue.popleft())
print(f"queue = {queue}")

queue.appendleft(4)
print(f"queue = {queue}")

queue.append(5)
print(f"queue = {queue}")


# List Comprehesion 
#squares = list(map( lambda x: x ** 2, range(10) ))
squares  = [(x, x ** 2) for x in range(10)]
print(f"squares = {squares}")


matrix = [ [j for j in range( i * 4 + 1, i * 4 + 5 )] for i in range(4) ]
print(f"matrix = {matrix}")

for row in matrix:
    print(f"row = {row}")

tranposed = [ [ row[i] for row in matrix ] for i in range(4) ]
print(f"transposed = {tranposed}")


# del
list = [1,2,3,4,5]
print(f"list={list}")

del list[2:4]
print(f"list={list}")


# Sets
a = set('abracadabra')
b = set('alacazam')

print(f"l in b {'l' in b}")
print(f"a - b = {a - b}")
print(f"a & b = {a & b}")
print(f"a ^ b = {a ^ b}")
print(f"a | b = {a | b}")

c = {x for x in 'abracadraba' if x not in 'abc'}
print(f"c = {c}")


# Dictionaries
ages = {"John": 42, "Mary": 23, "Joana": 12}
print(f"Age of Jhon is {ages['John']}")

#sorted_ages = sorted(ages)
sorted_ages = sorted(ages, key = lambda k: ages[k])
#sorted_ages_values = list( map( lambda k: ages[k], sorted_ages ) ) ????
sorted_ages_values = [ages[k] for k in sorted_ages]
print(f"sorted ages: {sorted_ages} map ages {sorted_ages_values}")

del ages["Mary"]
print(f"del ages {ages}")

print(f"John is in dictionare? : {'John' in ages}")
print(f"Mary is not in dictionare? : {'Mary' not in ages}")

squares = {x: x ** 2 for x in (1, 2, 3, 4) }
print(f"Squares: {squares}")

#tel = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
tel = dict(sape=4139, guido=4127, jack=4098)
print(f"tel. = {tel}")

for index, value in enumerate(["Jhon", "Mary", "Jane"]):
    print(f"{index + 1}. {value}")

numbers = [x for x in range(10) if x % 2 == 0]
print(f"numbers = {numbers}")
squares = [y ** 2 for y in numbers]
print(f"squares = {squares}")

for number, square in zip(numbers, squares):
    print(f"{number}^2 = {square}")







