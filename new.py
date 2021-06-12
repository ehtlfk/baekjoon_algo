# linked list?

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None
class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.current = None
        self.buffer = []
        self.nlist = None
        
    def set_current(self,n,k):
        self.nlist = [0]*n
        self.current = self.head
        for i in range(n):
            self.current.next = Node(i)
            tmp = self.current
            self.current = self.current.next
            self.current.next = self.tail
            self.tail.pre = self.current
            self.current.pre = tmp
        self.current = self.head
        for _ in range(k+1):
            self.current = self.current.next
            
        
    def delete(self):
        if self.current.next == self.tail:
            self.buffer.append(self.current)
            tmp = self.current.pre
            tmp.next = self.tail
            self.tail.pre = tmp
            self.current = tmp
            return
        if self.current.pre == self.head:
            self.buffer.append(self.current)
            tmp = self.current.next
            tmp.pre = self.current.pre
            self.head.next = tmp
            self.current = tmp
        else:
            self.buffer.append(self.current)
            ne = self.current.next
            pre = self.current.pre
            pre.next = ne
            ne.pre = pre
            self.current = ne
            
    def cancle(self):
        tmp = self.buffer.pop()
        pre = tmp.pre
        ne = tmp.next
        pre.next = tmp
        ne.pre = tmp
        
    def move(self,cnt):
        if cnt<0:
            for _ in range(abs(cnt)):
                self.current = self.current.pre
        else:
            for _ in range(cnt):
                self.current = self.current.next
                
    def print_all(self):
        tmp = self.head.next
        answer = ''
        while tmp !=self.tail:

            self.nlist[tmp.data] = 1
            tmp = tmp.next
        return self.nlist
def solution(n, k, cmd):
    answer = ''
    
    linkedlist = LinkedList()
    linkedlist.set_current(n,k)
    for c in cmd:
        tmp = c[0]
        if tmp == 'U':
            linkedlist.move(-int(c[2]))
     
        elif tmp == 'D':
            linkedlist.move(int(c[2]))
            print(linkedlist.current.data)
        elif tmp == 'C':
            linkedlist.delete()
            print(linkedlist.current.data)
        elif tmp == 'Z':
            linkedlist.cancle()
            
            
    for num in linkedlist.print_all():
        if num == 1:
             answer+='O'
        else:
             answer+='X'
   
    
    return answer
print(solution(10,3,["D 2"]))