import random
import numpy as np 
class Voo:
    def __init__(self, Origem, Destino, HorarioPartida, HorarioChegada, Preco):
        self.Origem = Origem
        self.Destino = Destino
        self.HorarioPartida = HorarioPartida
        self.HorarioChegada = HorarioChegada
        self.Preco = Preco

    def __eq__(self, other):
        return (self.Preco == other.Preco and
                self.Origem == other.Origem and
                self.Destino == other.Destino and
                self.HorarioPartida == other.HorarioPartida and
                self.HorarioChegada == other.HorarioChegada)
    
    def __repr__(self):
        return (f"Voo(Origem={self.Origem}, Destino={self.Destino},"
                f"HorarioPartida={self.HorarioPartida},"
                f"HorarioChegada={self.HorarioChegada}, Preco={self.Preco}) \n")
        

class Individuo:
    def __init__(self, VoosDisponiveis, key,flag):
        self.key = key
        self.flag = flag
        # Defenir um passagem aleatóriamente
        self.voos = [Voo(*random.choice(VoosDisponiveis[rota])) for rota in key
                        if rota in VoosDisponiveis]
      
    def __repr__(self):
        return f"(VoosIda={self.voos} \n"
    
    def copy(self):
        # Criar uma nova instância do Individuo
        novo_individuo = Individuo([], self.key, self.flag)
        # Copiar todos os atributos necessários
        novo_individuo.voos = [Voo(voo.Origem, voo.Destino, voo.HorarioPartida, voo.HorarioChegada, voo.Preco) for voo in self.voos]
        return novo_individuo
    
    def calcular_aptidao(self):
        Alfa = 0.75
        Beta = 0.25
        PrecoFinal = 0
        TemposEsperaPorPessoa = []

        if self.flag:
            for voo in self.voos:
                PrecoFinal += voo.Preco

            # Calcula o tempo de espera para os voos de ida
            tempos_chegada_ida = [voo.HorarioChegada for voo in self.voos]
            TempoMaximoChegada = max(tempos_chegada_ida)
            TemposEsperaPorPessoa = [TempoMaximoChegada - tempo for tempo in tempos_chegada_ida]


            media_tempo_ida = np.mean(TemposEsperaPorPessoa)
            desvio_tempo_ida = np.std(TemposEsperaPorPessoa)
            CoeficienteTempo = media_tempo_ida + desvio_tempo_ida


            aptidaoIda = Alfa * PrecoFinal + Beta * CoeficienteTempo
            return aptidaoIda 
        else:
            for voo in self.voos:
                PrecoFinal += voo.Preco

            # Calcula o tempo de espera para os voos de volta
            tempos_partida_volta = [voo.HorarioPartida for voo in self.voos]
            TempoMinimoPartida = min(tempos_partida_volta)
            TemposEsperaPorPessoa = [tempo - TempoMinimoPartida  for tempo in tempos_partida_volta]
            
            media_tempo_volta= np.mean(TemposEsperaPorPessoa)
            desvio_tempo_volta = np.std(TemposEsperaPorPessoa)
            CoeficienteTempo = media_tempo_volta + desvio_tempo_volta

            aptidaoVolta = Alfa * PrecoFinal + Beta * CoeficienteTempo

            return  aptidaoVolta

    def crossover(self, other,VoosDisponiveis):
    
        tamanho = len(self.voos)
        ponto1 = random.randint(1, tamanho - 2)
        ponto2 = random.randint(ponto1 + 1, tamanho - 1)

        filho1_genes = self.voos[:ponto1] + other.voos[ponto1:ponto2] + self.voos[ponto2:]
        filho2_genes = other.voos[:ponto1] + self.voos[ponto1:ponto2] + other.voos[ponto2:]

        filho1 = Individuo(VoosDisponiveis, self.key, self.flag)  
        filho2 = Individuo(VoosDisponiveis, self.key, self.flag)  
        
        filho1.voos = filho1_genes
        filho2.voos = filho2_genes

        return filho1, filho2
    
    def mutacao(self, voos_disponiveis,taxa):
      if random.random() >  taxa:
        mask = [random.randint(0, 1) for _ in range(len(self.voos))]

        for i in range(len(self.voos)):
            if mask[i] == 1:
                rota = list(voos_disponiveis.keys())[i]
                self.voos[i] = Voo(*random.choice(voos_disponiveis[rota]))

