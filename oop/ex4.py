class Person():
  def __init__(self, name, surname, dob, email):
    self.name = name
    self.surname = surname
    self.dob = dob
    self.email = email

class Staff(Person):
  def __init__(self, name, surname, dob, email, auth_id, role, c_exp_date):
    super().__init__(name, surname, dob, email)
    self.auth_id = auth_id
    self.role = role
    self.c_exp_date = c_exp_date

class Student(Person):
  def __init__(self,name, surname, dob, email, student_id, grade_avg):
    super().__init__(name, surname, dob, email)
    self.student_id = student_id
    self.grade_avg = grade_avg

agoni = Staff("Agon", "Cecelia", "19/05/1993", "agonn.c@gmail.com", "10033", "pastrues", "20/05/2023")
taulant = Student("Taulant", "Musa", "20/01/1997", "taulant_bukuroshi_podujeva@gmail.com", "1000007", 9.5)

print(agoni.name)
print(taulant.name)
print(taulant.grade_avg)
