import csv

class User():
	
	def __init__(self, inNumber, inPassword):
		self.username = inNumber
		self.password = inPassword
	
	def __str__(self):
		print("Username is: " + str(self.username) + "\npPassword is: " + str(self.password))
	
		
class Student():
	"""Object to store Student User information, create a new Student and let them login"""
	
	def __init__(self, inStudentNumber, inPassword):
		self.studentUsername = inStudentNumber
		self.password = inPassword
	
	def createNewStudent(self, inStudentNumber, inPassword):
		"""Add a new a student to the dB, using their student number as a key in the dB"""
		pass
		
	def studentLogin(self, inStudentNumber, inPassword):
		"""Allow the student to login, if the login credentials are correct"""
		"""
		>>> studentLogin("000", "password")
		true
		"""
                with open('students.csv', 'rb') as csvfile:
                        linereader = csv.reader(csvfile)
                        next()
			for line in linereader:
                                if str(inStudentNumber) == line[0]:
                                        if str(inPassword) == line[2]:
                                                return true
                return false
		
		
	def __str__(self):
		print("Student Username is: " + str(self.studentUsername) + "\nPassword is: " 
		+ str(self.password))

		
class Tutor():
	"""Object to store Tutor User information, create a new Tutor and let them login """
	
	def __init__(self, inTutorNumber, inPassword):
		self.tutorUsername = inTutorNumber
		self.password = inPassword
	
	def createNewTutor(self, inTutorNumber, inPassword):
		"""Add a new a tutor to the dB, using their tutor number as a key in the dB"""
		
		pass
		
	def tutorLogin(self, inTutorNumber, inPassword):
		"""Allow the tutor to login, if the login credentials are correct"""
		with open('tutors.csv', 'rb') as csvfile:
                        linereader = csv.reader(csvfile)
                        next()
			for line in linereader:
				if str(inTutorNumber) == line[0]:
					if str(inPassword) == line[2]:
						return true
		return false
		
	def __str__(self):
		print("Tutor Username is: " + str(self.tutorUsername) + "\nPassword is: " 
		+ str(self.password))
		
