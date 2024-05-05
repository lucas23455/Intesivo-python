planetas = ['mercurio','venus','terra','marte','saturno','jupite','urano','netuno','plutao']
print(planetas)

planetas = ['mercurio','venus','terra','marte','saturno','jupite','urano','netuno','plutao']
Maiusculo=str(planetas).upper()
#Remove os colchetes
Maiusculo = Maiusculo.strip("[]")
print(Maiusculo)

Minusculo = str(planetas).lower()
Minusculo = Minusculo.strip('[]')
print(Minusculo)


Titulo = str(planetas).title()
Titulo = Titulo.strip('[]')
print(Titulo)

planetas.append('lua')
planetas.append('europa')
planetas.append('caronte')
print(planetas)


del planetas [3]
del planetas [6]
del planetas [9]
print(planetas)


planetas.insert(9,"sol")
planetas.insert(0,'cometa halley')
print(planetas)

planetas [2] = "venuso"
print(planetas)


planeta_removido = planetas.pop()
print(planeta_removido)

planetas.remove('saturno')
print(planetas)


planetas.sort()
print(planetas)

planetas.sort(reverse=True)
print(planetas)

print(sorted(planetas))

planetas.reverse()
print(planetas)

print(f'tamanho da lista: {len(planetas)}')