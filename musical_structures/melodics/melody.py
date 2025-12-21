import random
from data import musical_data

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