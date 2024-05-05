def informacoes_carro(fabricante, modelo, **outros_infos):
    carro = {'fabricante': fabricante, 'modelo': modelo}
    for chave, valor in outros_infos.items():
        carro[chave] = valor
    return carro

# Chamada da função com informações sobre um carro
meu_carro = informacoes_carro('Ford', 'Mustang', ano=2022, cor='preto', motor='V8')
print(meu_carro)
