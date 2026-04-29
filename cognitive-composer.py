import random
from data import musical_data
from musical_structures import rhythm
from musical_structures import harmony
from musical_structures.melodics import melody
from infrastructure import infra
import variations
repertorio = {}

# TIPOS DE VARIACAO:



# GERACAO COMPLETA:

def montar_secao_completa(tonica_midi, escala_graus): # monta uma secao formal completa, como verso e refrao
    contexto = {
        'notas_midi': [],
        'intervalos': []
    } # incializa o historico
    ritmo_A = rhythm.gerar_motivo_ritmico()
    melodia_A = melody.gerar_frase_inteligente(ritmo_A, contexto)

    frase_A = infra.definir_evento_musical(melodia_A, ritmo_A) # une a melodia e o ritmo gerados

    escala_midi = [melody.grau_para_midi(g, tonica_midi) for g in escala_graus if g != 'rest']
    escala_midi = [nota for nota in escala_midi if nota is not None] 
    
    frase_A_variada1 = variations.variar(frase_A, escala_midi)
    frase_A_variada2 = variations.variar(frase_A, escala_midi)
    
    ritmo_B = rhythm.gerar_motivo_ritmico()
    melodia_B = melody.gerar_frase_inteligente(ritmo_B, contexto)
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