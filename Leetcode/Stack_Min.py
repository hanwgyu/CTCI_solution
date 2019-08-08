class MinNode(object):
    def __init__(self, min, value):
        self.min = min
        self.value = value

#Solution : node저장시 stack 전체의 최소값을 같이 저장. stack의 가장 최근 노드에 저장된 최소값이 항상 stack전체의 최소값.
class MinStack(object):
    def __init__(self):
        self.stack = []
        
    def push(self, x):
        current_min = self.getMin()
        if current_min is None or current_min > x:
            current_min = x
        self.stack.append(MinNode(current_min, x))

    def pop(self):
        self.stack.pop()

    def top(self):
        return None if not self.stack else self.stack[-1].value
        
    def getMin(self):
        return None if not self.stack else self.stack[-1].min
