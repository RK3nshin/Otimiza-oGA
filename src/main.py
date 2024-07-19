from individuos import Individuo
from Populacao import Populacao
from AlgoritmoGenetico import AlgoritmoGenetico
from ProcessarDados import ProcessarDados 
import matplotlib.pyplot as plt
import numpy as np
import threading


def executar_ga1(resultados, indice, ga1, num_geracoes):
    resultados[indice] = ga1.executar(num_geracoes)

def executar_ga2(resultados, indice, ga2, num_geracoes):
    resultados[indice] = ga2.executar(num_geracoes)



def AnaliseEstatistica(media_aptidao, melhor_aptidao, pior_aptidao, nome, num_geracoes):
    plt.figure(figsize=(10, 6))

    plt.plot(range(1, num_geracoes + 1), media_aptidao, label='Média de Aptidão')

    plt.plot(range(1, num_geracoes + 1), melhor_aptidao, label=f'Melhor Aptidão - {nome}')

    plt.plot(range(1, num_geracoes + 1), pior_aptidao, label=f'Pior Aptidão - {nome}')

    plt.title(f'Aptidão por Geração - {nome}')
    plt.xlabel('Geração')
    plt.ylabel('Aptidão')
    
    plt.legend()
    plt.grid(True)
    
    plt.show()

def Analise(Ida, Volta):
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    axs[0].bar(range(len(Ida)), Ida, color='blue')
    axs[0].set_title('Passagens Vencedoras para Ida')
    axs[0].set_xlabel('Índividuos')
    axs[0].set_ylabel('Aptidão')

    axs[1].bar(range(len(Volta)), Volta, color='green')
    axs[1].set_title('Passagens Vencedoras para Volta')
    axs[1].set_xlabel('Índividuos')
    axs[1].set_ylabel('Aptidão')

    plt.tight_layout()
    plt.show()


def imprimir_resultados(Melhor):
    preco, tempos_espera = Melhor.Resultados()

    print(f"Preço Final: {preco}")
    print("Tempos de Espera por Pessoa:")
    for idx, tempo in enumerate(tempos_espera):    print(f"Pessoa {idx + 1}: {tempo} minutos")

if __name__ == "__main__":
    caminho_arquivo = 'flights.txt'

    with open(caminho_arquivo, 'r') as TabelaVoos:
        Voos_ida, Voos_Volta = ProcessarDados(TabelaVoos)
    
    
    keyIdas = ["BRUFCO", "LHRFCO", "MADFCO", "DUBFCO", "CDGFCO", "LISFCO"]
    keyVolta = ["FCOBRU", "FCOLHR", "FCOMAD", "FCODUB", "FCOCDG", "FCOLIS"]
    tamanho_populacao =200
    num_geracoes = 100
    teste = False
    

    
    if teste :
        MelhoresGlobalIda = []
        MelhoresGlobalVolta = []
        
        for i in range(30):


            populacaoida = Populacao(Voos_ida, tamanho_populacao, keyIdas, 1)
            populacaovolta = Populacao(Voos_Volta, tamanho_populacao, keyVolta, 0)

            ga1 = AlgoritmoGenetico(populacaoida)
            ga2 = AlgoritmoGenetico(populacaovolta)

            
            resultados = [None, None]
            # Criar as threads
            thread1 = threading.Thread(target=executar_ga1, args=(resultados, 0, ga1, num_geracoes))
            thread2 = threading.Thread(target=executar_ga2, args=(resultados, 1, ga2, num_geracoes))

            thread1.start()
            thread2.start()

            thread1.join()
            thread2.join()

        
            melhor_aptidaoIda, pior_aptidaoIda, media_aptidaoIda, MelhorIda = resultados[0]
            melhor_aptidaoVolta, pior_aptidaoVolta, media_aptidaoVolta, MelhorVolta = resultados[1]
            MelhoresGlobalIda.append(MelhorIda.calcular_aptidao())
            MelhoresGlobalVolta.append(MelhorVolta.calcular_aptidao())
            print(i)
       
        Analise(MelhoresGlobalIda,MelhoresGlobalVolta)
        print ('Média')
        print(f'Média dos Valores de ida: {np.mean(MelhoresGlobalIda)}')
        print(f'Média dos Valores de Volta: {np.mean(MelhoresGlobalVolta)}')
        print('Variância')
        print(f'Variância dos Valores de ida: {np.var(MelhoresGlobalIda)}')
        print(f'Variância dos Valores de Volta: {np.var(MelhoresGlobalVolta)}')
        print('Desvio Padrão')
        print(f'Desvio Padrão dos Valores de ida: {np.std(MelhoresGlobalIda)}')
        print(f'Desvio Padrão dos Valores de Volta: {np.std(MelhoresGlobalVolta)}')
    else: 
         
    
        populacaoida = Populacao(Voos_ida, tamanho_populacao, keyIdas, 1)
        populacaovolta = Populacao(Voos_Volta, tamanho_populacao, keyVolta, 0)

        ga1 = AlgoritmoGenetico(populacaoida)
        ga2 = AlgoritmoGenetico(populacaovolta)

            
        resultados = [None, None]
        thread1 = threading.Thread(target=executar_ga1, args=(resultados, 0, ga1, num_geracoes))
        thread2 = threading.Thread(target=executar_ga2, args=(resultados, 1, ga2, num_geracoes))

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        
        melhor_aptidaoIda, pior_aptidaoIda, media_aptidaoIda, MelhorIda = resultados[0]
        melhor_aptidaoVolta, pior_aptidaoVolta, media_aptidaoVolta, MelhorVolta= resultados[1]
         
        print("Passagem de Ida \n")
        print(MelhorIda)
        print(f'Aptidão do Melhor Indivíduo: {melhor_aptidaoIda[-1]}')
            
        AnaliseEstatistica(media_aptidaoIda, melhor_aptidaoIda, pior_aptidaoIda, 'Ida', num_geracoes)

        print("Passagem de Volta \n")
        print(MelhorVolta)
        print(f'Aptidão do Melhor Indivíduo: {melhor_aptidaoVolta[-1]}')
        AnaliseEstatistica(media_aptidaoVolta, melhor_aptidaoVolta, pior_aptidaoVolta, 'Volta', num_geracoes)
        print("Performace do Melhor conjunto")
        print("ida")
        imprimir_resultados(MelhorIda)
        print("volta")
        imprimir_resultados(MelhorVolta)
       