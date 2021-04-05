"""
Jogo de Questoes
vs Python

__author__ = Nurul-GC
__description__ = Apoio ao projecto do camarada Alberto Ferraz
"""

from os import listdir
from time import time


class JQ:
    def __init__(self):
        # definindo as variaveis globais
        self.inicioJogo = time()
        self.pontos = 0
        self.nomeJogador = input('Digite o seu nome:\n> ')

        self.jogo()

    def jogo(self):
        try:
            # para cada arquivo dentro da pasta "questoes"
            for pergunta in listdir('questoes'):
                # abra o arquivo e le a primeira linha substituindo a paragrafo por espaco vazio
                pergunta = open(f'questoes/{pergunta}').readlines()[0].replace('\n', '')
                # abre e le o arquivo contendo a resposta de acordo ao pergunta feita
                # e de igual modo e a primeira linha substituindo a paragrafo por espaco vazio
                respostaCorreta = open(f'respostas/{pergunta[0]}.txt').readlines()[0].replace('\n', '')

                # imprime a pergunta
                print(f"\n{pergunta}")
                # recebe a resposta
                respostaJogador = input('> ')

                # se a resposta do jogador for igual a resposta definida
                if respostaJogador == respostaCorreta:
                    # +2 pontos e imprime a informacao
                    self.pontos += 2
                    print(f"\nAcertou {self.nomeJogador} (+2 pontos)..")
                else:
                    # se nao, -1 ponto e imprime a informacao
                    self.pontos -= 1
                    print(f"\nErrou {self.nomeJogador} (-1 ponto)!\nResposta correta: '{respostaCorreta}'..")
        except KeyboardInterrupt:
            # se o usuario cancelar o jogo pela combinacao de teclado
            print("\nJogo cancelado pelo usuario..")
        finally:
            # imprimindo informaao final..
            fimJogo = time()
            totalTempo = fimJogo-self.inicioJogo
            print(f"Fim do jogo em {totalTempo}segundos com {self.pontos} pontos Parabens {self.nomeJogador}..")


if __name__ == '__main__':
    # executando o programa
    print("""
    ********************
    * JOGO DE QUESTOES *
    *  from: Nurul-GC  *
    * to:AlbertoFerraz *
    ********************
    """)
    jogar = JQ()
