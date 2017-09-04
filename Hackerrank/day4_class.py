class Person:
    def __init__(self,initialAge):
            self.int = initialAge

    def amIOld(self):
        if self.int < 0:
            print( "Age is not valid, setting age to 0.")
            self.int = 0
        if self.int < 13:
            print("You are young.")
        elif self.int < 18:
            print("You are a teenager.")
        else: print("You are old.")

    def yearPasses(self):
        self.int += 1
        return self.int

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
