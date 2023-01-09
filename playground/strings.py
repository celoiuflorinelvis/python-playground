import math


text = """
This is 
        a
    multiline string.
"""

print(text)

print('Length: %(length)d\n' %{'length': len(text)})
print('Name: {0}, Age: {1}'.format("John", 23))

print("Substring text[1:10] = ", text[1:10])
print("text[-len(text):-len(text) + 4] = ", text[-len(text) + 1 : -len(text) + 4])

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
msg = f"{yes_votes:-10} YES votes / {percentage:3.3%} NO votest"
print(msg)
print(f"Debugging {yes_votes=}, {no_votes=}")

print(repr( [1, 2, ("a", "b", 4)] ))
print( repr( "Hello \n" ) )
print( repr( dict(name="Mary", age=23) ) )

print(str( math.pi ) + "sss")
print(str('Hello \n'))

for x in range(1, 11):
    #print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))

print(repr(math.pi).zfill(20))




