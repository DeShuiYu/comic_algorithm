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

def removeKDigits(num:str,k:int)->None:
    newLength = len(num) - k
    stack = Stack()
    top = 0
    for i in range(len(num)):
        c = num[i]
        while not stack.isEmpty()  and  stack.peek() > c and k > 0:
            stack.pop()
            k -= 1
        stack.push(c)
    
    newString = ""
    while not stack.isEmpty():
        newString += stack.pop()
    newString = newString[::-1]
    offset = 0
    while offset < newLength and newString[offset] == '0':
        offset += 1
    return "0" if offset == newLength else newString[offset:]


if __name__ == "__main__":
    print(removeKDigits("1593212",3))
    print(removeKDigits("30200",1))
    print(removeKDigits("10",2))
    print(removeKDigits("541270936",3))
    