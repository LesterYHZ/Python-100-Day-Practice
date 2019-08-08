"""
Class Defination
"""
class Student(object):
	# __init__ is for initialization when creating the object
	# using this method, we are able to have two properties for
	# student object
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def study(self,course_name):
		print('%s is studying %s. ' % (self.name, course_name))
	
	def watch_movie(self):
		if self.age < 18:
			print('%s is watching Spider-Man. ' % self.name)
		else:
			print('%s is clearly mature enough to watch some FOW Studio Animation hehehe.' % self.name)
	
	# __ means that this property is private and therefore 
	# we have access to it only inside the class
	# But in most cases, we prefer to have the properties to be public
	# rather than private
	def __bar(self):
		print("__bar")		

"""
After defining a class, we can now create an object
"""
def main():
	# Create a student object with specific name and age
	stu1 = Student('Hana Song', 19)
	# Send message to the object
	stu1.study('StarCraft')
	stu1.watch_movie()
	
	stu2 = Student('Dora', 10)
	stu2.study('Trash')
	stu2.watch_movie()

"""
Main
"""
if __name__ == '__main__':
	main()


			