import shelve


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
		
		db = shelve.open('StudentdB')
		
		# get the current student number from the StudentdB
		studentNumber = len(db)
		
		# create an instance of user, which will be stored into the Student dB
		newStudent = user(str((self.studentNumber + 1), self.password))
		
		# 
		db[newStudent.username] = newStudent
		db.close
		
	def studentLogin(self, inStudentNumber, inPassword):
		"""Allow the student to login, if the login credentials are correct"""
		db = shelve.open('StudentdB')
		
		try:
			studentPassword = db[str(inStudentNumber)]
			
			if inPassword == studentPassword:
				# if the password passed matches the one in the dB, then allow the student to login
				return True
				
				
		except KeyError:
			return "Login information was incorrect"
		
		db.close
		
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
		
		db = shelve.open('TutordB')
		
		# get the current student number from the TutordB
		tutorNumber = len(db)
		
		# create an instance of user, which will be stored into the Tutor dB
		newTutor = user(str((self.tutorUsername + 1), self.password))
		
		# 
		db[newTutor.username] = newTutor
		db.close
		
	def studentLogin(self, inStudentNumber, inPassword):
		"""Allow the tutor to login, if the login credentials are correct"""
		db = shelve.open('TutordB')
		
		try:
			tutorPassword = db[str(inTutorNumber)]
			
			if inPassword == inTutorNumber:
				# if the password passed matches the one in the dB, then allow the tutor to login
				return True
				
				
		except KeyError:
			return "Login information was incorrect"
		
		db.close
		
	def __str__(self):
		print("Tutor Username is: " + str(self.tutorUsername) + "\nPassword is: " 
		+ str(self.password))
		