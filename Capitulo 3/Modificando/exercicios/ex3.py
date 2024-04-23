pessoa = ['caio','vinicius','julia']

pessoa.insert(0,'paulo')
pessoa.insert(0,'pedro')
pessoa.append('lucas')
print(f'Tres pessoas foram convidadas : {pessoa[0]}, {pessoa[1]} e {pessoa[5]}')

message = f'Ola prezado'

print(message,pessoa[0]+' vc foi convidado para a festa')
print(message,pessoa[1]+' vc foi convidade para a festa')
print(message,pessoa[5]+' vc foi convidado para a festa')