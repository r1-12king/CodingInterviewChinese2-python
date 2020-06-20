class Stock:
    """
    进栈：元素入队列1
    出栈：判断如果队列1只有一个元素，则直接出队。否则，把队1中的元素出队并入队2，
            直到队1中只有一个元素，再直接出队。为了下一次继续操作，互换队1和队2。
    """
    def __init__(self):
        self.queue1=[]
        self.queue2=[]
    def push(self, node):
        self.queue1.append(node)
    def pop(self):
        if len(self.queue1)==0:
            return None
        while len(self.queue1)!=1:
            self.queue2.append(self.queue1.pop(0))
        self.queue1,self.queue2=self.queue2,self.queue1 #交换是为了下一次的pop
        return self.queue2.pop()

if __name__=='__main__':
    times=5
    testList=list(range(times))
    testStock=Stock()
    for i in range(times):
        testStock.push(testList[i])
    print(testList)
    for i in range(times):
        print(testStock.pop(),',',end='')
    # 输出结果：后进先出
    # [0, 1, 2, 3, 4]
    # 4 ,3 ,2 ,1 ,0 ,