class StackNode:
    '''
    Representation of a node in a singly-linked list
    '''
    def __init__(self, data = None, prev = None):
        self.__data = data
        self.__prev = prev
        
    def __str__(self):
        return str(self.__data)

    def __repr__(self):
        return "StackNode containing " + str(self.__data)
    
    def getData(self):
        return self.__data
    
    def setData(self, data):
        self.__data = data
        
    def getPrev(self):
        return self.__prev
    
    def setPrev(self, node):
        self.__prev = node

        
    
class Stack:
        """
        Representation of a stack
        """
        def __init__(self):
            self.__head = None

        def __repr__(self):
            return "It's a stack!"
        
        def __str__(self):
            return "Stack"
        
        def getHead(self):
            return self.__head

        def isEmpty(self):
            if self.__head is None:
                return True
            
        def push(self, node):
            if self.__head is None:
                self.__head = node
            else:
                node.setPrev(self.__head)
                self.__head = node

        def pop(self):
            popItem = self.getHead()
            if self.__head.getPrev() is None:
                    self.__head = None
            else: 
                self.__head = self.__head.getPrev()
            return popItem

        def peek(self):
            if self.__head is None:
                return self.__head
            else:
                return self.__head.getData()

        def add(self, otherStack):
            while otherStack.getHead() is not None:
                tempNode = otherStack.pop()
                #print(tempNode)
                self.push(tempNode)

        def __contains__(self, searchnode):
            if self.__head is not None:
                #n = 0
                tempStack = Stack()
                while searchnode != self.__head:
                    #print(n)
                    #n = n+1
                    tempNode = self.pop()
                    print(tempNode)
                    tempStack.push(tempNode)
                    #tempStack.cheatDisplay()
                    if self.__head is None:
                        self.add(tempStack)
                        return False
                self.add(tempStack)
                return True
            else:
                return False

        def cheatDisplay(self):
            pos = self.getHead()
            while pos is not None:
                print(pos.getData())
                pos = pos.getPrev()
            
        def destroy(self):
            self.__head = None

stack = Stack()
thing = StackNode("thing")
thing2 = StackNode("thing2")
thing3 = StackNode("thing3")
stack.push(thing)
stack.push(thing2)
stack.push(thing3)

otherStack = Stack()
thing4 = StackNode("thing4")
thing5 = StackNode("thing5")
thing6 = StackNode("thing6")
otherStack.push(thing4)
otherStack.push(thing5)
otherStack.push(thing6)
