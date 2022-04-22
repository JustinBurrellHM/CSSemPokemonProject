from queue import PriorityQueue
class Battlequeue:
    def __init__(self):
        self.pq = []
    
    def set_priotity(self, option):
        if option.options["move_type"] == "Switch":
            return -6
        else:
            return -option.options["pokemon_move"].priority

    def save(self, option):
        priority_value = self.set_priotity(option)
        self.pq.append((priority_value, option))
    
    def length(self):
        return self.pq.qsize()
    
    def process(self):
        max_option = None
        for (priority, option) in self.pq:
            if priority > max_option:
                max_option = priority
            elif priority == max_option:
                #compare speed
            #save it as something else
            #delete the option from self.pq
        # return the new variable


