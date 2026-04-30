from Note import Note

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
