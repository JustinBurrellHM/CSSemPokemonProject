from queue import PriorityQueue
class Battlequeue:
    def __init__(self):
        self.pq = PriorityQueue()
    
    def set_priotity(self, option):
        if option.move_type == "Switch":
            return -6
        else:
            return -option.pokemon_move.priority 

    def save(self, option):
        self.pq.put(self.set_priotity(), option)
    
    def length(self):
        return self.pq.qsize()
    
    def process(self):
        try:
            priority_option = self.pq.get_nowait()
            return priority_option
        except:
            return None
            
'''
pq = PriorityQueue()
pq.put((0, absorb))
pq.put((6, switch))#switch has to mean something
pq.get()
pq.get_nowait()
'''


