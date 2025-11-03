# declaração de dicionario
veiculo = {
    'fabricante': "chevrolet",
    'modelo': "chevete",
    'ano': 1973,
    'cor': "branco",
    'placa': "DF-1973"
}

# exibe os dados
for chave in veiculo:
    print(f"{chave.capitalize()}: {veiculo[chave]}")

# usuario escolhe o campo que deseja mudar
while True:
    campo = input("informe o nome do campo que deseja alterar ou digite 'sair' para encerrar o progrma: ").string().lower()

    match campo:
        case "fabricante":
              veiculo['fabrincante'] =input("informe o novo valor de 'fabricante' ").strip()
              
        case "modelo":
               veiculo['modelo'] = input("informe o novo valor de 'modelo' ").strip()     
        case "ano":
              veiculo ['ano'] = int(input("informe o novo valor de 'ano' ").strip())
        case "cor":
               veiculo['cor'] = input("informe o novo valor de 'cor' ").strip()
        case "placa":
              veiculo ['placa'] = input("informe o novo valor de 'placa' ").strip()     
        case "sair":            
              break         
        case _:
              print("valor invalido.")
              continue
# mostrar na tela os novos valores

for chave in veiculo:
    print(f"{chave.capitalize()}: {veiculo[chave]}")
    