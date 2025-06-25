import MarvelModel

class MarvelView:
    data=MarvelModel.Marvel_Player().Marveldata

    def get_view(self):
        print(MarvelModel.Marvel_Player().Marveldata)