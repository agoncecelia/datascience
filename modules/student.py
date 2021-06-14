class Student:
    def __init__(self, name, lastname, average):
        self.name = name
        self.lastname = lastname
        self.average = average

    def get_average(self):
        return self.average