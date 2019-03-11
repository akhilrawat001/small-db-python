'''
This is my SmallDB i.e. Small Database
'''
print('SmallDB imported succesfully!')

import json, words, os, api

def load(file_name = 'test.db',auto_dump = False):
		'''
		This function loads the file name given as 
		the argument to the function by creating
		an objext of the class smallDB, and then
		this functions returns the object
		'''
		smalldb = smallDB(file_name,auto_dump)
		smalldb.load_file()
		return smalldb


class smallDB():
	'''
	This is the main class
	The pupose of this class is to create 
	instances/objects of this class and 
	call methods on the created instances/objects
	'''
	

	file_name = ""
	jsonObject = {}
	jsonObject2 = {}

	def __init__(self, file_name,auto_dump):
		'''
		__init__ is a reseved method in python classes. 
		It is known as a constructor in object oriented 
		concepts. This method is called when an object 
		is created from the class and it initializes 
		an instance of a class or an object
		'''
		'''	
		self represents the instance of the class. 
		By using the "self" keyword we can access 
		the attributes and methods of the class
		'''
		self.file_name = file_name
		self.auto_dump = auto_dump


		

	def load_file(self):
		'''
		This function will load 
		the json data drom the file.
		'''
		print('Loading Database from {} ...'.format(self.file_name))
		if os.path.exists(self.file_name):
			content = open(self.file_name).read()
			if content != "":
				self.jsonObject = json.loads(content)
			else:
				self.jsonObject = {}
				content = open(self.file_name, 'w+').write(json.dumps(self.jsonObject))
		else:
			self.jsonObject = {}
			content = open(self.file_name, 'w+').write(json.dumps(self.jsonObject))

		print('Database loaded succesfully!')
		return self.jsonObject
	
	def dump(self):
		'''
		This function is for saving the files
		'''
		print('Dumping Database to {} ...'.format(self.file_name))
		open(self.file_name, 'w').write(json.dumps(self.jsonObject))
		print('***Changes Saved***')


	def set(self,key = 'key' ,value = 'value'):
		'''
		This function is for setting 
		a key,value pair in the file
		'''
		self.jsonObject[key] = value
		if self.auto_dump:
			self.dump()
		return self.jsonObject
		
	def get(self,key = 'key'):
		'''
		This function will return 
		the corresponding value of the
		key demanded by user.
		'''	
		if key in self.jsonObject:
			print(self.jsonObject[key])
		elif 'http' in key:
			print('Key Not Found\nBut adding the requested key-value pair')
			value = api.get_data(key)
			self.set(key,value)
		else:
			print('Key Not Found')
	def getAll(self):
		'''
		Returns a dict_keys of all the keys in the Database,
		if no keys are found then returns 'No Keys Found' 
		'''
		if len(self.jsonObject) != 0:
			return self.jsonObject.keys()
		else:
			return 'No Keys Found'
	def remKey(self,key):
		'''
		Removes a key from Database if 
		finds it else returns the DB as it is
		'''
		if key in self.jsonObject:
			self.jsonObject.pop(key)
			if self.auto_dump:
				self.dump()
			return self.jsonObject
		else:
			print('Key Not Found')
			return self.jsonObject
	def exists(self,key):
		'''
		If key exists in Database then this function
		returns True else it returns false
		'''
		return True if key in self.jsonObject.keys() else False

	def total_keys(self):
		'''
		Returns the total number of keys in our database
		'''
		return len(self.jsonObject)
	
	def del_db(self):
		'''
		Deletes Database and returns {}
		'''
		self.jsonObject = {}
		if self.auto_dump:
				self.dump()
		return self.jsonObject
	def random_insert(self,number = 0):
		'''
		Inserts random keys and values in our 
		Database number of key-value pairs 
		depend on the argument(number)
		''' 
		for num in range(number):
			entry = words.get_entry()
			self.jsonObject[entry[0]] = entry[1]
		if self.auto_dump:
				self.dump()
		return self.jsonObject
	def dbmerge(self,another_file = 'test.db'):
		if os.path.exists(another_file):
			content = open(another_file).read()
			if content != "":
				self.jsonObject2 = json.loads(content)
			else:	
				self.jsonObject2 = {}
				content = open(another_file, 'w+').write(json.dumps(self.jsonObject))
		else:
			self.jsonObject2 = {}
			content = open(another_file, 'w+').write(json.dumps(self.jsonObject2))
		print('Second Database loaded succesfully!')
		self.jsonObject.update(self.jsonObject2)
		if self.auto_dump:
				self.dump()
		return self.jsonObject


	
	
