import random
from rhythm import variar_ritmo
from melody import variar_melodia

def inverter(frase_original): # mantem o ritmo e toca as notas na ordem contraria
    frase_invertida = frase_original[:] 
    frase_invertida.reverse()
    return frase_invertida

def diminuir(frase_original): # mantem as notas e o ritmo, tirando as ultimas duas
    frase_menor = frase_original [:-2]
    return frase_menor

def variar(frase_original, escala_midi): # escolhe dentre os tipos diferentes de variacao disponiveis
    escolhido = random.randint(1,5)
    match escolhido:
        case 1: 
            return variar_ritmo(frase_original)
        case 2: 
            return variar_melodia(frase_original,escala_midi)
        case 3: 
            return inverter(frase_original)
        case 4:
            frase_variada = variar_ritmo(frase_original)
            return variar_melodia(frase_variada, escala_midi)
        case 5:
            return diminuir(frase_original)
