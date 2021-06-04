from pathlib import Path
from shutil import copyfile
import xlsxwriter
import re

basepath = Path('/home/brpl2103/bankrobber/')

files_in_basepath = basepath.glob('*.txt')

lista_termos = ('\"DEB.JUROS\"',
                '\"DEB.IOF\"',
                '\"TR TEV IBC\"',
                '\"DEB MORA\"',
                '\"TAR EXCESS\"')
conta = []
data_movimento = []
nr_doc = []
historico = [] 
valor = []
deb_cred = []
"Conta";"Data_Mov";"Nr_Doc";"Historico";"Valor";"Deb_Cred"




for item in files_in_basepath:
	with open(item) as inp:
		inp.re.match("\"D\"", "\"D\";")
		data = inp.readlines()
		for line in data:
			prin(line)
		# data_new = data.split(';') # Esse pega apenas o primeiro item do Extrato
		# print(data_new)
		# print(data_new[0]) # Conta
		# print(data_new[1]) # Data Movimento
		# print(data_new[2]) # Nr_Doc
		# print(data_new[3]) # Historico
		# print(data_new[4]) # Valor
		# print(data_new[5]) # Deb_Cred 

		try:
			for item in lista_termos:
				indexacao = data_new.index(item)
				conta.append(data_new[indexacao-3])
				data_movimento.append(data_new[indexacao-2])
				valor.append(data_new[indexacao+1])
				#print(f'Conta: {data_new[indexacao-3]} Data: {data_new[indexacao-2]} Tipo: {item} Valor: {data_new[indexacao+1]}')
		except:
			pass

