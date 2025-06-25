class Marvel_Player:
    
    Marveldata=[]
    player_name=""
    height=0.0
    weight=0.0
    number_of_games_played=0

    def set_player_name(self,name):
        self.player_name=name

    def get_player_name(self):
        return self.player_name
    

    def set_player_height(self,height):
        self.height=height

    def get_player_height(self):
        return self.height
    
    def set_player_weight(self,weight):
        self.weight=weight

    def get_player_weight(self):
        return self.weight
    
    def set_player_no_of_games(self,number):
        self.number_of_games_played=number

    def get_player_no_of_games(self):
        return self.number_of_games_played

# Marveldata=[
#         {"name": "IronMan", "height":182, "weight": 90, "games_played": 105},
#         {"name": "Thor", "height":187, "weight": 120, "games_played": 75},
#         {"name": "Captain America", "height":184, "weight": 85, "games_played": 205},
#         {"name": "IronMan", "height":175, "weight": 75, "games_played": 45},
#         {"name": "Hulk", "height":179, "weight": 290, "games_played": 210}
# ]