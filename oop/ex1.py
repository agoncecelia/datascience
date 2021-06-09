class Person:
  def __init__(self, name, lastname, dob, email):
    self.name = name
    self.lastname = lastname
    self.dob = dob
    self.email = email

  def eat(self):
    return "{} is eating.".format(self.name)
  def walk(self):
    return "{} is walking.".format(self.name)
  def sleep(self):
    return "{} is sleeping.".format(self.name)

agoni = Person("Agon", "Cecelia", "19/05/1993", "agonn.c@gmail.com")

print(agoni.eat())
print(agoni.walk())
print(agoni.sleep())
