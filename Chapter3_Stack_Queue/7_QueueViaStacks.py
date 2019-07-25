class MyQueue(object):
    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
        self.using_push = True #If False, pop_stack is being used.

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
       
