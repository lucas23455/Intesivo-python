from teste1 import Carro
from teste2 import Carro_eletrico


carro_comum = Carro('ford','corola',2007)
print(carro_comum.descrever_carro())

print('='*20)

carro_eletrico = Carro_eletrico('tesla','city',2040)
print(carro_eletrico.descrever_carro())
carro_eletrico.bateria.descrever_bateria()