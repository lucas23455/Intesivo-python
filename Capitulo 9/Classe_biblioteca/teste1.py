from collections import  OrderedDict

linguagens_favoritas = OrderedDict()

linguagens_favoritas['lucas'] = 'python'
linguagens_favoritas['pedro'] = 'java'
linguagens_favoritas['maria'] = 'ruby'
linguagens_favoritas['marcos'] = 'java script'
linguagens_favoritas['joao'] = 'lua'


print(linguagens_favoritas)

for nome , linguagem in linguagens_favoritas.items():
    print(f'Linguagem favorita de {nome.title()}: {linguagem.title()}')



    