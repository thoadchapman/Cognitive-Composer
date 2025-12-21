import random
from data import musical_data
from musical_structures import rhythm
from midiutil import MIDIFile

def midi_para_grau(nota_midi, tonica_midi): # transforma a nota em midi para o seu equivalente em graus
    if nota_midi is None: return 'rest'
    return musical_data.INTERVALO_PARA_GRAU.get((nota_midi - tonica_midi)%12,'1')

def grau_para_midi(grau, tonica_midi): # transforma o grau para o seu equivalente em midi
    if grau == 'rest': return None
    intervalo = musical_data.GRAU_PARA_INTERVALO.get((grau))
    return tonica_midi + intervalo if intervalo is not None else None

def gerar_candidatos(grau_anterior, tonica_midi, escala_graus): # procura no dicionario de probabilidades melodicas e cria uma lista com todas que podem ser escolhidas
        transicoes_brutas = musical_data.PROBABILIDADES_MELODICAS.get(grau_anterior) 
        transicoes_filtradas = {nota:chance for nota,chance in transicoes_brutas.items() if nota in escala_graus}
        
        if not transicoes_filtradas: return [tonica_midi]

        graus_possiveis = list(transicoes_filtradas.keys())
        pesos = list(transicoes_filtradas.values())

        graus_escolhidos = random.choices(graus_possiveis, weights=pesos, k=5)

        midi_escolhidos = [grau_para_midi(grau_escolhido, tonica_midi) for grau_escolhido in graus_escolhidos]

        midi_escolhidos_limpos = [c for c in midi_escolhidos if c is not None]

        return midi_escolhidos_limpos


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
            return rhythm.variacao_ritmica(frase_original)
        case 2: 
            print("Variacao Melodica Escolhida!")
            return variacao_melodica(frase_original,escala_midi)
        case 3: 
            print("Inversao Escolhida!")
            return inversao(frase_original)
        case 4:
            print("Variacao Ritmica + Variacao Melodica Escolhida!")
            frase_variada = rhythm.variacao_ritmica(frase_original)
            return variacao_melodica(frase_variada, escala_midi)
        case 5:
            return diminuir_motivo(frase_original)

# GERACAO COMPLETA:

def montar_secao_completa(tonica_midi, escala_graus): # monta uma secao formal completa, como verso e refrao
    contexto = {
    'notas_midi': [],
    'intervalos': []
    } # incializa o historico
    ritmo_A = rhythm.gerar_motivo_ritmico(musical_data.ONSET_COUNT_WEIGHTS, musical_data.RHYTHM_DNA_DATABASE, musical_data.POSITIONAL_PROPERTY_WEIGHTS)
    melodia_A = gerar_frase_inteligente(ritmo_A, tonica_midi, escala_graus, contexto)

    frase_A = definir_evento_musical(melodia_A, ritmo_A) # une a melodia e o ritmo gerados

    escala_midi = [grau_para_midi(g, tonica_midi) for g in escala_graus if g != 'rest']
    escala_midi = [nota for nota in escala_midi if nota is not None] 
    
    frase_A_variada1 = variacao(frase_A, escala_midi)
    frase_A_variada2 = variacao(frase_A, escala_midi)
    
    ritmo_B = rhythm.gerar_motivo_ritmico(musical_data.ONSET_COUNT_WEIGHTS, musical_data.RHYTHM_DNA_DATABASE, musical_data.POSITIONAL_PROPERTY_WEIGHTS)
    melodia_B = gerar_frase_inteligente(ritmo_B, tonica_midi, escala_graus, contexto)
    frase_B = definir_evento_musical(melodia_B, ritmo_B)

    return [frase_A, frase_A_variada1, frase_B, frase_A_variada2]

def salvar_midi(nome_arquivo, secoes, harmonia, bpm): # transcreve as secoes para arquivos midi usando o midiutil



    arquivo_midi = MIDIFile(2)
    arquivo_midi.addTempo(track=0, time=0, tempo=bpm)
    
    tempo_atual_harmonia = 0.0
    for _ in range(2):
        for secao_harmonia in harmonia:
                for _ in range(2):
                    for acorde_nome in secao_harmonia:
                        if isinstance(acorde_nome, list):
                            acorde_nome = acorde_nome[0]
                    
                        midi_acorde = musical_data.ACORDES_MIDI.get(acorde_nome, musical_data.ACORDES_MIDI['I']) 
                    
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

    harmonia_verso = gerar_progressao_complexa('maior', musical_data.DICT_PROGRESSOES)
    harmonia_refrao = gerar_progressao_complexa('maior', musical_data.DICT_PROGRESSOES)
    musica_toda = [verso, refrao]
    harmonia_toda = [harmonia_verso, harmonia_refrao]

    salvar_midi("musica_final.mid", musica_toda, harmonia_toda, bpm=120)
    print("Arquivo musica_final.mid salvo com sucesso!")