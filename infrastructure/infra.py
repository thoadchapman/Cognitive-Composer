from data import musical_data
from midiutil import MIDIFile

def atualizar_contexto(contexto, nova_nota_pitch): # atualiza o dicionario 'contexto', que atua como historico
    if contexto['notas_midi']:
        nota_anterior = contexto['notas_midi'][-1]
        intervalo = nova_nota_pitch - nota_anterior
        contexto['intervalos'].append(intervalo)
    contexto['notas_midi'].append(nova_nota_pitch)

def definir_evento_musical(melodia, ritmo): # recebe uma melodia e um ritmo e os formaliza em um dicionario
    frase_musical = []
    for i in range(len(ritmo)):
        evento_musical = {'type': 'note', 'pitch': melodia[i], 'duration': ritmo[i]} # representa a nota tocada, seu tom e duracao
        frase_musical.append(evento_musical)
    return frase_musical

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
