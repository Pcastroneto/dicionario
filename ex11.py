# simula um cadastro e vai guardadno os valores dentro de um dicionario 

cadastro={}
while True:
    nome = input("Digite o nome completo:")
    if nome == '':
        break
    idade = int(input('Digite a idade:')) 
    cidade = input("Digite a cidade:")
    
    #adciona os dados ao dicionario
    cadastro[nome]= {'idade': idade, 'cidade': cidade}
     
# Imprime o cadastro completo 
print("Cadastro:")
print(cadastro)
for nome, dados in cadastro.items():
    print("- Nome:",nome)
    print("- Nome:",dados["idade"])
    print("- Nome:",dados["cidade"])
    
#lista dentro de lista
    
    