import sys
class Queue:
    def __init__(self, size: int): 
        self.queue = [None]*size
        self.head = 0
        self.tail = 0
        #self.size = size
        self.num = 0 #埋まってる要素数
    def enqueue(self, a: int):
        if self.num < len(self.queue):
            self.queue[self.tail % len(self.queue)]=a
            self.tail +=1
            if self.tail>2:
                self.tail = self.tail % len(self.queue)
            self.num += 1
            #print('head=',self.head,'tail=',self.tail,'num=',self.num,self.queue)
        else:
            print('queue is full')
    def dequeue(self):
        if self.queue[self.head] != None:
            tmp = self.queue[self.head]
            #print('tmp=',tmp)
            self.queue[self.head] = None
            self.head  = (self.head+1) % len(self.queue)
            self.num += -1
            #print('head=',self.head,'tail=',self.tail,'num=',self.num,self.queue)
            print(tmp)
        else: print('queue is empty')
Q,K = map(int, input().split())
rbuf = Queue(K)
for i in range(Q):
    s = list(map(int, input().split()))
    #typ, x = map(int, input().split())
    if s[0] == 1:
        rbuf.enqueue(s[1])
    elif s[0] == 2:
        rbuf.dequeue()
    i+=1