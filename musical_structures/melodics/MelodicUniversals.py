class MelodicUniversals:
    def __init__(self,previous_note,current_note):
        self.set_notes(previous_note,current_note)
        self.leap = self.pitch_proximity()
        self.SCORES = {
            'expected': 100,
            'somewhat_expected': 50,
            'unexpected': 10
        }
    
    def set_notes(self,previous_note,current_note):
        self.previous_note = previous_note 
        self.current_note = current_note

    def calculate_proximity(self):
        return self.current_note - self.previous_note

    def pitch_proximity(self):
        step_distance = 2
        distance_abs = abs(self.calculate_proximity())
        return False if distance_abs <= step_distance else True

    def leap_ascension(self):
        if not self.leap: return
        return False if self.calculate_proximity() <= 0 else True
    
    

if __name__ == "__main__":
    test = MelodicUniversals(60,63)
    print(test.pitch_proximity())
    test.set_notes(60,65)
    print(test.leap_ascension())
