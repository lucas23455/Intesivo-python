pessoa1 = {'firts_name': 'lucas',
          'last_name': 'passos',
          'idade': 21,
          'nacionalidade': 'brasileiro',
           }

pessoa2 = {'firts_name': 'paulo',
          'last_name': 'souza',
          'idade': 54,
          'nacionalidade': 'mexicano',
           }

pessoa3 = {'firts_name': 'marcos',
          'last_name': 'silva',
          'idade': 87,
          'nacionalidade': 'europeu',
           }


pessoas = [pessoa1,pessoa2,pessoa3]



for pessoa in pessoas:
    print(f'\nprimeiro nome: {pessoa['firts_name']}')
    print(f'sobrenome {pessoa['last_name']}')
    print(f'idade: {pessoa['idade']}')
    print(f'nacionalidade: {pessoa['nacionalidade']}')