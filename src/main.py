from individuos import Individuo
from Populacao import Populacao
from AlgoritimoGenetico import AlgoritimoGenetico
import matplotlib.pyplot as plt



def ProcessarDados(Dados):
    BRUFCO = []
    LHRFCO = []
    MADFCO = []
    DUBFCO = []
    CDGFCO = []
    LISFCO = []
    FCOBRU = []
    FCOLHR = []
    FCOMAD = []
    FCODUB = []
    FCOCDG = []
    FCOLIS = []

    for linha in Dados:
        linha = linha.strip()  
        if linha:  
            Voo = linha.split(',')
            Origem = Voo[0]
            Destino = Voo[1]
            HorarioPartida = float(Voo[2].split(':')[0]) * 60 + float(Voo[2].split(':')[1])
            HorarioChegada = float(Voo[3].split(':')[0]) * 60 + float(Voo[3].split(':')[1])
            Preco = float(Voo[4])

            # Adiciona o voo ao dicionário correspondente
            voo_info = (Origem, Destino, HorarioPartida, HorarioChegada, Preco)

            if Origem == 'BRU' and Destino == 'FCO':
                BRUFCO.append(voo_info)
            elif Origem == 'LHR' and Destino == 'FCO':
                LHRFCO.append(voo_info)
            elif Origem == 'MAD' and Destino == 'FCO':
                MADFCO.append(voo_info)
            elif Origem == 'DUB' and Destino == 'FCO':
                DUBFCO.append(voo_info)
            elif Origem == 'CDG' and Destino == 'FCO':
                CDGFCO.append(voo_info)
            elif Origem == 'LIS' and Destino == 'FCO':
                LISFCO.append(voo_info)
            elif Origem == 'FCO' and Destino == 'BRU':
                FCOBRU.append(voo_info)
            elif Origem == 'FCO' and Destino == 'LHR':
                FCOLHR.append(voo_info)
            elif Origem == 'FCO' and Destino == 'MAD':
                FCOMAD.append(voo_info)
            elif Origem == 'FCO' and Destino == 'DUB':
                FCODUB.append(voo_info)
            elif Origem == 'FCO' and Destino == 'CDG':
                FCOCDG.append(voo_info)
            elif Origem == 'FCO' and Destino == 'LIS':
                FCOLIS.append(voo_info)
    
    Voos_Ida = {"BRUFCO": BRUFCO, "LHRFCO": LHRFCO, "MADFCO": MADFCO, "DUBFCO": DUBFCO, "CDGFCO": CDGFCO, "LISFCO": LISFCO}
    Voos_Volta = {"FCOBRU": FCOBRU, "FCOLHR": FCOLHR, "FCOMAD": FCOMAD, "FCODUB": FCODUB, "FCOCDG": FCOCDG, "FCOLIS": FCOLIS}

    return [Voos_Ida,Voos_Volta]


def GraficoPopulacao(PassagemIdas, PassagemVolta):
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    # Gráfico de barras para PassagemIdas
    axs[0].bar(range(len(PassagemIdas)), PassagemIdas, color='blue')
    axs[0].set_title('Passagens de Ida')
    axs[0].set_xlabel('Índice')
    axs[0].set_ylabel('Preço')

    # Gráfico de barras para PassagemVolta
    axs[1].bar(range(len(PassagemVolta)), PassagemVolta, color='green')
    axs[1].set_title('Passagens de Volta')
    axs[1].set_xlabel('Índice')
    axs[1].set_ylabel('Preço')

    # Ajustar layout
    plt.tight_layout()

    # Exibir o gráfico
    plt.show()


def AnaliseEstatistica(media_aptidao, melhor_aptidao, pior_aptidao, nome, num_geracoes):
    # Gráfico da média de aptidão por geração
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, num_geracoes + 1), media_aptidao, label='Média de Aptidão')
    plt.title(f'Média de Aptidão por Geração - {nome}')
    plt.xlabel('Geração')
    plt.ylabel('Aptidão')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Gráfico da melhor e pior aptidão por geração
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, num_geracoes + 1), melhor_aptidao, label=f'Melhor Aptidão - {nome}')
    plt.plot(range(1, num_geracoes + 1), pior_aptidao, label=f'Pior Aptidão - {nome}')
    plt.title(f'Melhor e Pior Aptidão por Geração - {nome}')
    plt.xlabel('Geração')
    plt.ylabel('Aptidão')
    plt.legend()
    plt.grid(True)
    plt.show()

# Exemplo de uso:
# Suponha que você tenha definido media_aptidaoIda, melhor_aptidaoIda, pior_aptidaoIda e num_geracoes corretamente
# AnaliseEstatistica(media_aptidaoIda, melhor_aptidaoIda, pior_aptidaoIda, 'Ida', num_geracoes)


if __name__ == "__main__":
    caminho_arquivo = 'flights.txt'

    # Processar os dados do arquivo de voos
    with open(caminho_arquivo, 'r') as TabelaVoos:
        Voos_ida, Voos_Volta = ProcessarDados(TabelaVoos)
    
    keyIdas = ["BRUFCO", "LHRFCO", "MADFCO", "DUBFCO", "CDGFCO", "LISFCO"]
    keyVolta = ["FCOBRU", "FCOLHR", "FCOMAD", "FCODUB", "FCOCDG", "FCOLIS"]

    tamanho_populacao = 200

    populacaoida = Populacao(Voos_ida, tamanho_populacao, keyIdas, 1)
    populacaovolta = Populacao(Voos_Volta, tamanho_populacao, keyVolta, 0)

    ga1 = AlgoritimoGenetico(populacaoida)
    ga2 = AlgoritimoGenetico(populacaovolta)

    num_geracoes = 300

    melhor_aptidaoIda, pior_aptidaoIda, media_aptidaoIda, melhor_globalIda = ga1.executar(num_geracoes)
    melhor_aptidaoVolta, pior_aptidaoVolta, media_aptidaoVolta, melhor_globalVolta = ga2.executar(num_geracoes)

    print("Passagem de Ida \n")
    print(melhor_globalIda)
    print(f'Aptidão do Melhor Indivíduo: {melhor_aptidaoIda[-1]}')
    
    AnaliseEstatistica(media_aptidaoIda, melhor_aptidaoIda, pior_aptidaoIda, 'Ida', num_geracoes)

    print("Passagem de Volta \n")
    print(melhor_globalVolta)
    print(f'Aptidão do Melhor Indivíduo: {melhor_aptidaoVolta[-1]}')
    AnaliseEstatistica(media_aptidaoVolta, melhor_aptidaoVolta, pior_aptidaoVolta, 'Volta', num_geracoes)
