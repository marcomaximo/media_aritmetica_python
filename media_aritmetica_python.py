#Primeira nota
nota1 = int(input('Informe a primeira nota: '))


#Peso da primeira nota
peso1 = int(input('Informe o primeiro peso: '))


#Segunda nota
nota2 = int(input('Informe a segunda nota: '))


#Peso da segunda nota
peso2 = int(input('Informe o segundo peso: '))


#Média Aritmética Ponderada
media_ponderada = (peso1 + peso2)


#Cálculo das médias
media_simples = (nota1 + nota2)/2
media_ponderada = (nota1 + nota2)/media_ponderada


#Resultado final dos cálculos
print('Média Aritmética Simples' ':', media_simples)
print('Média Aritmética Ponderada' ':', media_ponderada)