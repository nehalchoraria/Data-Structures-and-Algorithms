class Node:
	def __init__(self,value=None):
		self.current = value
		self.next = None

	def isEmpty(self):
		return self.current == None

	def append(self,value):  #Adds towards the end of the list
		if self.current == None:
			self.current = value
			self.next = None
			return 
		else:
			newNode = Node(value)
			temp = self

			while temp.next != None :
				temp = temp.next

			temp.next = newNode
			return

	def viewList(self):
		temp = self
		while temp.next != None:
			print(temp.current,end=" ")
			temp = temp.next
		if temp.current != None:
			print(temp.current)

	def insert(self,value): #Adds towards the start of the list
		if self.isEmpty():
			self.current = value
			self.next = None
			return
		
		newNode = Node(value)

		self.current,newNode.current = newNode.current,self.current
		self.next,newNode.next = newNode,self.next

	def count(self):
		count = 0
		temp = self
		while temp.next != None:
			count = count + 1
			temp = temp.next
		if temp.current != None:
			count = count + 1

		return count


	def deleteNode(self,position):
		if position > self.count():
			return 
		else:	
			temp = self
			count = 0

			if position == 1:             #If first node
				temp.current = temp.next.current
				temp.next = temp.next.next
				return

			position = position - 1

			while temp.next != None:
				count = count + 1

				if count == position:
					temp.next = temp.next.next
					return

				temp = temp.next

	def length(self):
		if self.current == None:
			return 0
		elif self.next == None:
			return 1
		else:
			return self.next.length() + 1

v = Node(5)
v.insert(10)
v.insert(20)
v.insert(40)
v.append(25)
v.append(34)
v.append(95)
v.viewList()
v.deleteNode(5)
v.viewList()

print ( v.length() )