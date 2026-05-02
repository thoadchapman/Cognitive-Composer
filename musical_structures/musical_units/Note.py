class Note:
    def __init__(self,pitch,duration):
        self.pitch = pitch
        self.duration = duration
    
    def __repr__(self):
        return f'|| pitch: {self.pitch} / dur: {self.duration} '
    
    def get_pitch(self):
        return self.pitch
    
    def get_duration(self):
        return self.duration
    
    def set_pitch(self,p):
        self.pitch = p

    def set_duration(self,d):
        self.duration = d

    def add_duration(self,d):
        self.duration += d

if __name__ == "__main__":
    test = Note(60,4)
    print(test)