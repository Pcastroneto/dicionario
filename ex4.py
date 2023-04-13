dicionario = {"gato": "chat", "dog": "chien", "horse": "cheval"}

for chave in dicionario.keys(): # aqui ele pega ó a chave em vez de ambos como no outro  a chave é gato e o valor é chat
    print(chave,"->", dicionario[chave])