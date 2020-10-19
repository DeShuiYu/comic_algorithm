class Node:


    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.pre:Node = None
        self.next:Node = None

class LRUCache:
    def __init__(self,limit:int):
        self.head = Node(None,None)
        self.end = Node(None,None)
        self.limit = limit
        self.hashMap = dict()

        # print(type(self.head))


    def get(self,key:str) -> str:
        node:Node = self.hashMap[key]
        if node == None:
            return None

        self.refreshNode(node)

        return node.value

    def  put(self,key:str,value:str):
        node = self.hashMap.get(key)
        if node == None:
            if len(self.hashMap) >= self.limit:
                oldKey = self.removeNode(self.head)
                self.hashMap.pop(oldKey)

            self.addNode(Node(key,value))
            self.hashMap[key] = node
        else:
            node.value = value
            self.refreshNode(node)

    def remove(self,key:str):
        node = self.hashMap[key]
        self.removeNode(node)
        self.hashMap.pop(key)

    def refreshNode(self,node):
        if node == end:
            return None
        self.removeNode(node)
        self.addNode(node)

    def removeNode(self,node:Node):
        if node == self.head and node == self.end:
            self.head = None
            self.end = None
        elif node == self.end:
            self.end = self.end.pre
            self.end.next = None
        elif node == self.head:
            self.head = self.head.next
            print(type(self.head))
            self.head.pre = None
        else:
            node.pre.next = node.next
            node.next.pre = node.pre

        return node.key

    def addNode(self,node):
        if self.end != None:
            self.end.next = node
            node.pre = self.end
            node.next = None
        end = node
        if self.head == None:
            self.head = node


if __name__ == "__main__":
    lruCache = LRUCache(5)
    lruCache.put("001","用户1信息")
    lruCache.put("002","用户2信息")
    lruCache.put("003","用户3信息")
    lruCache.put("004","用户4信息")
    lruCache.put("005","用户5信息")

    lruCache.get("002")

    lruCache.put("004","用户4信息更新")
    lruCache.put("006","用户6信息")

    print(lruCache.get("001"))
    print(lruCache.get("006"))
    # a = {"1":2,"3":4}
    # print(a.get("4"))

    
