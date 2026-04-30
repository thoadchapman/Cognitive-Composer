class Note:
    def __init__(self,pitch,duration):
        self.pitch = pitch
        self.duration = duration
    
    def __repr__(self):
        return f'|| pitch: {self.pitch} / dur: {self.duration} '
    
if __name__ == "__main__":
    test = Note(60,4)
    print(test)