class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.block_until = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        for k, b in list(self.block_until.items()):
            if b <= timestamp:
                del self.block_until[k]
        if self.block_until[message] > timestamp:
            return False
        else:
            self.block_until[message] = timestamp + 10
            return True



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
