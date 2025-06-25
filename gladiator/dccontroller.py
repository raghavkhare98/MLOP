"""
this is where the user interacts. So we will run these functions to store the data which gets stored
in DCModel.py
"""

import DCView
import DCModel

player = DCModel.DC_Player()
View = DCView.DCView()

class DC_Controller:
    
    def dc_controller(self):
        
        i=0
        while i<5:
            temp_dict = {
                'name': None,
                'height': None,
                'weight': None,
                'games_played': None
            }
            name=input("Enter Player Name: ")
            player.set_player_name(name)

            # player.dcdata.append(player.get_player_name())
            temp_dict['name'] = player.get_player_name()

            height=float(input("Enter Player height:"))
            player.set_player_height(height)
            temp_dict['height'] = player.get_player_height()

            # player.dcdata.append(player.get_player_height())

            weight=float(input("Enter Player Weight:"))
            player.set_player_weight(weight)

            # player.dcdata.append(player.get_player_weight())
            temp_dict['weight'] = player.get_player_weight()


            number_of_games=int(input("Enter Player games:"))
            player.set_player_no_of_games(number_of_games)

            # player.dcdata.append(player.get_player_no_of_games())
            temp_dict['games_played'] = player.get_player_no_of_games()

            player.dcdata.append(temp_dict)
            i+=1
            print(f'Player number {i} stored in dcdata successfully')

        # View.get_view(player)
        return DCModel.DC_Player.dcdata

# dc_data=DC_Controller().dc_controller()