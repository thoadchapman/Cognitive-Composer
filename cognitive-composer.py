import random
from midiutil import MIDIFile

# do livro 'Sweet Anticipation' de David Huron
PROBABILIDADES_MELODICAS = { '1':{'1':.034,'2':.028,'3':.019,'4':.002,'5':.013,'6':.008,'7':.023,'rest':.036,'#1':6e-5,'b2':2e-5,'#2':1e-5,'b3':2.1e-4,'#4':1.3e-4,'b6':3e-5,'b7':9.9e-4},'#1':{'2':4.2e-4,'3':4e-5,'6':3e-5,'7':2e-5,'rest':2e-5,'#1':4e-5,'#2':1e-5},'b2':{'1':4e-5,'3':1e-5},'2':{'1':.041,'2':.026,'3':.032,'4':.006,'5':.008,'6':.002,'7':.005,'rest':.015,'#1':3.3e-4,'#2':3e-5,'b3':6.6e-4,'#4':1.7e-4,'b7':1.2e-4},'#2':{'3':1.8e-4},'b3':{'1':3e-4,'2':1.08e-3,'4':7.1e-4,'5':1e-4,'rest':1.7e-4,'#2':2e-5,'b3':2.9e-4,'b6':1e-5,'b7':1e-5},'3':{'1':.015,'2':.048,'3':.031,'4':.026,'5':.023,'6':.002,'7':2.9e-4,'rest':.023,'#1':3e-5,'b2':1e-5,'#2':4e-5,'b3':1e-5,'#4':8.8e-4,'#5':3e-5},'4':{'1':5.4e-4,'2':.012,'3':.041,'4':.015,'5':.017,'6':.004,'7':.001,'rest':.005,'#1':1e-5,'b2':1e-5,'b3':8.4e-4,'#4':4e-5,'b6':3e-5,'b7':6e-5},'#4':{'1':3e-5,'2':1.6e-4,'3':3.7e-4,'4':1e-4,'5':2.57e-3,'6':4e-4,'7':3e-5,'rest':1.3e-4,'#5':4e-4,'b6':2e-5},'5':{'1':.025,'2':.005,'3':.028,'4':.036,'5':.048,'6':.020,'7':.003,'rest':.022,'#1':1e-5,'b3':3.7e-4,'#4':2.07e-3,'#5':6e-5,'b6':1.3e-4,'b7':5.4e-4},'#5':{'3':1e-5,'4':1e-5,'6':2.7e-4,'7':3e-5,'rest':2e-5,'#4':1e-5,'#5':6e-5},'b6':{'1':1e-5,'3':1e-5,'4':3e-5,'5':2.1e-4,'rest':2e-5},'6':{'1':2.38e-3,'2':1.68e-3,'3':6.5e-4,'4':3.42e-3,'5':.036,'6':.012,'7':.008,'rest':.004,'#1':4e-5,'#4':3.7e-4,'#5':1.6e-4,'b6':1e-5,'b7':7e-4},'b7':{'1':6.2e-4,'2':3e-5,'3':1e-5,'4':3e-5,'5':4.3e-4,'6':1.19e-3,'rest':2.5e-4,'b3':8e-5,'b6':7e-5,'b7':4.8e-4},'7':{'1':.020,'2':.005,'3':3.5e-4,'4':2.9e-4,'5':3.23e-3,'6':.013,'7':.004,'rest':.002,'#1':3e-5,'#4':4e-5,'#5':4e-5,'b7':1e-5},'rest':{'1':.019,'2':.010,'3':.016,'4':.007,'5':.030,'6':.004,'7':.002,'#1':3e-5,'#2':1e-5,'b3':2.3e-4,'#4':1e-4,'#5':3e-5,'b6':3e-5,'b7':2.7e-4}}
GRAU_PARA_INTERVALO = {'1':0,'#1':1,'b2':1,'2':2,'#2':3,'b3':3,'3':4,'4':5,'#4':6,'b5':6,'5':7,'#5':8,'b6':8,'6':9,'#6':10,'b7':10,'7':11}
INTERVALO_PARA_GRAU = {0:'1',1:'b2',2:'2',3:'b3',4:'3',5:'4',6:'#4',7:'5',8:'b6',9:'6',10:'b7',11:'7'}

PITCH_MAP = {
    'C3':48, 'D3':50, 'E3':52, 'F3':53, 'G3':55, 'A3':57, 'B3':59, 'G#3': 56,
    'C4':60, 'D4':62, 'E4':64, 'F4':65, 'G4':67, 'A4':69, 'B4':71,
    'C5':72, 'D5':74, 'E5':76, 'F5':77, 'G5':79, 'A5':81, 'B5':83
}
NOME_PARA_MIDI = {name: midi for name, midi in PITCH_MAP.items()}
MIDI_PARA_NOME = {midi: name for name, midi in PITCH_MAP.items()}

# do livro 'The Geometry of Rhythm' de Godfried Toussaint
ONSET_COUNT_WEIGHTS = {
    3: 4,   # Ex: Tresillo (muito importante)
    4: 3,   # Ex: Shiko (variante), Fandango
    5: 10,  # O mais comum e o foco principal (Son, Rumba, etc.)
    7: 2,   # Ex: Bembé (importante)
}

RHYTHM_DNA_DATABASE = {
    3: [
        [6, 6, 4],     # Uma variação mais lenta do tresillo
        [5, 5, 6],
        [4, 4, 8],     # Ritmo de dois quartos de nota e uma mínima
    ],
    4: [
        [4, 4, 4, 4],     # Completamente regular (on-beat)
        [3, 3, 4, 6],
        [2, 2, 6, 6],
        [3, 5, 3, 5],
    ],
    5: [
        [3, 3, 4, 2, 4], # Clave Son (o mais importante)
        [4, 2, 4, 2, 4], # Shiko
        [3, 3, 4, 3, 3], # Bossa-Nova
        [3, 4, 3, 2, 4], # Rumba
        [3, 3, 4, 1, 5], # Soukous
        [3, 3, 4, 4, 2], # Gahu
        [3, 3, 3, 3, 4], # Um ritmo muito popular e estável
        [2, 2, 2, 2, 8], # Quatro colcheias e uma mínima
    ],
    7: [
        [2, 2, 1, 2, 2, 2, 5], # Semelhante ao Bembé
        [2, 2, 2, 2, 2, 2, 4], # Um ritmo regular com uma pausa
        [1, 1, 2, 2, 3, 3, 4],
    ]
}

POSITIONAL_PROPERTY_WEIGHTS = {
    "mainbeat onsets": {
        '1': 3,
        '2': 2,
        '3': 1
    }
}

DICT_PROGRESSOES = {
    'maior': {
        'progressoes': [
            # Clássicas
            ['I', 'V', 'vi', 'IV'],
            ['I', 'IV', 'V', 'I'],
            ['vi', 'IV', 'I', 'V'],
            ['I', 'vi', 'IV', 'V'],
            # Progressões de "power" do livro (Lesson 17)
            ['I', 'vi', 'ii', 'V'],  # Conhecida como "progressão dos anos 50"
            ['ii', 'V', 'I', 'I'],
            ['I', 'ii', 'iii', 'IV'],
        ],
        'substituicoes': {
            # Substituições diatônicas
            'IV': ['ii', 'IVmaj7'],
            'V': ['V7'],
            'I': ['Imaj7', 'vi'],
            'vi': ['iii'],
            'iii': ['I'],
            # Acordes emprestados e secundários (Lesson 14)
            'ii': ['V7/V'], # D7 em Dó Maior
            'iii': ['V7/vi'], # E7 em Dó Maior
            'Imaj7': ['V7/IV'], # C7 em Dó Maior
        }
    },

}

def midi_para_grau(nota_midi, tonica_midi): # transforma a nota em midi para o seu equivalente em graus
    if nota_midi is None: return 'rest'
    return INTERVALO_PARA_GRAU.get((nota_midi - tonica_midi)%12,'1')

def grau_para_midi(grau, tonica_midi): # transforma o grau para o seu equivalente em midi
    if grau == 'rest': return None
    intervalo = GRAU_PARA_INTERVALO.get((grau))
    return tonica_midi + intervalo if intervalo is not None else None

def gerar_candidatos(grau_anterior, tonica_midi, escala_graus): # procura no dicionario de probabilidades melodicas e cria uma lista com todas que podem ser escolhidas
        transicoes_brutas = PROBABILIDADES_MELODICAS.get(grau_anterior) 
        transicoes_filtradas = {nota:chance for nota,chance in transicoes_brutas.items() if nota in escala_graus}
        
        if not transicoes_filtradas: return [tonica_midi]

        graus_possiveis = list(transicoes_filtradas.keys())
        pesos = list(transicoes_filtradas.values())

        graus_escolhidos = random.choices(graus_possiveis, weights=pesos, k=5)

        midi_escolhidos = [grau_para_midi(grau_escolhido, tonica_midi) for grau_escolhido in graus_escolhidos]

        midi_escolhidos_limpos = [c for c in midi_escolhidos if c is not None]

        return midi_escolhidos_limpos

def gerar_motivo_ritmico(ONSET_COUNT_WEIGHTS, RHYTHM_DNA_DATABASE, POSITIONAL_PROPERTY_WEIGHTS): # decide uma sequencia de intervalos com base em ritmos e claves populares 
    num_notas = random.choices(list(ONSET_COUNT_WEIGHTS.keys()),weights = list(ONSET_COUNT_WEIGHTS.values()), k=1)[0]
    
    intervalos = random.choice(RHYTHM_DNA_DATABASE[num_notas])
    print(f'intervalos escolhidos: {intervalos}')
    
    primeiro_onset = random.choices(list(POSITIONAL_PROPERTY_WEIGHTS['mainbeat onsets'].keys()),weights=list(POSITIONAL_PROPERTY_WEIGHTS['mainbeat onsets'].values()), k=1)[0]
    print(f'primeiro onset na beat: {primeiro_onset}')
    
    onsets = []
    onsets.append(int(primeiro_onset))
    
    for i in range(1, num_notas):
        onset = (onsets[i-1]) + (intervalos[i-1])
        onsets.append(onset)
    
    print (f"Onsets: {onsets}")

    if len(onsets) > 1:
        duracoes = [(onsets[i+1] - onsets[i]) * 0.25 for i in range(len(onsets)-1)]
        duracoes.append((17 - onsets[-1]) * 0.25)
    else:
        duracoes = [4.0] 
    return duracoes

def score_melodico_avancado(pitch_candidato, contexto): # cria um placar que procura a proxima nota mais esperada
    if not contexto['notas_midi']:
        return 100

    ultimo_pitch = contexto['notas_midi'][-1]
    intervalo = pitch_candidato - ultimo_pitch

    if intervalo == 0:
        return 10 

    score_proximidade = max(0, 100 - (abs(intervalo) * 8)) # determina se a proxima nota vai ser um salto 

    score_reversao = 0
    if contexto['intervalos'] and abs(contexto['intervalos'][-1]) > 4: 
        if (intervalo * contexto['intervalos'][-1]) < 0: # determina se a proxima nota muda de direção
            score_reversao = 50
    return score_proximidade + score_reversao    

def escolher_proxima_nota(contexto, tonica_midi, escala_graus): # decide a proxima nota a ser tocada com base na lista de candidatos 
    ultima_nota = contexto['notas_midi'][-1] if contexto['notas_midi'] else tonica_midi
    grau_anterior = midi_para_grau(ultima_nota,tonica_midi)
    candidatos_midi = gerar_candidatos(grau_anterior,tonica_midi,escala_graus)

    if not candidatos_midi: return tonica_midi
    nota_escolhida = sorted(candidatos_midi, key = lambda k:score_melodico_avancado(k,contexto), reverse=True)[random.randint(0,len(candidatos_midi)-1)] # pra ele não tender sempre as opcoes mais obvias

    return nota_escolhida

def atualizar_contexto(contexto, nova_nota_pitch): # atualiza o dicionario 'contexto', que atua como historico
    if contexto['notas_midi']:
        nota_anterior = contexto['notas_midi'][-1]
        intervalo = nova_nota_pitch - nota_anterior
        contexto['intervalos'].append(intervalo)
    contexto['notas_midi'].append(nova_nota_pitch)

def gerar_frase_inteligente(ritmo, tonica_midi, escala_graus, contexto): # recebe o ritmo e comeca a "eleicao" da proxima nota
    frase_melodica = [] 
    for duracao in ritmo: 
        nota_atual = escolher_proxima_nota(contexto, tonica_midi, escala_graus) # escolhe a nota a ser tocada com base nos escores melodicos huron
        frase_melodica.append(nota_atual) # adiciona na lista 
        atualizar_contexto(contexto, nota_atual)
    
    return frase_melodica # retorna a melodia (sem as duracoes)

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

def definir_evento_musical(melodia, ritmo): # recebe uma melodia e um ritmo e os formaliza em um dicionario
    frase_musical = []
    for i in range(len(ritmo)):
        evento_musical = {'type': 'note', 'pitch': melodia[i], 'duration': ritmo[i]} # representa a nota tocada, seu tom e duracao
        frase_musical.append(evento_musical)
    return frase_musical

# TIPOS DE VARIACAO:

def inversao(frase_original): # mantem o ritmo e toca as notas na ordem contraria
    frase_invertida = frase_original[:] 
    frase_invertida.reverse()
    print (f"A frase invertida eh {frase_invertida}")
    return frase_invertida

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
    
    # CORRIGIDO: Impede que a duração de uma nota se torne negativa ou zero
    if frase_alterada[idx2]['duration'] - variacao_duracao <= 0:
        print("Variação rítmica ignorada para evitar duração negativa.")
        return frase_original
        
    frase_alterada[idx1]['duration'] = nova_duracao
    frase_alterada[idx2]['duration'] -= variacao_duracao
    
    print(f"Índice {idx1} trocado. Variação de duração: {variacao_duracao:.2f}")
    return frase_alterada

def variacao_melodica(frase_original, escala_midi): # mantem o ritmo e altera a tonalidade de uma nota
    frase_alterada_melodica = [dict(evento) for evento in frase_original]
    
    indices_de_notas = [i for i, evento in enumerate(frase_alterada_melodica) if evento['type'] == 'note']

    if not indices_de_notas or not escala_midi:
        return frase_original

    indice_a_trocar = random.choice(indices_de_notas)
    
    nota_antiga = frase_alterada_melodica[indice_a_trocar]['pitch']
    nova_nota = nota_antiga


    if len(escala_midi) > 1:
      while nova_nota == nota_antiga:
          nova_nota = random.choice(escala_midi)

    frase_alterada_melodica[indice_a_trocar]['pitch'] = nova_nota
    
    print(f"A nota de índice {indice_a_trocar} foi escolhida. A nova nota eh {nova_nota}")


    return frase_alterada_melodica
    
def diminuir_motivo(frase_original): # mantem as notas e o ritmo, tirando as ultimas duas
    print("Diminuicao Escolhida!")
    frase_menor = frase_original [:-2]
    return frase_menor

def variacao(frase_original, escala_midi): # escolhe dentre os tipos diferentes de variacao disponiveis
    escolhido = random.randint(1,5)
    match escolhido:
        case 1: 
            print("Variacao Ritmica Escolhida!")
            return variacao_ritmica(frase_original)
        case 2: 
            print("Variacao Melodica Escolhida!")
            return variacao_melodica(frase_original,escala_midi)
        case 3: 
            print("Inversao Escolhida!")
            return inversao(frase_original)
        case 4:
            print("Variacao Ritmica + Variacao Melodica Escolhida!")
            frase_variada = variacao_ritmica(frase_original)
            return variacao_melodica(frase_variada, escala_midi)
        case 5:
            return diminuir_motivo(frase_original)

# GERACAO COMPLETA:

def montar_secao_completa(tonica_midi, escala_graus): # monta uma secao formal completa, como verso e refrao
    contexto = {
    'notas_midi': [],
    'intervalos': []
    } # incializa o historico
    ritmo_A = gerar_motivo_ritmico(ONSET_COUNT_WEIGHTS, RHYTHM_DNA_DATABASE, POSITIONAL_PROPERTY_WEIGHTS)
    melodia_A = gerar_frase_inteligente(ritmo_A, tonica_midi, escala_graus, contexto)

    frase_A = definir_evento_musical(melodia_A, ritmo_A) # une a melodia e o ritmo gerados

    escala_midi = [grau_para_midi(g, tonica_midi) for g in escala_graus if g != 'rest']
    escala_midi = [nota for nota in escala_midi if nota is not None] 
    
    frase_A_variada1 = variacao(frase_A, escala_midi)
    frase_A_variada2 = variacao(frase_A, escala_midi)
    
    ritmo_B = gerar_motivo_ritmico(ONSET_COUNT_WEIGHTS, RHYTHM_DNA_DATABASE, POSITIONAL_PROPERTY_WEIGHTS)
    melodia_B = gerar_frase_inteligente(ritmo_B, tonica_midi, escala_graus, contexto)
    frase_B = definir_evento_musical(melodia_B, ritmo_B)

    return [frase_A, frase_A_variada1, frase_B, frase_A_variada2]

def salvar_midi(nome_arquivo, secoes, harmonia, bpm): # transcreve as secoes para arquivos midi usando o midiutil

    ACORDES_MIDI = {
    'I': [48, 52, 55], 'Imaj7': [48, 52, 55, 59], 'ii': [50, 53, 57], 
    'iii': [52, 55, 59], 'IV': [53, 57, 60], 'IVmaj7': [53, 57, 60, 64], 
    'V': [55, 59, 62], 'V7': [55, 59, 62, 65], 'vi': [57, 60, 64],
    'V7/IV': [48, 52, 55, 58], 'V7/V': [50, 54, 57, 60], 'V7/vi': [52, 56, 59, 62]
    }

    arquivo_midi = MIDIFile(2)
    arquivo_midi.addTempo(track=0, time=0, tempo=bpm)
    
    tempo_atual_harmonia = 0.0
    for _ in range(2):
        for secao_harmonia in harmonia:
                for _ in range(2):
                    for acorde_nome in secao_harmonia:
                        if isinstance(acorde_nome, list):
                            acorde_nome = acorde_nome[0]
                    
                        midi_acorde = ACORDES_MIDI.get(acorde_nome, ACORDES_MIDI['I']) 
                    
                        for pitch in midi_acorde:
                            arquivo_midi.addNote(
                                track=1, 
                                channel=0, 
                                pitch=pitch, 
                                time=tempo_atual_harmonia, 
                                duration=4, 
                                volume=60
                            )
                        tempo_atual_harmonia += 4.0
                
    tempo_atual_melodia = 0.0
    for _ in range(2):
        for secao in secoes:
            for _ in range(2):
                for frase in secao:
                    if frase is None:
                        print("Aviso: uma frase musical estava vazia e foi ignorada.")
                        continue
                    for nota in frase:
                        if nota['type'] == 'note':
                            arquivo_midi.addNote(
                                track=0,  
                                channel=0, 
                                pitch=nota['pitch']+12,
                                time=tempo_atual_melodia,
                                duration=nota['duration'], 
                                volume=100
                            )
                        tempo_atual_melodia += nota['duration'] 
                    if tempo_atual_melodia % 4 != 0:
                        tempo_atual_melodia = (int(tempo_atual_melodia / 4) + 1) * 4


    with open(nome_arquivo, "wb") as arquivo_de_saida:
        arquivo_midi.writeFile(arquivo_de_saida)


escala_pentatonica_maior = {'1', '2', '3', '5', '6', 'rest'} 
grau_inicial = '1'
tonica = 60



if __name__ == "__main__":

    tonica_refrao = 60
    escala_refrao = escala_pentatonica_maior

    tonica_verso = 60
    escala_verso = escala_pentatonica_maior

    verso = montar_secao_completa(tonica_verso, escala_verso)

    refrao = montar_secao_completa(tonica_refrao, escala_refrao)

    harmonia_verso = gerar_progressao_complexa('maior', DICT_PROGRESSOES)
    harmonia_refrao = gerar_progressao_complexa('maior', DICT_PROGRESSOES)
    musica_toda = [verso, refrao]
    harmonia_toda = [harmonia_verso, harmonia_refrao]

    salvar_midi("musica_final.mid", musica_toda, harmonia_toda, bpm=120)
    print("Arquivo musica_final.mid salvo com sucesso!")