from queue import PriorityQueue
class Battlequeue:
    def __init__(self):
        self.pq = []
    
    def set_priotity(self, option):
        if option.options["move_type"] == "Switch":
            return 6
        else:
            return option.options["pokemon_move"].priority

    def save(self, option):
        priority_value = self.set_priotity(option)
        self.pq.append((priority_value, option))
    
    def length(self):
        return len(self.pq)
    
    def process(self):
        max_option = (-99999999, None)
        for (priority, option) in (self.pq):
            if priority > max_option[0]:
                max_option = (priority, option)
            elif priority == max_option[0]:
                if option.options["agent"].spe > max_option[1].options["agent"].spe:
                    max_option = (priority, option)
        self.pq.remove(max_option)
        return max_option[1]

