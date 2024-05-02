import datetime

# Obtendo a data e hora atuais
data_hora_atual = datetime.datetime.now()
print("Data e hora atuais:", data_hora_atual)

# Obtendo apenas a data atual
data_atual = datetime.date.today()
print("Data atual:", data_atual)

# Criando um objeto datetime específico
data_especifica = datetime.datetime(2023, 12, 31, 23, 59, 59)
print("Data e hora específicas:", data_especifica)

# Convertendo data_atual para datetime.datetime
data_atual = datetime.datetime.combine(data_atual, datetime.time())

# Calculando a diferença entre duas datas
data_passada = datetime.datetime(2020, 1, 1)
diferenca = data_atual - data_passada
print("Diferença entre datas:", diferenca.days, "dias")

# Adicionando uma quantidade específica de tempo a uma data
data_futura = data_atual + datetime.timedelta(days=365)
print("Data daqui a um ano:", data_futura)

# Formatando datas
data_formatada = data_atual.strftime("%d/%m/%Y")
print("Data formatada:", data_formatada)

# Obtendo o dia da semana
dia_semana = data_atual.strftime("%A")
print("Dia da semana:", dia_semana)
