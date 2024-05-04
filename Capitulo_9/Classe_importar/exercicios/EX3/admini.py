from user import User
from privilegios import Privilegios

class Admin(User):
    def __init__(self, nome, sobrenome):
        super().__init__(nome, sobrenome)
        self.privilegios = Privilegios(['adicionar post', 'deletar post', 'banir post'])

    def mostre_privilegios(self):
        self.privilegios.mostre_privilegios()


