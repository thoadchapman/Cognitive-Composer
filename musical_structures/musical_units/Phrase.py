from Note import Note

class Phrase:
    def __init__(self,notes):
        self.notes = notes

    def __repr__(self):
        return f'{self.notes}'

if __name__ == "__main__":
    test1 = Note(60,4)
    test2 = Note(63,4)
    test3 = Note(65,4)

    notes = [test1,test2,test3]

    phrase1 = Phrase(notes)

    print(phrase1)