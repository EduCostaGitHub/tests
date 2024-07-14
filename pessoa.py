import requests

class Pessoa():
    def __init__(self, nome='',sobrenome='', data=False) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.data = data

    def getData(self):
        response = requests.get('')

        if response.ok:
            self.data =True
            return 'CONNECTED'
        else:
            self.data = False
            return 'ERROR 404'