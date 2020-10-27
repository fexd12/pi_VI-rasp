
import datetime


data_atual = datetime.datetime.today()
data_atual = str(data_atual.year) + '-' + str(data_atual.month) + '-' + str(data_atual.day)
print(data_atual)

datetime.date.strftime

data_final = datetime.datetime.strptime('26/10/20',"%d/%m/%y") #data recebida
data_final = str(data_final.year) + '-' + str(data_final.month) + '-' + str(data_final.day) 
print(data_final)


print(True if data_atual == data_final else 'errror')


# from leitura_tag import leitura

# leitura()