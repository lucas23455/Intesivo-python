pessoa = ['caio','vinicius','julia']

pessoa.insert(0,'paulo')
pessoa.insert(0,'pedro')
pessoa.append('lucas')
print(f'Tres pessoas foram convidadas : {pessoa[0]}, {pessoa[1]} e {pessoa[5]}')




#removendo pessoas da lista
pessoa.pop()
pessoa.pop()
pessoa.pop()
pessoa.pop()
print(pessoa)

#messagem de convite para as pessoas da lista
print(f'Vc ainda está convidado {pessoa[0]}')
print(f'vc ainda esta convidade {pessoa[1]}')


