# declaração de coleções
usuarios = [
    {
        'nome':"Arthur",
        'idade':20,
        'email':"arthur@gmail.com"
    },
    {
        'nome':"jão",
        'idade':25,
        'email':"jao@gmail.com"
    },
    {
        'nome':"cleiton",
        'idade':30,
        'email':"cleiton@gmail.com"
    }
]

# exibindo os dados dos usuários
for usuario in usuarios:
    print(f"\n{'-'*40}\n")
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario[chave]}")