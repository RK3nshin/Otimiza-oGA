import Populacao 
class AlgoritimoGenetico:
    def __init__(self, populacao):
        self.populacao = populacao

    def executar(self, num_geracoes):
        melhor_aptidao_por_geracao = []
        pior_aptidao_por_geracao = []
        media_aptidao_por_geracao = []
        

        for geracao in range(num_geracoes):
            self.populacao.avaliar()
            if self.populacao.melhor_global is None or self.populacao.melhor_individuo.calcular_aptidao() < self.populacao.melhor_global.calcular_aptidao():
                self.populacao.melhor_global = self.populacao.melhor_individuo

            self.populacao.aplicar_elitismo()
            melhor_aptidao_por_geracao.append(self.populacao.melhor_global.calcular_aptidao())
            pior_aptidao_por_geracao.append(self.populacao.pior_individuo.calcular_aptidao())
            media_aptidao_por_geracao.append(self.populacao.media_aptidao)
            self.populacao.proxima_geracao()

        return melhor_aptidao_por_geracao, pior_aptidao_por_geracao, media_aptidao_por_geracao, self.populacao.melhor_global
