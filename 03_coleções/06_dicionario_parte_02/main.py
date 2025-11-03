# declaração de dicionario
usuario = {
    'nome': "Alex Machado",
    'nascimento': "01/01/1995",
    'email': "alex@gmail.com",
    'telefone':"(61) 98765-4321",
    'endereço': "QI"
}

for chave in usuario:
    print(f"{chave.capitalize()}{usuario[chave]}")
