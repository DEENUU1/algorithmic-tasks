import random 

class RandomizedSet:

    def __init__(self):
        self.lst = []

    def insert(self, val: int) -> bool:
        if val not in self.lst:
            self.lst.append(val)
            return True
        return False 

    def remove(self, val: int) -> bool:
        try:
            idx = self.lst.index(val)
            self.lst.pop(idx)
            return True
        except ValueError:
            return False


    def getRandom(self) -> int:
        return random.choice(self.lst)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()