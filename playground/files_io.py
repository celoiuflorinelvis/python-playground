
import json

strJson = json.dumps(dict(name="Mary", age=34))
print(f"JSON = {strJson}")

f = open("data_single.json", "w", encoding="UTF-8")
f.write(strJson)
f.close()

f = open("data.json", "r")
data = f.read()
f.close()

print(f"data.json read: {data}")
print(f"data.json closed: {f.closed}")


print("Read lines: ")
f = open("data.json", "r")

line = ";"
while line:
    line = f.readline()
    print(f"Line = {line}")

f.close()


print("Read all lines: ")
f = open("data.json", "r")

lines = f.readlines()
print(f"Lines = {lines}")

f.close()

