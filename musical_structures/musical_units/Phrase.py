from random import choice, sample
from musical_structures.musical_units import Note

class Phrase:
    def __init__(self,notes):
        self.notes = notes

    def __repr__(self):
        return f'{", ".join(str(note) for note in self.notes)}'
    
    def __len__(self):
        return len(self.notes)
    
    def __add__(self,other):
        new_notes = self.notes.copy()
        if isinstance(other,Note):
            new_notes.append(other)
        elif isinstance(other,Phrase):    
            new_notes.extend(other.notes)
        return Phrase(new_notes)
    
    def __iadd__(self,other):
        new_notes = self.notes.copy()
        if isinstance(other,Note):
            new_notes.append(other)
        elif isinstance(other,Phrase):    
            new_notes.extend(other.notes)
        self.notes = new_notes
        return self
    
    def get_notes(self):
        return self.notes
    
    def inverter(self):
        nova_frase = self.notes.copy()
        nova_frase.reverse()
        return Phrase(nova_frase)

    def diminuir(self):
        nova_frase = self.notes.copy()
        nova_frase = nova_frase[:-2]
        return Phrase(nova_frase)

    def variar_ritmo(self):    
        nova_frase = self.notes.copy()
        nota1, nota2 = sample(nova_frase, 2)
        
        duracoes = [0.25, 0.5, 1.0, 2.0]
        duracao_antiga = nota1.get_duration()
        nova_duracao = choice([d for d in duracoes if d != duracao_antiga])
        variacao_duracao = nova_duracao - duracao_antiga
        
        if nota2.get_duration() - variacao_duracao <= 0:
            print("Variação rítmica ignorada para evitar duração negativa.")
            return self
            
        nota1.set_duration(nova_duracao)
        nota2.add_duration(-variacao_duracao)
        return Phrase(nova_frase)   

    def variar_melodia(self, escala_midi):
        nova_frase = self.notes.copy()
        nota = choice(nova_frase)
        nota.set_pitch(choice(escala_midi))
        return Phrase(nova_frase)

if __name__ == "__main__":
    test1 = Note(60,4)
    test2 = Note(63,4)
    test3 = Note(65,4)

    notes = [test1,test2,test3]

    phrase1 = Phrase(notes)
    phrase2 = Phrase(notes[::-1])

    phrase3 = phrase1 + phrase2
    print(f'add method test: {phrase3}')

    phrase1 += test1
    print(f'addi method test: {phrase1}')
