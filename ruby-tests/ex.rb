require 'fast_excel'
require 'date'
require 'time'

x = []
y = []

file = File.open("ex.txt").readlines.map(&:chomp)

file.each do |lines|
	x << "#{lines.to_s};\n"
end

x.each do | lines |
	y << lines.split(";")
end

puts y[0][0] # Conta
puts y[0][1] # Data_Mov
puts y[0][2] # Nr_Doc
puts y[0][3] # Historico
puts y[0][4] # Valor
puts y[0][5] # Deb_Cred



workbook = FastExcel.open("test.xlsx", constant_memory: true)
bold = workbook.bold_format
worksheet = workbook.add_worksheet(y[1][0])
worksheet.auto_width = true
#format = worksheet.add_format(font_color: :red)


worksheet.append_row([y[0][1], y[0][2], y[0][3], "Beneficiário", "Conciliado", y[0][4], y[0][5]], bold)





y.each_with_index do |i, index|
	next if index == 0
	
	date = i[1].gsub('"', '')
	date_time = Time.parse(date).strftime("%d-%m-%Y")
	if i[5].gsub('"', '') == 'D'
		valor = i[4].gsub('"', '').to_f * -1
		valor_trabalhado = valor
	else
		valor_trabalhado = i[4].gsub('"', '').to_f
	end
	worksheet.append_row([date_time, i[2], i[3], "", "", valor_trabalhado, i[5].gsub('"', '')])
end
workbook.close
