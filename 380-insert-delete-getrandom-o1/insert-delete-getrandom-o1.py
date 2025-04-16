class RandomizedSet:

    def __init__(self):
        self.values = []
        self.index_map = {}
        
    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.values.append(val)
        self.index_map[val] = len(self.values) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        
        idx_to_remove = self.index_map[val]
        last_val = self.values[-1]

        self.values[idx_to_remove] = last_val
        self.index_map[last_val] = idx_to_remove

        self.values.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()