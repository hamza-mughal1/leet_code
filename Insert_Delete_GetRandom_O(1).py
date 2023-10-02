import random
class RanSet():
    def __init__(self):
        self.dic = {}
    
    def insert(self,val):
        n = len(self.dic)
        self.dic[val] = val
        return True if len(self.dic)>n else False
    
    def remove(self,val):
        e = self.dic.pop(val,"not")
        return False if e == "not" else True
    
    def getRandom(self):
        return random.choice(list(self.dic.items()))[0]
        
           
        
r = RanSet()

print(r.insert(0))
print(r.getRandom())
print(r.remove(0))
