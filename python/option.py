class Option:
    def __init__(self, agent, agent_team, target, move_type, pokemon_name, pokemon_move, agent_index):
        self.agent = agent
        self.agent_team = agent_team
        self.target = target
        self.move_type = move_type
        self.pokemon_name = pokemon_name
        self.pokemon_move = pokemon_move
        self.agent_index = agent_index
        
        self.d = []

    def __init__(self, options):
        self.options = {}
        
        

