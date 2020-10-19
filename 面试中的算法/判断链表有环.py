class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def isCycle(head:Node):
    '''
    判断是否有环
    '''
    p1 = head
    p2 = head
    while p2 != None and p2.next != None:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            return (p1,True)
    return (None,False)

def cycleLength(head:Node):
    '''
    判断环的长度
    '''
    step = 0
    meet,_ = isCycle(head)
    if meet != None:
        p1,p2 = meet,meet
        while p2 !=Node and p2.next != Node:
            p1 = p1.next
            p2 = p2.next.next
            step += 1
            if p1 == p2:
                break
    return step

def cycleInput(head:Node):
    '''
    判断环的入点
    '''
    meet,_ = isCycle(head)
    if meet != None:
        p1,p2 = head,meet
        while p2 != None:
            p1 = p1.next
            p2 = p2.next
            if p1 == p2:
                return p1
    return None

def create():
    node5 = Node(5)
    node3 = Node(3)
    node7 = Node(7)
    node2 = Node(2)
    node6 = Node(6)
    node8 = Node(8)
    node1 = Node(1)

    node5.next = node3
    node3.next = node7
    node7.next = node2
    node2.next = node6
    node6.next = node8
    node8.next = node1
    node1.next = node2

    return node5
if __name__ == "__main__":

    head = create()
    
    _,iscycle = isCycle(head)
    print(iscycle)

    print(cycleLength(head))

    print(cycleInput(head).data)