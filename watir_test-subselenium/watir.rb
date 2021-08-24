require 'watir'
browser = Watir::Browser.new
browser.goto 'https://internetbanking.caixa.gov.br'

text_field_name = browser.text_field(id: 'nomeUsuario')
text_field_name.set 'BRPL8611111'

radio = browser.radio(id: 'tpPessoaJuridica')
radio.select

button = browser.button(value: 'CONTINUAR')
button.click

element = browser.element(class: 'textHiddenDV')
element.click


browser.alert.wait_until { |a| a.text == "foo" }

#browser.element(class: 'xx').wait_until(&:enabled?)



#browser.text_field( 'brpl8611111')
#text_field.set 'Luke'