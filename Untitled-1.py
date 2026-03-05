entrada_usuario = (float(input("Digite um numero: "))) #Definindo a entrada do usuario (usando ponto flutuante pra nao quebrar)

maior_que = entrada_usuario #Definindo variavel fora do loop para não dar erro e atribuindo ela o primeiro valor digitado para o usuario

#Inicio do loop de verificacao dos numeros digitados 
for i in range(4): #Definir a quantidade com (I sendo indice 0) até (range(4) que vai ate 5 pois 0, mais 1 mais 2 mais 3 mais 4 mais 5 definido pelo rang(4))
    entrada_usuario = (float(input("Digite outro numero: ")))
    
    if entrada_usuario > maior_que: #Declarando condicional se a minha entrada de usuario foi maior que o primeiro numero atuliza o primeiro caso contrario nao faz nada 
        maior_que=entrada_usuario

print(f"Seu maior numero foi {maior_que}")
