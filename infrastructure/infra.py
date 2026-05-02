from data import musical_data
from midiutil import MIDIFile

def salvar_midi(nome_arquivo, secoes, harmonia, bpm): # transcreve as secoes para arquivos midi usando o midiutil
    OITAVA = 12
    
    arquivo_midi = MIDIFile(2)
    arquivo_midi.addTempo(track=0, time=0, tempo=bpm)
    arquivo_midi.addTempo(track=1, time=0, tempo=bpm)

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
                    notas = frase.get_notes()
                    for nota in notas:
                            duracao = nota.get_duration()
                            if duracao <= 0:
                                duracao = 0.5
                            arquivo_midi.addNote(
                                track=0,  
                                channel=0, 
                                pitch= nota.get_pitch(),
                                time=tempo_atual_melodia,
                                duration=duracao, 
                                volume=100
                            )
                            tempo_atual_melodia += duracao
                    if tempo_atual_melodia % 4 != 0:
                        tempo_atual_melodia = (int(tempo_atual_melodia / 4) + 1) * 4

    with open(nome_arquivo, "wb") as arquivo_de_saida:
        arquivo_midi.writeFile(arquivo_de_saida)
