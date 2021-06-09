class Person:

  def __init__(self, name, last_name, age):
    self.name = name
    self.last_name = last_name
    self.age = age

  def birthday(self):
    self.age = self.age + 1


class Staff(Person):
  def get_paid(self):
    return "{} got paid today".format(self.name)

driloni = Person("Drilon", "hajrullahu", 10)
print(driloni.get_paid())
agoni = Staff("Agon", "Cecelia", 10)
print(agoni.get_paid())
