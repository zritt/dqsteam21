from tkinter import *
from tkinter import messagebox
import shelve
from csv import *


class user():
	
	def __init__(self):
		self.username = ""
		self.password = ""
	
	
	def createNewUser(self, inUsername, inPassword):
		self.username = inUsername
		self.password = inPassword
		
		db = shelve.open('usersdb')
		usersCount = len(db)
		newUser = user
		