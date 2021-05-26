fruits = ["Apple", "Orange", "Cherry"]
fruits_tuple = ("Apple", "Orange", "Cherry")

# for loops
for x in fruits:
  print(x + " is delicoous")

# while loops
counter = 0
while counter < len(fruits):
  print(fruits[counter] + " is delicious")
  counter += 1

# Reverse a list
fruits.reverse()
print(fruits)

print(fruits)
print(fruits[0])

fruits.append("Banana")
print(fruits)

fruits.insert(1, "Cranberry")
print(fruits)

fruits.remove("Banana")
print(fruits)
fruits.pop()
print(fruits.pop(0))
print(fruits)


# Tuples don't change.
print(fruits_tuple)
