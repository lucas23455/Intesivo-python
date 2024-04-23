alien = {'x_posiçao': 0 , 'y_posiçao': 25 , 'velocidade': 'rapida'}

print(f'A posiçao x original: {alien['x_posiçao']}')


if alien['velocidade'] == 'lenta':
    x_increment = 1

elif alien['velocidade'] == 'media':
    x_increment = 2

else:
    x_increment = 3


alien ['x_posiçao'] = alien['x_posiçao'] + x_increment

print(f'A nova posiçao {alien['x_posiçao']}')