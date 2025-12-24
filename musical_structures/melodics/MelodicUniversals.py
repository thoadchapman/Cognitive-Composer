class MelodicUniversals:
    def __init__(self,previous_note,current_note):
        self.previous_note = previous_note 
        self.current_note = current_note
            
        self.SCORES = {
            'expected': 100,
            'somewhat_expected': 50,
            'unexpected': 10
        }
        

