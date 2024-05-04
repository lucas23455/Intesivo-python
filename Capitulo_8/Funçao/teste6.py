def describe_pessoa(nome, nacionalidade = 'brasileira'):
    print(f'\nMeu nome é {nome}')
    print(f'Sou de nacionalidade {nacionalidade}')



describe_pessoa('lucas')

describe_pessoa('joao','americana')

describe_pessoa(nacionalidade='mexicana',nome='maria')

describe_pessoa(nome='marcos')

describe_pessoa()