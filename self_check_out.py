class SelfCheckOutHandler:

	def __init__(self, employee):
		self.__ready = True
		self.__currCheck = Check()
		self.__helper = employee

	def startNewCheck(self, customer):
		self.__currCheck = Check()

	def printCurrPrice(self):
		print (self.__currCheck.getTotalPrice())

	def printCurrProductList(self):
		print (self.__currCheck.getAllProduct())

	def checkOut(self, payment):
		self.printCurrProductList()
		self.printCurrPrice()
		if payment >= self.__currCheck.getTotalPrice():
			print ("your change is " + (payment - self.__currCheck.getTotalPrice()))
			print ("Check out Completed, Thank You.")
		else:
			print ("you don't have sufficient payment\nplease try again")

	def addProduct(self, product):
		self.__currCheck.addProduct(product)

	def removeProduct(self, product):
		if self.__helper.checkRemoveProduct(product):	self.__currCheck.removeProduct(product)

	def requestHelp(self):
		self.__helper.HelpCustomer()

	def changeEmployee(self, employee):
		self.__helper = employee

class Check:

	def __init__(self):
		self.__totalPrice = 0
		self.__productList = []
	
	def getTotalPrice(self):
		sum = 0
		for product in self.__productList:
			sum += product.price
		return sum

	def getAllProduct(self):
		return self.__productList

	def addProduct(self, product):
		self.__productList.append(product)

	def removeProduct(self):
		self.__productList.remove(product)


class Employee:

	def __init__(self, ID, name, age):
		self.__ID = ID
		self.__name = name
		self.__age = age

	def HelpCustomer(self):
		return 

	def checkRemoveProduct(self, product):
		if product:
			return True
		return False

class Product:

	def __init__(self, name, price):
		self.name = name
		self.price = price