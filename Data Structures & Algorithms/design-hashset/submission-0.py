class MyHashSet:

    def __init__(self):
       self.size=1000
       self.obj = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        idx=key%self.size
        if key not in self.obj[idx]:
            self.obj[idx].append(key)

    def remove(self, key: int) -> None:
        idx=key % self.size
        if key in self.obj[idx]:
            self.obj[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = key % self.size
        if key in self.obj[idx]:
            return True
        else:
            return False
        

        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)