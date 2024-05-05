lugares = ['paris','estados unidos','suecia','alemanha','russia','japao']
print('lista original')
print(lugares)

print('lista ordenada')
print(sorted(lugares))

print('lista original não foi alterada')
print(lugares)

lugares.reverse()
print('lista reversa')
print(lugares)

lugares.reverse()
print('lista voltou ao normal')
print(lugares)

lugares.sort()
print('lista ordenada com sort')
print(lugares)

lugares.sort(reverse=True)
print('lista reversa com sort')
print(lugares)