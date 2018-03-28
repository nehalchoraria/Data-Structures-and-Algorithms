class Tree:
	def __init__(self,initvalue = None):
		
		self.value = initvalue
		
		if initvalue!=None:
			self.right = Tree()
			self.left = Tree()
		else:
			self.right = None
			self.left = None

		return

	def isEmpty(self):
		return self.value == None

	def inOrder(self):

		if self.value == None:
			return []

		return self.left.inOrder() + [self.value] + self.right.inOrder()

	def find(self,findValue):

		if self.isEmpty():
			return False

		if self.value == findValue:
			return True

		if findValue < self.value:
			self.left.find(findValue)
		else:
			self.right.find(findValue)

	def insert(self,inputValue):

		if self.isEmpty():
			self.value = inputValue
			self.right = Tree()
			self.left = Tree()

		if self.value == inputValue:
			return

		if inputValue > self.value:
			self.right.insert(inputValue)
			return
		else:
			self.left.insert(inputValue)
			return	

v = Tree(50)
v.insert(2)	
v.insert(20)	
v.insert(56	)
v.insert(76)	
v.insert(1)	
v.insert(45)	
v.insert(23)	
print( v.inOrder() )	