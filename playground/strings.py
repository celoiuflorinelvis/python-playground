
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
