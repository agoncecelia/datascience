#Function with no argument and no Return value
def greeting():
  print("Hello world")

greeting()

#Function with no argument and with Return value
def return_greeting():
  return "Hello there"

print(return_greeting())

#Python Function with argument and No Return value
def greet_with_name(name):
  print("Hello " + name)

greet_with_name("Agon")

#Function with argument and Return value
def sum_two_numbers(a, b):
  return a + b

vlera = sum_two_numbers(5,6)
print(vlera)
