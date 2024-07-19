
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