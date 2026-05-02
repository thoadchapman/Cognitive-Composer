import random
from data import musical_data

PROGRESSOES = musical_data.DICT_PROGRESSOES

def gerar_harmonia(tonalidade): # escolhe uma progressao comum e deixa mais complexa com substituicoes funcionais
    if tonalidade == None: tonalidade = 'major'
    progressao_escolhida = random.choice(PROGRESSOES[tonalidade]['progressoes'])
    substituicoes = PROGRESSOES[tonalidade]['substituicoes']
    progressao_nova = []
    for acorde in progressao_escolhida:
        if acorde in substituicoes and random.random() < 0.4: # adiciona uma chance em 40% de substituir o acorde
            progressao_nova.append(random.choice(substituicoes[acorde]))
        else:
            progressao_nova.append(acorde)
    return progressao_nova