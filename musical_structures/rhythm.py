import random
from data import musical_data

ONSET_WEIGHTS_BASE = musical_data.ONSET_COUNT_WEIGHTS
RHYTHM_DNA_BASE = musical_data.RHYTHM_DNA_DATABASE
POS_WEIGHTS_BASE = musical_data.POSITIONAL_PROPERTY_WEIGHTS

def gerar_motivo_ritmico(onset_weights=ONSET_WEIGHTS_BASE, rhythm_dna=RHYTHM_DNA_BASE, pos_weights=POS_WEIGHTS_BASE): # decide uma sequencia de intervalos com base em ritmos e claves populares 
    num_notas = random.choices(list(onset_weights.keys()),weights = list(onset_weights.values()), k=1)[0]

    intervalos = random.choice(rhythm_dna[num_notas])
    print(f'intervalos escolhidos: {intervalos}')
    
    primeiro_onset = random.choices(list(pos_weights['mainbeat onsets'].keys()),weights=list(pos_weights['mainbeat onsets'].values()), k=1)[0]
    print(f'primeiro onset na beat: {primeiro_onset}')
    
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

def variacao_ritmica(frase_original): # mantem as notas e altera a duracao de uma nota
    frase_alterada = [dict(e) for e in frase_original]
    indices_notas = [i for i, e in enumerate(frase_alterada) if e['type'] == 'note']
    
    if len(indices_notas) < 2:
        return frase_original
    
    idx1, idx2 = random.sample(indices_notas, 2)
    
    duracoes = [0.25, 0.5, 1.0, 2.0]
    duracao_antiga = frase_alterada[idx1]['duration']
    nova_duracao = random.choice([d for d in duracoes if d != duracao_antiga])
    
    variacao_duracao = nova_duracao - duracao_antiga
    
    if frase_alterada[idx2]['duration'] - variacao_duracao <= 0:
        print("Variação rítmica ignorada para evitar duração negativa.")
        return frase_original
        
    frase_alterada[idx1]['duration'] = nova_duracao
    frase_alterada[idx2]['duration'] -= variacao_duracao
    
    print(f"Índice {idx1} trocado. Variação de duração: {variacao_duracao:.2f}")
    return frase_alterada