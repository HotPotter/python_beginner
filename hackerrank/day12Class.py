class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
	def __init__(self, firstName, lastName, idNumber, scores):
		#Person.__init__(self,firstName,lastName, idNumber)
		super().__init__(firstName,lastName,idNumber)
		self.scores = scores
	def calculate(self):
		total = sum(self.scores)/len(self.scores)
		if total >= 90:
			return "O"
		elif total >= 80:
			return "E"
		elif total >= 70:
			return "A"
		elif total >= 55:
			return "P"
		elif total >= 40:
			return "D"
		else:
			return "T"

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
