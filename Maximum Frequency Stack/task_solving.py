"""Maximum Frequency Stack"""
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

class FreqStack:
    """class FreqStack"""
    def __init__(self):
        """Function init"""
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        """Function increases how many times the value appears and puts it in the right stack"""
        if val not in self.freq:
            self.freq[val] = 0

        self.freq[val] += 1
        f = self.freq[val]

        if f > self.max_freq:
            self.max_freq = f

        if f not in self.group:
            self.group[f] = Stack()

        self.group[f].push(val)

    def pop(self) -> int:
        """Function returns and removes the value that appears most often"""
        val = self.group[self.max_freq].pop()

        self.freq[val] -= 1

        if self.group[self.max_freq].empty():
            self.max_freq -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
