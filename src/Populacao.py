import random
import math
from individuos import Individuo

class Populacao:
    

    def __init__(self, voos_disponiveis, tamanho_populacao, key, flag):
        self.voos_disponiveis = voos_disponiveis
        self.tamanho_populacao = tamanho_populacao
        self.individuos = [Individuo(voos_disponiveis, key, flag) for _ in range(tamanho_populacao)]
        self.pior_individuo = None
        self.melhor_individuo = None
        self.media_aptidao = 0

    def avaliar(self):
        # Avaliar
        aptidoes = [ind.calcular_aptidao() for ind in self.individuos]

        # Atualizar Melhor e Pior Indivíduo
        self.melhor_individuo = min(self.individuos, key=lambda ind: ind.calcular_aptidao())
        self.pior_individuo = max(self.individuos, key=lambda ind: ind.calcular_aptidao())

        # Calcular média da aptidão
        self.media_aptidao = sum(aptidoes) / len(aptidoes)

    def selecao_por_torneio(self, k=2):
        competidores = random.sample(self.individuos, k)
        sorte = random.random()
        if sorte > 0.2:
            return min(competidores, key=lambda ind: ind.calcular_aptidao())
        else:
            return max(competidores, key=lambda ind: ind.calcular_aptidao())

    def proxima_geracao(self, prob_cruzamento=0.80, prob_mutacao=0.35):
        nova_populacao = []

        while len(nova_populacao) < self.tamanho_populacao:
            pai1 = self.selecao_por_torneio()
            pai2 = self.selecao_por_torneio()

            # Cruzamento (crossover)
            if random.random() < prob_cruzamento:
                filho1, filho2 = pai1.crossover(pai2, self.voos_disponiveis)
            else:
                filho1, filho2 = pai1, pai2

            # Mutação
            filho1.mutacao(self.voos_disponiveis, prob_mutacao)
            filho2.mutacao(self.voos_disponiveis, prob_mutacao)

            nova_populacao.extend([filho1, filho2])

        self.individuos = nova_populacao[:self.tamanho_populacao]
        self.avaliar()
        
    def aplicar_elitismo(self,melhor_global):
        elite = math.ceil(0.05 * self.tamanho_populacao)
        

        for i in range(elite):
            self.individuos.remove(self.pior_individuo)
            self.individuos.append(melhor_global)
            self.pior_individuo = max(self.individuos, key=lambda ind: ind.calcular_aptidao())

            

        self.pior_individuo = max(self.individuos, key=lambda ind: ind.calcular_aptidao())
