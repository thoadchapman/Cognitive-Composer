import random
from data import musical_data
from musical_structures import rhythm
from musical_structures import harmony
from musical_structures.melodics import melody
from infrastructure import infra


def gerar_frase_inteligente(ritmo, tonica_midi, escala_graus, contexto): # recebe o ritmo e comeca a "eleicao" da proxima nota
    frase_melodica = [] 
    for duracao in ritmo: 
        nota_atual = melody.escolher_proxima_nota(contexto, tonica_midi, escala_graus) # escolhe a nota a ser tocada com base nos escores melodicos huron
        frase_melodica.append(nota_atual) # adiciona na lista 
        infra.atualizar_contexto(contexto, nota_atual)
    
    return frase_melodica # retorna a melodia (sem as duracoes)


# TIPOS DE VARIACAO:

def inversao(frase_original): # mantem o ritmo e toca as notas na ordem contraria
    frase_invertida = frase_original[:] 
    frase_invertida.reverse()
    print (f"A frase invertida eh {frase_invertida}")
    return frase_invertida

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
            return melody.variacao_melodica(frase_original,escala_midi)
        case 3: 
            print("Inversao Escolhida!")
            return inversao(frase_original)
        case 4:
            print("Variacao Ritmica + Variacao Melodica Escolhida!")
            frase_variada = rhythm.variacao_ritmica(frase_original)
            return melody.variacao_melodica(frase_variada, escala_midi)
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

    frase_A = infra.definir_evento_musical(melodia_A, ritmo_A) # une a melodia e o ritmo gerados

    escala_midi = [melody.grau_para_midi(g, tonica_midi) for g in escala_graus if g != 'rest']
    escala_midi = [nota for nota in escala_midi if nota is not None] 
    
    frase_A_variada1 = variacao(frase_A, escala_midi)
    frase_A_variada2 = variacao(frase_A, escala_midi)
    
    ritmo_B = rhythm.gerar_motivo_ritmico(musical_data.ONSET_COUNT_WEIGHTS, musical_data.RHYTHM_DNA_DATABASE, musical_data.POSITIONAL_PROPERTY_WEIGHTS)
    melodia_B = gerar_frase_inteligente(ritmo_B, tonica_midi, escala_graus, contexto)
    frase_B = infra.definir_evento_musical(melodia_B, ritmo_B)

    return [frase_A, frase_A_variada1, frase_B, frase_A_variada2]


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

    harmonia_verso = harmony.gerar_progressao_complexa('maior', musical_data.DICT_PROGRESSOES)
    harmonia_refrao = harmony.gerar_progressao_complexa('maior', musical_data.DICT_PROGRESSOES)
    musica_toda = [verso, refrao]
    harmonia_toda = [harmonia_verso, harmonia_refrao]

    infra.salvar_midi("musica_final.mid", musica_toda, harmonia_toda, bpm=120)
    print("Arquivo musica_final.mid salvo com sucesso!")