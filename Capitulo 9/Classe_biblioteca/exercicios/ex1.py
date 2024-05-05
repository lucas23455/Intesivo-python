from collections import OrderedDict

glossario = OrderedDict()

glossario['if'] = 'decisão'
glossario['else'] = 'decisão composta'
glossario['title'] = 'título'
glossario['range'] = 'repetição'
glossario['print'] = 'impressão'

for palavra, significado in glossario.items():
    print(f'{palavra}: {significado}')
