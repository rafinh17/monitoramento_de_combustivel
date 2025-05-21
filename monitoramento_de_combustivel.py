#O programa deve solicitar ao usuário:

#Distância percorrida (em km)
distância_percorrida= float(input("digite a distancia percorrida em  km:"))
#Quantidade de combustível gasto (em litros)
combustivel_gasto = float(input('digite a quantidade de combustivel gasto:'))

#O programa deve calcular o consumo médio:

consumo_medio = distância_percorrida  / combustivel_gasto

#O valor calculado deve ser exibido junto com uma mensagem de desempenho, conforme a tabela abaixo:

if consumo_medio < 8:
    print("Menor que 8")
elif 8 > consumo_medio < 12:
    print("Maior que 8 e menor que 12")
else:
    print("Maior ou igual a 12")