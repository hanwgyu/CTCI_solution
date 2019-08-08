import random

# Use two hash. {val : idx} {idx : val} . When a node is removed, change maximum idx to index of the node.
class RandomizedSet(object):
    def __init__(self):
        self.idx_val = dict()
        self.val_idx = dict()
    def insert(self, val):
        if val in self.val_idx:
            return False
        idx = len(self.val_idx)
        self.val_idx[val] = idx
        self.idx_val[idx] = val
        return True
        
    def remove(self, val):
        if val not in self.val_idx:
            return False
        max_idx = len(self.val_idx) - 1
        idx = self.val_idx[val]
        del self.idx_val[idx]
        del self.val_idx[val]
        
        if idx == max_idx:
            return True
        match_val = self.idx_val[max_idx]
        del self.idx_val[max_idx]
        self.idx_val[idx] = match_val
        self.val_idx[match_val] = idx
        return True          

    def getRandom(self):
        rand_idx = random.randrange(0, len(self.val_idx))
        return self.idx_val[rand_idx]
