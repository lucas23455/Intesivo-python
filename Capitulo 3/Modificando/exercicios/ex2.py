
pessoas = ['caio', 'vinicius', 'pedro']
pessoa_removida = pessoas.pop()
pessoas.append('julia')
message_de_cancelamento = 'Infelizmente o '

print(message_de_cancelamento + pessoa_removida + ' não estará no jantar \nEntão ' + pessoas[-1] + ' irá!')
print(pessoas)