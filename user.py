import csv

class User():
	
	def __init__(self, inNumber, inPassword):
		self.username = inNumber
		self.password = inPassword
	
	def __str__(self):
		print("Username is: " + str(self.username) + "\npPassword is: " + str(self.password))
	
		
class Student():
	"""Object to store Student User information, create a new Student and let them login"""
	
	def __init__(self, inStudentNumber, inPassword, inUsername, inFirstname, inLastname):
		self.studentUsername = inStudentNumber
		self.password = inPassword
		self.username = inUsername
		self.firstname = inFirstname
		self.lastname = inLastname
	
	def createNewStudent(self, inStudentNumber, inPassword, inUsername, inFirstname, inLastname):
		"""Add a new a student to the dB, using their student number as a key in the dB"""
		
		with open('students.csv', 'a') as csvfile:
			# We are going to write an entire record into the csv file (append it)
			linewriter = csv.writer(csvfile, delimiter=',', quotechar='"', 
			quoting=csv.QUOTE_MINIMAL)
			
			# append the record to the csv file
			linewriter.writerow([str(self.studentUsername), self.password, self.username, 
			self.firstname, self.lastname])
			
		
	def studentLogin(self, inStudentNumber, inPassword):
		"""Allow the student to login, if the login credentials are correct
		
		>>> Student.studentLogin(Student, "000", "password")
		True
		"""
		
		with open('students.csv', 'r') as csvfile:
			# place all the contents of the csv file into linereader
			linereader = csv.reader(csvfile)
			
			# skip the header 
			next(linereader)
			
			# iterate over the records, and then access each element in the record
			for line in linereader:
				if str(inStudentNumber) == line[0]:
					if str(inPassword) == line[2]:
						return True
		return False
		
		
	def __str__(self):
		print("Student Username is: " + str(self.studentUsername) + "\nPassword is: " 
		+ str(self.password))

		
class Tutor():
	"""Object to store Tutor User information, create a new Tutor and let them login """
	
	def __init__(self, inTutorNumber, inPassword, inUsername, inFirstname, inLastname):
		self.tutorUsername = inTutorNumber
		self.password = inPassword
		self.username = inUsername
		self.firstname = inFirstname
		self.lastname = inLastname
	
	def createNewTutor(self, inTutorNumber, inPassword, inUsername, inFirstname, inLastname):
		"""Add a new a tutor to the dB, using their tutor number as a key in the dB"""
		with open('tutors.csv', 'a') as csvfile:
			# We are going to write an entire record into the csv file (append it)
			linewriter = csv.writer(csvfile, delimiter=',', quotechar='"', 
			quoting=csv.QUOTE_MINIMAL)
			
			# append the record to the csv file
			linewriter.writerow([str(self.tutorUsername), self.password, self.username, 
			self.firstname, self.lastname])
		
	def tutorLogin(self, inTutorNumber, inPassword):
		"""Allow the tutor to login, if the login credentials are correct
		
		>>> Tutor.tutorLogin(Tutor, "000", "password")
		True
		"""

		with open('tutors.csv', 'r') as csvfile:
			# place all the contents of the csv file into linereader
			linereader = csv.reader(csvfile)
			
			# skip the header 
			next(linereader)
			
			# iterate over the records, and then access each element in the record
			for line in linereader:
				if str(inTutorNumber) == line[0]:
					if str(inPassword) == line[2]:
						return True
		return False
		
		
	def __str__(self):
		print("Tutor Username is: " + str(self.tutorUsername) + "\nPassword is: " 
		+ str(self.password))

		
# for testing purposes		
if __name__ == "__main__":
    import doctest
    doctest.testmod()
