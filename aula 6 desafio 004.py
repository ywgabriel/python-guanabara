x = input('Digite qualquer coisa:')
print(x, 'É do tipo primitivo', type(x))
print(x, 'Possui apenas números?', x.isnumeric(), '!')
print(x, 'Possui apenas letras?',  x.isalpha(), '!')
print(x, 'Possui letra ou número?', x.isalnum())
print(x, 'Possuia apenas letras maiúsculas?', x.isupper())
print(x, 'Possui apenas letras minúsculas?', x.islower())