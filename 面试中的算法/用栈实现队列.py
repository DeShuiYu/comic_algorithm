class Stack:

    def __init__(self):
        self.items = []
    def isEmpty(self):
        return True if len(self.items) == 0 else False
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self):
        if self.isEmpty():
            raise Exception("栈为空")
        return self.items[self.size() - 1]

class StackQueue():
    def __init__(self):
        self.stackA = Stack()
        self.stackB = Stack()

    def enQueue(self,ele:int):
        self.stackA.push(ele)
    def deQueue(self):
        if self.stackB.isEmpty():
            if self.stackA.isEmpty():
                return None
            self.transfer()
        return self.stackB.pop()
    def transfer(self):
        while self.stackA.isEmpty() == False:
            self.stackB.push(self.stackA.pop())

            

if __name__ == "__main__":
    stackQueue = StackQueue()
    stackQueue.enQueue(1)
    stackQueue.enQueue(2)
    stackQueue.enQueue(3)

    print(stackQueue.deQueue())
    print(stackQueue.deQueue())

    stackQueue.enQueue(4)

    print(stackQueue.deQueue())
    print(stackQueue.deQueue())