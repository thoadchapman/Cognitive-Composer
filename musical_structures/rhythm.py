import random
from data import musical_data

ONSET_WEIGHTS_BASE = musical_data.ONSET_COUNT_WEIGHTS
RHYTHM_DNA_BASE = musical_data.RHYTHM_DNA_DATABASE
POS_WEIGHTS_BASE = musical_data.POSITIONAL_PROPERTY_WEIGHTS

def gerar_ritmo(onset_weights=ONSET_WEIGHTS_BASE, rhythm_dna=RHYTHM_DNA_BASE, pos_weights=POS_WEIGHTS_BASE): # decide uma sequencia de intervalos com base em ritmos e claves populares 
    num_notas = random.choices(list(onset_weights.keys()),weights = list(onset_weights.values()), k=1)[0]

    intervalos = random.choice(rhythm_dna[num_notas])
    
    primeiro_onset = random.choices(list(pos_weights['mainbeat onsets'].keys()),weights=list(pos_weights['mainbeat onsets'].values()), k=1)[0]
    
    onsets = []
    onsets.append(int(primeiro_onset))
    
    for i in range(1, num_notas):
        onset = (onsets[i-1]) + (intervalos[i-1])
        onsets.append(onset)
    
    print (f"Onsets: {onsets}")

    return onset_to_duracoes(onsets)

def onset_to_duracoes(onsets):
    if len(onsets) > 1:
        duracoes = [(onsets[i+1] - onsets[i]) * 0.25 for i in range(len(onsets)-1)]
        duracoes.append((17 - onsets[-1]) * 0.25)
    else:
        duracoes = [4.0] 
    return duracoes    

def variar_ritmo(frase_original): # mantem as notas e altera a duracao de uma nota
    return frase_original.variar_ritmo()