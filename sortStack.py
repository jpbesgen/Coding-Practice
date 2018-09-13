class Stack: 
	
	def __init__(self):
		self.items = []

	def isEmpty(self): 
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)


def sortStack(stack):
	if not stack.isEmpty(): 
		temp = stack.pop()
		sortStack(stack)
		sortedInsert(stack, temp)

def sortedInsert(stack, elem):
	if (stack.isEmpty() or elem > stack.peek()):
		stack.push(elem)
	else:
		temp = stack.pop()
		sortedInsert(stack, elem)
		stack.push(temp)


s = Stack() 
s.push(1)
s.push(-5)
s.push(-2)
s.push(8)
s.push(7)
s.push(15)
s.push(0)
s.push(-14)

print("Unsorted: ", s.items)
sortStack(s)
print("Sorted: ", s.items)

