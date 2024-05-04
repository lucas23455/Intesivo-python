aliens = []

for alien_number in range(30):

    novo_alien = {'cor':'amarelo',
                  'pontos':'50',
                  'velocidade':'lento',
                  }

    aliens.append(novo_alien)

for alien in aliens [0:3]:
    if alien ['cor'] == 'verde':
        alien['cor'] = 'amarelo'
        alien['velocidade'] = 'media'
        alien ['pontos'] = 10

    elif alien ['cor'] == 'amarelo':
        alien['cor'] = 'vermelho'
        alien['velocidade'] = 'rapido'
        alien['pontos'] = 15



for alien in aliens[:5]:
    print(alien)

print('...')