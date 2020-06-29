class MaxQueue:

    def __init__(self):
        self.queue = []       # 输入队列
        self.max_queue = []   # 可能最大值队列

    def max_value(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.max_queue[0]

    def push_back(self, value: int):
        self.queue.append(value)

        ## 判断是否要删除 最大值 队列
        if len(self.max_queue) == 0:
            self.max_queue.append(value)
        else:
            while len(self.max_queue) != 0 and self.max_queue[-1] < value:
                self.max_queue.pop()
            self.max_queue.append(value)

        return None

    def pop_front(self):
        if len(self.queue) == 0:
            return -1

        queue_front = self.queue[0]

        ## 判断头部元素是否相等
        if queue_front == self.max_queue[0]:
            del self.max_queue[0]

        del self.queue[0]
        return queue_front


if __name__ == "__main__":
    q = MaxQueue()
    q.push_back(3)
    print(q.max_queue)
    q.push_back(1)
    print(q.max_queue)
    q.push_back(2)
    print(q.max_queue)
    q.pop_front()
    print(q.max_queue)
    q.pop_front()
    print(q.max_queue)