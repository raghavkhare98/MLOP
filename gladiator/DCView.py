#this is where we write the logic for displaying the data. No other logic needed

class DCView:   
    def get_view(self, player):
        for i in player.dcdata:
            print(i)
