class Student():

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def name(self):
        return self.name

    def grade(self):
        return self.grade

    def greeting(self):
        return "I'm {} and I'm in grade {}".format(self.name, self.grade)

s = Student("Shelby", 6)
print(s.name)

"""
assert s.name == "Shelby"
assert s.grade == 6
assert s.greeting() == "I'm Shelby and I'm in grade 6"

s = Student("Maurice", 8)
assert s.name == "Maurice"
assert s.grade == 8
assert s.greeting() == "I'm Maurice and I'm in grade 8"

print("PASSED ALL")
"""