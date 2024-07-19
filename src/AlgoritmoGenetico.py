import matplotlib.pyplot as plt

class AlgoritmoGenetico:
    def __init__(self, populacao):
        self.populacao = populacao
        self.melhor_global = None

    def executar(self, num_geracoes):
        melhor_aptidao_por_geracao = []
        pior_aptidao_por_geracao = []
        media_aptidao_por_geracao = []

        while num_geracoes > 0:
            self.populacao.avaliar()

            if self.melhor_global is None or self.populacao.melhor_individuo.calcular_aptidao() < self.melhor_global.calcular_aptidao():
                self.melhor_global = self.populacao.melhor_individuo.copy()

            self.populacao.aplicar_elitismo(self.melhor_global.copy())
            melhor_aptidao_por_geracao.append(self.melhor_global.calcular_aptidao())
            pior_aptidao_por_geracao.append(self.populacao.pior_individuo.calcular_aptidao())
            media_aptidao_por_geracao.append(self.populacao.media_aptidao)

            self.populacao.proxima_geracao()
            
          
            num_geracoes -= 1

        return melhor_aptidao_por_geracao, pior_aptidao_por_geracao, media_aptidao_por_geracao, self.melhor_global.copy()

