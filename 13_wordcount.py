"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys
from itertools import count
from pathlib import Path

# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).


def print_words(filename):
    path = Path(filename)
    contents = path.read_text(encoding='utf-8').lower()
    exclusive_words = get_exclusive_words(contents)

    exclusive_words.sort()
    for word in exclusive_words:
        num_words = contents.count(word)
        print(f'{word} {num_words}')


def print_top(filename):
    path = Path(filename)
    contents = path.read_text(encoding='utf-8').lower()
    exclusive_words = get_exclusive_words(contents)

    top_words = []
    for word in exclusive_words:
        num_words = contents.count(word)
        top_words.append([word, num_words])
    top_words = sorted(top_words, key=lambda word: word[1], reverse=True)

    if len(top_words) > 20:
        for word, occurrences in top_words[:20]:
            print(word, occurrences)
            pass
    else:
        for word, occurrences in top_words:
            print(word, occurrences)
            pass

def get_exclusive_words(contents):
    split_contents = contents.split()
    exclusive_words = []
    for word in split_contents:
        if word not in exclusive_words:
            exclusive_words.append(word)
    return exclusive_words

# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
