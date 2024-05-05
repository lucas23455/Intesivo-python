pets = ['cao', 'gato', 'cao', 'peixe dourado', 'gato', 'coelho' , 'gato']
print(pets)

while 'gato' in pets:
    pets.remove('gato')
    pets.remove('cao')


print(pets)