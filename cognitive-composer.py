from data.musical_data import DICT_PROGRESSOES as progressoes, ESCALAS_MOLDE, gerar_probs_inharmonicas
from musical_structures.rhythm import gerar_ritmo
from musical_structures.harmony import gerar_harmonia
from musical_structures.melodics.melody import gerar_frase
from musical_structures.melodics.variations import variar
from infrastructure.infra import salvar_midi

# GERACAO COMPLETA:

def montar_secao_completa(tonica, escala): # monta uma secao formal completa, como verso e refrao
    ritmo_A = gerar_ritmo()
    frase_A = gerar_frase(ritmo_A,tonica,escala)

    frase_A_variada1 = variar(frase_A, escala)
    frase_A_variada2 = variar(frase_A, escala)
    
    ritmo_B = gerar_ritmo()
    frase_B = gerar_frase(ritmo_B,tonica,escala)

    return [frase_A, frase_A_variada1, frase_B, frase_A_variada2]

if __name__ == "__main__":
    minor_penta = ESCALAS_MOLDE.get('minor_pentatonic')
    major_penta = ESCALAS_MOLDE.get('minor_pentatonic')

    tonica_refrao = 60
    escala_refrao = [int(n) + tonica_refrao for n in major_penta]

    tonica_verso = 57
    escala_verso = [int(n) + tonica_verso for n in minor_penta]

    verso = montar_secao_completa(tonica_verso, escala_verso)
    refrao = montar_secao_completa(tonica_refrao, escala_refrao)

    harmonia_refrao = gerar_harmonia('major')
    harmonia_verso = gerar_harmonia('major')

    musica_toda = [verso, refrao]
    harmonia_toda = [harmonia_verso, harmonia_refrao]

    salvar_midi("musica_final.mid", musica_toda, harmonia_toda, bpm=120)
    print("Arquivo musica_final.mid salvo com sucesso!")