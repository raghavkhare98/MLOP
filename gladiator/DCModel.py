#here we will just store the data nothing else

class DC_Player:
    
    dcdata = []
    player_name = ""
    height = 0.0
    weight = 0.0
    number_of_games_played = 0

    def set_player_name(self, name):
        self.player_name = name
    
    def get_player_name(self):
        return self.player_name

    def set_player_height(self, height):
        self.height = height
    
    def get_player_height(self):
        return self.height
    
    def set_player_weight(self, weight):
        self.weight = weight
    
    def get_player_weight(self):
        return self.weight
    
    def set_player_no_of_games(self, number_of_games_played):
        self.number_of_games_played = number_of_games_played
    
    def get_player_no_of_games(self):
        return self.number_of_games_played


# dcdata = [
#         {"name": "BatMan", "height":180, "weight": 85, "games_played": 105},
#         {"name": "SuperMan", "height":189, "weight": 95, "games_played": 305},
#         {"name": "Harvedent", "height":181, "weight": 75, "games_played": 55},
#         {"name": "Henery", "height":176, "weight": 87, "games_played": 125},
#         {"name": "Heralt", "height":184, "weight": 100, "games_played": 145}
#     ]