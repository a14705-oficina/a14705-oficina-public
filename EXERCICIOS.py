print("hello world")

valorA = float(input("Insira o valor entre 1 a 20: "))
valorB = float(input("Insira o valor entre 1 a 20: "))
soma = valorA+valorB
media = (soma/2)
print(media)
if media >=10:
  print("Aprovado")
if media <=10:
  print ("Reprovado")
  
----------------------------------------------------------------------------

#EX0.1
"""
Declara uma variável chamada "idade" e atribuiu a tua idade.
Declara uma variável chamada "nome" e atribuiu o teu nome.
Imprima no ecrã a frase "O meu nome é [nome] e tenho [idade] anos."
"""
idade = input("Insira a sua idade: ");
nome = input("Insira o seu nome: ");

print(f"O meu nome é {nome} e tenho {idade} anos.");

----------------------------------------------------------------------------

#EX0.2

"""
Escreve um programa que imprima "Olá, mundo!" no ecrã.
Cria uma variável chamada "fruta" e atribuiu o nome de uma fruta.
Imprime no ecrã a frase "Eu gosto de [fruta]."
"""

print("Olá Mundo!");
fruta = "ananás"
print(f"Eu gosto de {fruta}.")

----------------------------------------------------------------------------

#EX0.3
"""
Solicita ao utilizador para digitar o nome.
Imprime no ecrã uma saudação personalizada utilizando o nome fornecido.
Pede ao utilizador para digitar um número inteiro.
Imprime o dobro desse número.
"""

nome = input("Insira o seu nome: ")
print(f"Olá, {nome}, espero que o seu trabalho corra bem! :)")
num = int(input("Insira um número inteiro: "))
dobro = num * 2;
print(f"O dobro do número que escolheu é {dobro}")

----------------------------------------------------------------------------
#EX1.1
"""
Elabora um programa que imprima a mensagem “Bem-vindos ao Python!”, precedida por uma linha em branco
"""
print("\nBem-vindos ao python!!")

----------------------------------------------------------------------------
#EX1.2
"""
Elabora um programa que imprima a mensagem “José, bem-vindo ao Python!”, precedida por uma linha em branco
"""

nome = input("\n Insira o seu nome: ")
print(f"\nOlá, {nome} , bem-vindo ao Python")

----------------------------------------------------------------------------
#EX1.3
"""
Elabora um programa que atribua a mensagem a uma variável e, em seguida, imprima o valor da variável.
"""

mensagem = "Eu gosto de carros e de motas"
print(mensagem)
----------------------------------------------------------------------------
#EX1.4
"""
Elabora um programa que atribua o nome, a idade e a localidade de residência do aluno a três variáveis e imprima os valores dessas variáveis.
"""
nome = input("\n Insira o seu nome: ")
idade = input("\n Insira a sua idade: ")
loc = input("\n Insira a sua localidade: ")

print(f"\nOlá! Eu chamo-me {nome}, tenho {idade} anos e moro em {loc}")

---------------------------------------------------------------------------
#EX1.5
"""
Elabora um programa que intercale a designação da linguagem de programação e o nome do aluno na mensagem
"""
ling = "Python"
nome = "Diogo"

print(f"Estou a aprender {ling} e chamo-me {nome}")
---------------------------------------------------------------------------
#EX1.6
"""
Elabora um programa que alinhe à direita, à esquerda e ao centro a mensagem “Bem-vindo ao Python!” num campo de edição com 50 carateres.
"""
mens = "Bem-vindo ao Python!"
print(f"{mens:<50}")
print(f"{mens:^50}")
print(f"{mens:>50}")

----------------------------------------------------------------------------
#EX1.7
print("Hello World!")

"""
Elabora um programa que desenvolva o algoritmo de um programa que permita calcular o perímetro e área de uma circunferência a partir do valor do raio.
"""

raio = float(input("Insira o valor do raio: "))
perimetro = 2 * 3.14 * raio
area = 3.14 * raio ** 2
print(f"O perímetro é {perimetro} e a área da circunferência é {area}")

----------------------------------------------------------------------------

#EX1.8
"""
Elabora um programa que imprima a data e horas correntes nos seguintes formatos: 
02-10-2024
02-10-2024 16:11:20
10-02-2024 16:11:20
02/10/24
16:11:20
"""

#Formato  02-10-2024
import datetime
a = datetime.datetime.now()
dia = a.strftime("%d")
mes = a.strftime("%m")
ano = a.strftime("%G")
print(f"{dia}-{mes}-{ano}")

#Formato  02-10-2024 16:11:20
import datetime
a = datetime.datetime.now()
dia = a.strftime("%d")
mes = a.strftime("%m")
ano = a.strftime("%Y")
horas = a.strftime("%H")
minutos = a.strftime("%M")
segundos = a.strftime("%S")
print(f"{dia}-{mes}-{ano} {horas}:{minutos}:{segundos}")

#Formato  10-02-2024 16:11:20
import datetime
a = datetime.datetime.now()
dia = a.strftime("%d")
mes = a.strftime("%m")
ano = a.strftime("%Y")
horas = a.strftime("%H")
minutos = a.strftime("%M")
segundos = a.strftime("%S")
print(f"{mes}-{dia}-{ano} {horas}:{minutos}:{segundos}")

#Formato  02/10/24
import datetime
a = datetime.datetime.now()
dia = a.strftime("%d")
mes = a.strftime("%m")
ano = a.strftime("%y")
horas = a.strftime("%H")
minutos = a.strftime("%M")
segundos = a.strftime("%S")
print(f"{mes}/{dia}/{ano}")

#Formato  16:11:20
import datetime
a = datetime.datetime.now()
dia = a.strftime("%d")
mes = a.strftime("%m")
ano = a.strftime("%Y")
horas = a.strftime("%H")
minutos = a.strftime("%M")
segundos = a.strftime("%S")
print(f"{horas}:{minutos}:{segundos}")

----------------------------------------------------------------------------
#EX1.9
"""
Elabora um programa que leia o número mecanográfico de um atleta, assim como a sua pontuação. O número é inteiro e a pontuação final é real.
Digite o número do atleta: 12304
Digite a pontuação final: 7.89
O atleta número 12304 obteve 7.89 pontos.
"""

no = input("Insira o número do atleta: ")
pf = input("Insira a pontuação final: ")
print(f"O atleta número {no} obteve {pf}")

-------------------------------------------------------------------------
#EX 1.10

"""
Elabora um programa que leia a data de nascimento de uma pessoa e imprima a sua idade à data atual.
"""
import datetime
data_atual = datetime.datetime.now()
dia = data_atual.strftime("%d")
mes = data_atual.strftime("%m")
ano = data_atual.strftime("%Y")
nascimento = input("Digite a data de nascimento (Do tipo dd/mm/aaaa): ")
data_atual = datetime.datetime.now()
dn  = int(nascimento[:2])
ma = int(nascimento[3:5])
an = int(nascimento[6:])
idade = data_atual.year - an - ((data_atual.month, data_atual.day) < (ma, dn))
print(f"A idade é {idade} anos.")

------------------------------------------------------------------------
#EX 1.11
"""
Elabora um programa que desenvolva o algoritmo de um programa que permita converter libras em euros, considerando a taxa de conversão de 1,19 ( ou seja, 1 GBP = 1,19 EURO).
"""
libras = float(input("Insira o valor em libras: "))
euros = libras * 1.19  
print(f"O valor em euros é {euros}")

-------------------------------------------------------------------------
#Trabalho Autonomia
print("Hello World!")

idade = int(input("\nEscreve a tua idade: "))

if idade < 12:
    print("\nÉs uma criança.")
elif idade < 18:
    print("\nÉs um adolescente.")
elif idade < 65:
    print("\nÉs um adulto.")
elif idade < 150:
    print("\nÉs um idoso.")
else:
    print("\nTu não és deste mundo!.")    

-------------------------------------------------------------------------
#Trabalho Autonomia
import random
seg = int(random.randint(0,5))

#print (f"O número secreto é: {seg}")
numes = int(input("Insira um valor inteiro entre (0 e 5): "))

if numes > seg:
  print("O número inserido é maior do que eu!")
elif numes < seg:
  print("O número inserido é menos do que eu!")
else:
  print("\n Acertaste!")

--------------------------------------------------------------------------
#Trabalho Autonomia
velocidade =int(input("Insira o valor da sua velocidade: "))
multa = velocidade - 80
valor = multa * 7
if velocidade < 80:
  print ("Boa! Continua a manter o limite de velocidade!")
elif velocidade > 80:
  print(f"Apanhaste uma multa! Vai ter que pagar {valor}€")

--------------------------------------------------------------------------
print("Hello World!")

"""
Exercício FP1: Verificar se um número é positivo, negativo ou zero.
Escreve um programa em Python que peça ao utilizador para introduzir um número e verifica se ele é positivo, negativo ou igual a zero.
Dica: Usa as estruturas condicionais if, elif e else.
"""

numero = int(input("\nEscolha um número inteiro à sua escolha: "))
if numero > 0:
  print("\nO seu número é positivo!")
elif numero == 0:
  print("\nO seu número é igual a zero!")
elif numero < 0:
  print ("\nO seu número é negativo!")

--------------------------------------------------------------------------
"""
Verificar se um número é par ou ímpar.
Escreve um programa que peça ao utilizador um número inteiro e verifica se ele é par ou ímpar.
Dica: Para verificar se um número é par, utilize a operação de módulo %.
"""
numero = int(input("\nInsira um número inteiro à sua escolha: "))
if numero % 2 == 0:
  print("O número é par")
else:
  print("o número é ímpar")

--------------------------------------------------------------------------
"""Calcular a nota final de um aluno.
Elabora um programa que pergunte ao utilizador a nota final de um aluno e verifica a classificação de acordo com a seguinte tabela:
Nota inferior a 10: "Reprovado"
Nota entre 10 e 14: "Suficiente"
Nota entre 15 e 17: "Bom"
Nota superior a 17: "Muito Bom"
"""
nota = float(input("\nInsira a nota do aluno: "))
if nota < 10:
  print ("Reprovado")
elif nota >= 10 and nota <= 14:
  print ("Suficiente")
elif nota >= 15 and nota < 17:
  print ("Bom")
else:
  print("Muito Bom")
--------------------------------------------------------------------------
"""
Exercício FP4: Conversor de temperaturas.
Cria um programa que pergunte ao utilizador uma temperatura em graus Celsius e a converta para Fahrenheit, Kelvin ou ambas. O utilizador deve escolher a unidade de destino (Fahrenheit ou Kelvin), e o programa deve exibir o valor convertido.
"""

Celsius = float(input("Escreva a temperatura em graus Celsius: "))
Fahrenheit = (Celsius * 9/5) + 32
Kelvin = Celsius + 273.15
opcao  = input("Escolha a conversão para Fahrenheit (F) | Kelvin (K) | Ambas (A): ")
if opcao == "F":
  print(f"\nA temperatura em Fahrenheit é {Fahrenheit}.")
elif opcao == "K":
  print(f"\nA temperatura em Kelvin é {Kelvin}")
elif opcao == "A": 
  print(f"\nA temperatura em Fahrenheit é {Fahrenheit} e em Kelvin é {Kelvin}.")
else:
  print("Opção inválida!")
--------------------------------------------------------------------------
"""
Exercício FP5: Cálculo de impostos
Crie um programa que peça ao utilizador o seu salário mensal e calcule o imposto de acordo com a seguinte tabela:
Salário até 1000: isento de impostos
Salário entre 1001 e 2000: 10% de imposto
Salário superior a 2000: 20% de imposto
O programa deve exibir o salário após a dedução do imposto.
"""

salario = float(input("Insira o seu salário mensal: "))
imposto2 = salario - 0.20
if salario <= 1000:
  print("Isento de Impostos!")
elif salario > 1001 and salario < 2000:
  imposto1 = salario * 0.10
  salarioImposto = salario - imposto1
  print(f"10% de Imposto! O valor do salário com o imposto é de {salarioImposto:.2f}€")
elif salario > 2001:
  imposto2 = salario * 0.20
  salarioImposto = salario - imposto2
  print(f"20% de Imposto! O valor do salário com o imposto é de {salarioImposto:.2f}€.")

---------------------------------------------------------------------------
#EX.FP6
print("Hello World\n")

"""
Escreve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10.
"""

for x in range(1,10):
  print (x)

---------------------------------------------------------------------------
#EX.FP7
"""
Escreve um programa que use um ciclo while para calcular a soma de todos os números de 1 a 100.
"""

soma = 0
num = 1
while num <= 100:
  soma += num
  num += 1
print(f"A soma dos números de 1 a 100 é: {soma}")

---------------------------------------------------------------------------
#EX.FP8
"""
Escreve um programa que peça ao utilizador para introduzir uma frase e utilize um ciclo for para contar quantas vogais (a, e, i, o, u) existem na frase.
"""

frase = input("Escreva uma frase: ")
vogal = 0
for letra in frase:
  if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    vogal += 1
print(f"\nEsta frase que escreveste tem {vogal} vogais.")

----------------------------------------------------------------------------
#EX.FP9
"""
Escreve um programa que utilize um ciclo for para listar todos os múltiplos de 5 entre 1 e 50.
"""
num = 5
while num <= 50:
  print(num)
  num += 5

-----------------------------------------------------------------------------
#EX.FP10
"""
Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números.
"""
valor = 0
notas = []
for i in range (1,6):

  num = int(input("\nEscreva um número inteiro: "))
  notas.append(num)
print(notas)
for i in range(0,4):
  valor += notas[i]
total = valor / 5
print (f"\nA média é: {total}")

------------------------------------------------------------------------------
#EX.FP11
"""
Escreve um programa que peça ao utilizador um número inteiro e verifique se ele é primo. Um número primo é divisível apenas por 1 e por ele mesmo. O programa deve utilizar um ciclo for para testar se o número é divisível por algum outro número.
"""
num = int(input("Insira um número inteiro: "))
div = 0
for i in range(1, num + 1):
  if num % i == 0:
    div += 1
if div == 2:
    print(f"O {num} é um número primo!")
else:
    print(f"O {num} não é um número primo")

-------------------------------------------------------------------------------
#EX.FP12
"""
Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista.
"""
lista = []
for i in range(1,21):
  if i % 2 == 0:
    lista.append(i)
print(f"Os números pares: {lista}")

----------------------------------------------------------------------------------
#EX.FP13
"""
Escreve um programa que peça ao utilizador para introduzir uma palavra ou frase e utilize um ciclo para imprimir a string invertida.
"""

texto = str(input("Insira um texto: "))
textoinv = texto [::-1]
print(textoinv)

----------------------------------------------------------------------------------
#EX.FP14
"""
Escreve um programa que gere a tabuada de multiplicação de um número introduzido pelo utilizador. O programa deve utilizar um ciclo for para calcular e exibir a tabuada até 10.
"""

num = int(input("Insira um número que deseja calcular a tabuada do mesmo: "))
for i in range(1,11):
  mult = num * i
  print(f"{num} x {i} = {mult}")

----------------------------------------------------------------------------------
#EX.FP15
"""
Escreve um programa que utilize um ciclo while para calcular o fatorial de um número introduzido pelo utilizador. O fatorial de um número n (n!) é o produto de todos os números inteiros positivos até n.
"""
num = int(input("Insira um número inteiro: "))
fatorial = 1
i = 1
while i <= num:
  fatorial *= i
  i += 1
print(f"O fatorial de {num} é {fatorial}")
