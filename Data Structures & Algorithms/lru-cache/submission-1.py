class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.tot = 0
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:   
            val = self.cache.pop(key)
            self.cache[key] = val
        return val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and self.cap == self.tot:
            for old_key in self.cache.keys():
                self.cache.pop(old_key)
                break
        else:
            if key in self.cache:
                self.cache.pop(key)
            else:
                self.tot+=1
        self.cache[key] = value
            
        
        
