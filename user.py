import csv

class User():
	
	def __init__(self, inNumber, inPassword):
		self.username = inNumber
		self.password = inPassword
	
	def __str__(self):
		print("Username is: " + str(self.username) + "\npPassword is: " + str(self.password))
	
		
class Student():
	"""Object to store Student User information, create a new Student and let them login"""
		
	def createNewStudent(self,inUsername , inPassword, inFirstname, inLastname):
		"""Add a new a student to the dB, using their student number as a key in the dB"""
		
		with open('students.csv', 'a+') as csvfile:
			# We are going to write an entire record into the csv file (append it)
			linewriter = csv.writer(csvfile, delimiter=',', quotechar='"', 
			quoting=csv.QUOTE_MINIMAL)
			
			self.username = inUsername
			self.password = inPassword
			self.firstname = inFirstname
			self.lastname = inLastname
			
			self.studentNumber = self.count_row()
			
			# append the record to the csv file
			linewriter.writerow([int(self.studentNumber), self.username, self.password, 
			self.firstname, self.lastname])
			
	def count_row(self):
		with open('students.csv', 'r') as csvfile:
			linereader = csv.reader(csvfile)
			row_count = sum(1 for line in linereader)
			return row_count - 1
	
	def studentLogin(self, inStudentNumber, inPassword):
		"""Allow the student to login, if the login credentials are correct
		
		>>> Student.studentLogin(Student, 0, "password")
		True
		"""
		
		with open('students.csv', 'r') as csvfile:
			# place all the contents of the csv file into linereader
			linereader = csv.reader(csvfile)
			
			# skip the header 
			next(linereader)
			
			# iterate over the records, and then access each element in the record
			for line in linereader:
				if str(inStudentNumber) == str(line[0]):
					if str(inPassword) == str(line[2]):
						return True
		return False
		
		
class Tutor():
	"""Object to store Tutor User information, create a new Tutor and let them login """
	
	
	def createNewTutor(self,inUsername , inPassword, inFirstname, inLastname):
		"""Add a new a student to the dB, using their student number as a key in the dB"""
		
		with open('tutors.csv', 'a+') as csvfile:
			# We are going to write an entire record into the csv file (append it)
			linewriter = csv.writer(csvfile, delimiter=',', quotechar='"', 
			quoting=csv.QUOTE_MINIMAL)
			
			self.username = inUsername
			self.password = inPassword
			self.firstname = inFirstname
			self.lastname = inLastname
			
			self.tutorNumber = self.count_row()
			
			# append the record to the csv file
			linewriter.writerow([int(self.tutorNumber), self.username, self.password, 
			self.firstname, self.lastname])
			
	def count_row(self):
		with open('tutors.csv', 'r') as csvfile:
			linereader = csv.reader(csvfile)
			row_count = sum(1 for line in linereader)
			return row_count - 1
	
	def tutorLogin(self, inTutorNumber, inPassword):
		"""Allow the student to login, if the login credentials are correct
		
		>>> Tutor.tutorLogin(Tutor, 0, "password")
		True
		"""
		
		with open('tutors.csv', 'r') as csvfile:
			# place all the contents of the csv file into linereader
			linereader = csv.reader(csvfile)
			
			# skip the header 
			next(linereader)
			
			# iterate over the records, and then access each element in the record
			for line in linereader:
				if str(inTutorNumber) == str(line[0]):
					if str(inPassword) == str(line[2]):
						return True
		return False
		
		
			
	
# def run():
	# student_1 = Student()
	# student_1.createNewStudent('test', 'password', 'testFName', 'TestLName')
		
# for testing purposes		
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #run()
