# Time : O(1) (For all functions), Space : O(N)


class MyCircularQueue:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = [0] * k
        self.maxlen = k
        self.size = 0
        self.front = 0

    def rearIndex(self) -> int:
        return (self.front + self.size - 1) % self.maxlen

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[(self.rearIndex() + 1) % self.maxlen] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.front = (self.front + 1) % self.maxlen
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rearIndex()]

    def isEmpty(self) -> bool:
        return True if self.size == 0 else False

    def isFull(self) -> bool:
        return True if self.size == self.maxlen else False
