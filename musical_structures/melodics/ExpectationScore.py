class ExpectationScore:
    def __init__(self,previous_note,current_note):
        self.previous_note = previous_note
        self.current_note = current_note
        self.leap = self.pitch_proximity()
        self.score = 0

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
    
    def get_score(self):
        score = 0
        score += self.pitch_proximity()
        if self.leap_ascension() is not None:
            score += 1
        self.grade = score
        return score

if __name__ == "__main__":
    test = ExpectationScore(60,63)
    print(test.pitch_proximity())
    test.set_notes(60,65)
    print(test.leap_ascension())
