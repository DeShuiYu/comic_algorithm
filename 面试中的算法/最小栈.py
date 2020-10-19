

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


class MinStack():
    def __init__(self):
        self.mainStack = Stack()
        self.minStack = Stack()

    def push(self,element:int):
        self.mainStack.push(element)

        if self.minStack.isEmpty() or element <= self.minStack.peek():
            self.minStack.push(element)
    def pop(self) -> int:
        if self.mainStack.peek() == self.minStack.peek():
            self.minStack.pop()
        return self.mainStack.pop()

    def getMin(self):
        if self.mainStack.isEmpty():
            raise Exception("stack is empty")
        return self.minStack.peek()

if __name__ == "__main__":
    stack = MinStack()
    stack.push(4)
    stack.push(9)
    stack.push(7)
    stack.push(3)
    stack.push(8)
    stack.push(5)

    print(stack.getMin()) # 3

    stack.pop()
    stack.pop()
    stack.pop()

    print(stack.getMin()) # 4

