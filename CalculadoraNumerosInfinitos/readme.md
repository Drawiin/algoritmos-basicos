# Calculadora De Números Infinitos

Realizar as 4 operações aritiméticas utilizando numeros inteiros, de tamanho teóricamente inifinitos

# Instruções de execução

## Requisitos

Python 3.8 ou superior, é importante resaltar que para que
as intruções funcionem corretamente o python esteja nas suas
variaveis de ambiente ou path

## Execução

Em um terminal bash, powershel, cmd ou outro basta utilizar o comando no diretorio em que o arquivo calculator.py se encontra:

`python calculator.py`

ou

`python3 calculator.py`

ou até

`python3.8 calculator.py`

# Uso da Calculadora

A calculadora funciona de maneira interativa recebendo 3 argumentos separados por espaço

`numero1 operação numero2`

Exemplo de entrada válida

`101002 + 19128`

## Operações que a calculadora suporta

Suporta as 4 operações e um comando de escape

#### Soma

`+`

#### Subtração

`-`

#### Multiplicação

`*`

#### Divisão

`/`

#### Sair

`q`

## Regras

- Sempre sevem ser passados números inteiros positivos

- Os numeros e operador devem ser separados por um único espaço

# Pontos importante

- A soma é a unica operação que os dois números podem ser de qualquer tamanho

- Na operação de subtração caso o segundo número seja maior sempre será retornado o valor -1

- Na operação de divisão caso o segundo numero seja 0 será retornado -1

- A abordagem escolida para divisão e multiplixação é extremamente inceficiente, e como python não é uma
  linguagem focada em velocidade, reconsidere realizar essas operações com números muito grandes
  Elas serão concluídas, mais é provavel que tomem um tempo significativo.

- Repare que os números podem ter zeros a esquerda.
