class MelodicUniversals:
    def __init__(self,previous_note,current_note):
        self.previous_note = previous_note 
        self.current_note = current_note
            
        self.SCORES = {
            'expected': 100,
            'somewhat_expected': 50,
            'unexpected': 10
        }

    def pitch_proximity(self):
        step_distance = 2
        distance_abs = abs(self.current_note - self.previous_note)
        if distance_abs <= step_distance: return self.SCORES['expected']
        else: return self.SCORES['somewhat_expected']
    
    

if __name__ == "__main__":
    test = MelodicUniversals(60,63)
    print(test.pitch_proximity())
