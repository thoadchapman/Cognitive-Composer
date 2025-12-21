import random

def gerar_progressao_complexa(tonalidade, DICT_PROGRESSOES): # escolhe uma progressao comum e deixa mais complexa com substituicoes funcionais
    if tonalidade == None: tonalidade = 'maior'
    progressao_escolhida = random.choice(DICT_PROGRESSOES[tonalidade]['progressoes'])
    substituicoes = DICT_PROGRESSOES[tonalidade]['substituicoes']
    progressao_nova = []
    for acorde in progressao_escolhida:
        if acorde in substituicoes and random.random() < 0.4: # adiciona uma chance em 40% de substituir o acorde
            progressao_nova.append(random.choice(substituicoes[acorde]))
        else:
            progressao_nova.append(acorde)
    return progressao_nova