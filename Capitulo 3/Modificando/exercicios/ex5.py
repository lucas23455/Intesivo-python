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

del pessoa [0]
del pessoa [0]
print(f"a lista está vazia" +str(pessoa))

