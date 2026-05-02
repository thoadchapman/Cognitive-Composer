from random import randint, choice, choices
from data.musical_data import PROBABILIDADES_INHARMONICAS as probabilidades, ESCALAS_MOLDE
from musical_structures.musical_units.Phrase import Phrase
from musical_structures.musical_units.Note import Note
from musical_structures.melodics.ExpectationScore import ExpectationScore

TONICA_BASE = 60
ESCALA_BASE = ESCALAS_MOLDE.get('major_pentatonic')

def gerar_frase(ritmo, tonica_midi=TONICA_BASE, escala=ESCALA_BASE): # recebe o ritmo e comeca a "eleicao" da proxima nota
    PRIMEIRA_NOTA = Note(TONICA_BASE, ritmo[0])
    notas = [PRIMEIRA_NOTA] 
    for i in range(1,len(ritmo)): 
        nota_atual = escolher_proxima_nota(notas[i-1].get_pitch(), tonica_midi, escala)
        notas.append(Note(nota_atual,ritmo[i])) 
    return Phrase(notas) 

def gerar_candidatos(ultimo_midi, tonica_midi=TONICA_BASE, escala=ESCALA_BASE): # procura no dicionario de probabilidades melodicas e cria uma lista com todas que podem ser escolhidas
        print(f'----- NOVA NOTA -----')
        
        ultimo_intervalo = ultimo_midi - tonica_midi
        escala_intervalos = [int(i)-tonica_midi for i in escala]
        possiveis_continuacoes = probabilidades.get(ultimo_intervalo)
        print(f'POSSIVEIS CONTINUACOES ITEMS: {possiveis_continuacoes.items()}')
        print(f'ESCALA: {escala_intervalos}')        
        transicoes_filtradas = {intervalo:chance for intervalo, chance in possiveis_continuacoes.items() if intervalo in escala_intervalos}
        
        print(f'transicoes_filtradas: {transicoes_filtradas}')
        if not transicoes_filtradas: return [tonica_midi]
        notas_possiveis = list(transicoes_filtradas.keys())
        pesos = list(transicoes_filtradas.values())

        notas_escolhidas = choices(notas_possiveis, weights=pesos, k=1)

        return notas_escolhidas

def score_melodico_avancado(nota_candidata, ultima_nota): # cria um placar que procura a proxima nota mais esperada
    if not ultima_nota:
        return 
    medidor_de_expectativa = ExpectationScore(nota_candidata,ultima_nota)
    score = medidor_de_expectativa.get_score()
    print(f'score {ultima_nota} -> {nota_candidata}: {score}')
    return score

def escolher_proxima_nota(ultimo_midi, tonica_midi, escala_graus): # decide a proxima nota a ser tocada com base na lista de candidatos 
    candidatos_midi = gerar_candidatos(ultimo_midi,tonica_midi,escala_graus)

    if not candidatos_midi: return tonica_midi
    scores = sorted(candidatos_midi, key = lambda k:score_melodico_avancado(k,ultimo_midi)) # pra ele não tender sempre as opcoes mais obvias
    indice_aleatorio = randint(0, len(scores)-1)
    nota_escolhida = scores[indice_aleatorio]
    return nota_escolhida+tonica_midi

def variar_melodia(frase_original, escala_midi): 
    return frase_original.variar_melodia(escala_midi)
