from pathlib import Path
from shutil import copyfile

basepath = Path('/media/bruno/DATA/GD/BR_BANKROBBER/EXTRATOS.TXT')
files_in_basepath = basepath.glob('*.txt')
lista_termos = ('\"DEB.JUROS\"', '\"DEB.IOF\"', '\"TR TEV IBC\"', '\"DEB MORA\"', '\"TAR EXCESS\"')

for item in files_in_basepath:
	with open(item) as inp:
		data = str(inp.readlines())
		#data_clean = data.replace("", '.')
		data_new = data.split(';')
		try:
			for item in lista_termos:
				indexacao = data_new.index(item)
				print(f'Conta: {data_new[indexacao-3]} Data: {data_new[indexacao-2]} Tipo: {item} Valor: {data_new[indexacao+1]}')
		except:
			pass