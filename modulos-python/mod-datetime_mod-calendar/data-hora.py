# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime
from pytz import timezone

# * Criando data e hora

# data_str = '2022-04-20 07:49:23'
# data_str_fmt = '%Y-%m-%d %H:%M:%S'
# data_str = '20/04/2022'
# data_str_fmt = '%d/%m/%Y'
# data = datetime(2022, 4, 20, 7, 1, 59)
# data = datetime.strptime(data_str, data_str_fmt)
# print(data)

# * Data e hora atual, unix timestamp e timezone
data = datetime.now(timezone('America/Sao_Paulo'))
# data = datetime(2022, 4, 20, tzinfo=timezone('Asia/Tokyo'))
print(data)
print(data.timestamp())  # Isso está na base de dados
print(datetime.fromtimestamp(1710471126.436809))
