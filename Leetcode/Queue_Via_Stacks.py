"""
self.st2가 비었을때만 self.st1에서 옮기도록 동작함.
따라서 pop시에도 amortized O(1) 시간 복잡도가 가능함.
"""
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st1 = []
        self.st2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.st1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.st2.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
        return self.st2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.st1 and not self.st2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

----

class MyQueue(object):
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
        self.using_push = True  # If False, pop_stack is being used.

    def push(self, x):
        if not self.using_push:
            while self.pop_stack:
                self.push_stack.append(self.pop_stack.pop())
            self.using_push = True
        self.push_stack.append(x)

    def pop(self):
        if self.using_push:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
            self.using_push = False
        return self.pop_stack.pop()

    def peek(self):
        if self.using_push:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
            self.using_push = False
        return None if not self.pop_stack else self.pop_stack[-1]

    def empty(self):
        return not self.push_stack and not self.pop_stack
