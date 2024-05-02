class Privilegios():
    def __init__(self, privilegios):
        self.privilegios = privilegios

    def mostre_privilegios(self):
        print('Privilégios:')
        for privilegio in self.privilegios:
            print(privilegio)