"""Implement Queue using Stacks"""

class Node:
    """class Node"""
    def __init__(self, item, next=None):
        """Function init"""
        self.item = item
        self.next = next

class Stack:
    """class Stack"""
    def __init__(self):
        """Function init"""
        self.head = None

    def empty(self):
        """Function checks if the stack is empty"""
        if self.head is None:
            return True
        return False

    def push(self, item):
        """Function adds el to the end"""
        self.head = Node(item, self.head)

    def pop(self):
        """Function deletes the last el"""
        item = self.head.item
        self.head = self.head.next
        return item

    def peek(self):
        """Function reterns the last el"""
        return self.head.item

class MyQueue:
    """class MyQueue"""

    def __init__(self):
        """Function init"""
        self.in_stack = Stack()
        self.out_stack = Stack()

    def push(self, x: int) -> None:
        """Function adds el to the end"""
        self.in_stack.push(x)

    def pop(self) -> int:
        """Function deletes the first el"""
        if self.out_stack.empty():
            while not self.in_stack.empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()


    def peek(self) -> int:
        """Function returns the first el"""
        if self.out_stack.empty():
            while not self.in_stack.empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.peek()


    def empty(self) -> bool:
        """Function queue if the stack is empty"""
        if self.in_stack.empty() and self.out_stack.empty():
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
