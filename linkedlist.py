class Node:

	def __init__(self, dataval=None):

		self.dataval = dataval
		self.next = None
class LinkedList:

	def __init__(self):
		self.head = None


	def printlist(self):

		printval = self.head

		while printval is not None:
			print(printval.dataval)
			

			printval = printval.next

	def newAtBeg(self,newData):
		NewNode = Node(newData)

		NewNode.next = self.head

		self.head = NewNode

	def newAtEnd(self, newData):
		NewNode = Node(newData)

		if self.head is None:
			self.head = NewNode
			return

		Laste = self.head
		while Laste.next:
			Laste = Laste.next

		Laste.next = NewNode

	def newInBetween(self, middleNode, newData):
		

		if(middleNode == None):
			print("The node does not Exist")
			return

		NewNode = Node(newData)
		NewNode.next = middleNode.next
		middleNode.next = NewNode


	def removeByKey(self, key):

		headval = self.head
			
		if(headval is not None):
			if(headval.dataval == key ):

				self.head = headval.next
				headval = None

				return

		while headval is not None:

			if (headval.dataval == key):
				break

			prev = headval

			headval = headval.next

		if headval is None:
			return

		prev.next = headval.next
		headval = None














lis = LinkedList()

lis.head = Node("Monday")

n1 = Node("Wednesday")
n2 = Node("Thursday")

lis.head.next = n1

n1.next = n2

lis.printlist()

nd = input("Enter new Data at begining: ")
lis.newAtBeg(nd)

lis.printlist()

nd = input("Enter new data at last: ")

lis.newAtEnd(nd)
lis.printlist()

nd = input("Enter data at middle")

lis.newInBetween(lis.head.next, nd)

lis.printlist()

nd = input("Enter data you wanna remove: ")

lis.removeByKey(nd)

lis.printlist()
