import MarvelView
import MarvelModel
# import gladiator.marvelcontroller as marvelcontroller
player=MarvelModel.Marvel_Player()
View=MarvelView.MarvelView()
# import mysql.connector

# player.set_player_height(90)
# print(player.get_player_height())

class Marvel_Controller:

    def marvel_controller(self):
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

            # player.Marveldata.append(player.get_player_name())
            temp_dict['name'] = player.get_player_name()

            height=float(input("Enter Player height:"))
            player.set_player_height(height)

            # player.Marveldata.append(player.get_player_height())
            temp_dict['height'] = player.get_player_height()

            weight=float(input("Enter Player Weight:"))
            player.set_player_weight(weight)

            # player.Marveldata.append(player.get_player_weight())
            temp_dict['weight'] = player.get_player_weight()

            number_of_games=int(input("Enter Player games:"))
            player.set_player_no_of_games(number_of_games)

            # player.Marveldata.append(player.get_player_no_of_games())
            temp_dict['games_played'] = player.get_player_no_of_games()

            player.Marveldata.append(temp_dict)
            i+=1
            print(f'Player number {i} stored in Marveldata successfully')

        # View.get_view()
        return MarvelModel.Marvel_Player.Marveldata
        
                    
# marvel_data=marvelcontroller().marvel_controller()



