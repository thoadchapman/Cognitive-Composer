# do livro 'Sweet Anticipation' de David Huron
PROBABILIDADES_MELODICAS = { '1':{'1':.034,'2':.028,'3':.019,'4':.002,'5':.013,'6':.008,'7':.023,'rest':.036,'#1':6e-5,'b2':2e-5,'#2':1e-5,'b3':2.1e-4,'#4':1.3e-4,'b6':3e-5,'b7':9.9e-4},'#1':{'2':4.2e-4,'3':4e-5,'6':3e-5,'7':2e-5,'rest':2e-5,'#1':4e-5,'#2':1e-5},'b2':{'1':4e-5,'3':1e-5},'2':{'1':.041,'2':.026,'3':.032,'4':.006,'5':.008,'6':.002,'7':.005,'rest':.015,'#1':3.3e-4,'#2':3e-5,'b3':6.6e-4,'#4':1.7e-4,'b7':1.2e-4},'#2':{'3':1.8e-4},'b3':{'1':3e-4,'2':1.08e-3,'4':7.1e-4,'5':1e-4,'rest':1.7e-4,'#2':2e-5,'b3':2.9e-4,'b6':1e-5,'b7':1e-5},'3':{'1':.015,'2':.048,'3':.031,'4':.026,'5':.023,'6':.002,'7':2.9e-4,'rest':.023,'#1':3e-5,'b2':1e-5,'#2':4e-5,'b3':1e-5,'#4':8.8e-4,'#5':3e-5},'4':{'1':5.4e-4,'2':.012,'3':.041,'4':.015,'5':.017,'6':.004,'7':.001,'rest':.005,'#1':1e-5,'b2':1e-5,'b3':8.4e-4,'#4':4e-5,'b6':3e-5,'b7':6e-5},'#4':{'1':3e-5,'2':1.6e-4,'3':3.7e-4,'4':1e-4,'5':2.57e-3,'6':4e-4,'7':3e-5,'rest':1.3e-4,'#5':4e-4,'b6':2e-5},'5':{'1':.025,'2':.005,'3':.028,'4':.036,'5':.048,'6':.020,'7':.003,'rest':.022,'#1':1e-5,'b3':3.7e-4,'#4':2.07e-3,'#5':6e-5,'b6':1.3e-4,'b7':5.4e-4},'#5':{'3':1e-5,'4':1e-5,'6':2.7e-4,'7':3e-5,'rest':2e-5,'#4':1e-5,'#5':6e-5},'b6':{'1':1e-5,'3':1e-5,'4':3e-5,'5':2.1e-4,'rest':2e-5},'6':{'1':2.38e-3,'2':1.68e-3,'3':6.5e-4,'4':3.42e-3,'5':.036,'6':.012,'7':.008,'rest':.004,'#1':4e-5,'#4':3.7e-4,'#5':1.6e-4,'b6':1e-5,'b7':7e-4},'b7':{'1':6.2e-4,'2':3e-5,'3':1e-5,'4':3e-5,'5':4.3e-4,'6':1.19e-3,'rest':2.5e-4,'b3':8e-5,'b6':7e-5,'b7':4.8e-4},'7':{'1':.020,'2':.005,'3':3.5e-4,'4':2.9e-4,'5':3.23e-3,'6':.013,'7':.004,'rest':.002,'#1':3e-5,'#4':4e-5,'#5':4e-5,'b7':1e-5},'rest':{'1':.019,'2':.010,'3':.016,'4':.007,'5':.030,'6':.004,'7':.002,'#1':3e-5,'#2':1e-5,'b3':2.3e-4,'#4':1e-4,'#5':3e-5,'b6':3e-5,'b7':2.7e-4}}
GRAU_PARA_INTERVALO = {'1':0,'#1':1,'b2':1,'2':2,'#2':3,'b3':3,'3':4,'4':5,'#4':6,'b5':6,'5':7,'#5':8,'b6':8,'6':9,'#6':10,'b7':10,'7':11}
INTERVALO_PARA_GRAU = {0:'1',1:'b2',2:'2',3:'b3',4:'3',5:'4',6:'#4',7:'5',8:'b6',9:'6',10:'b7',11:'7'}

PITCH_MAP = {
    'C3':48, 'D3':50, 'E3':52, 'F3':53, 'G3':55, 'A3':57, 'B3':59, 'G#3': 56,
    'C4':60, 'D4':62, 'E4':64, 'F4':65, 'G4':67, 'A4':69, 'B4':71,
    'C5':72, 'D5':74, 'E5':76, 'F5':77, 'G5':79, 'A5':81, 'B5':83
}
NOME_PARA_MIDI = {name: midi for name, midi in PITCH_MAP.items()}
MIDI_PARA_NOME = {midi: name for name, midi in PITCH_MAP.items()}

# do livro 'The Geometry of Rhythm' de Godfried Toussaint
ONSET_COUNT_WEIGHTS = {
    3: 4,   # Ex: Tresillo (muito importante)
    4: 3,   # Ex: Shiko (variante), Fandango
    5: 10,  # O mais comum e o foco principal (Son, Rumba, etc.)
    7: 2,   # Ex: Bembé (importante)
}

RHYTHM_DNA_DATABASE = {
    3: [
        [6, 6, 4],     # Uma variação mais lenta do tresillo
        [5, 5, 6],
        [4, 4, 8],     # Ritmo de dois quartos de nota e uma mínima
    ],
    4: [
        [4, 4, 4, 4],     # Completamente regular (on-beat)
        [3, 3, 4, 6],
        [2, 2, 6, 6],
        [3, 5, 3, 5],
    ],
    5: [
        [3, 3, 4, 2, 4], # Clave Son (o mais importante)
        [4, 2, 4, 2, 4], # Shiko
        [3, 3, 4, 3, 3], # Bossa-Nova
        [3, 4, 3, 2, 4], # Rumba
        [3, 3, 4, 1, 5], # Soukous
        [3, 3, 4, 4, 2], # Gahu
        [3, 3, 3, 3, 4], # Um ritmo muito popular e estável
        [2, 2, 2, 2, 8], # Quatro colcheias e uma mínima
    ],
    7: [
        [2, 2, 1, 2, 2, 2, 5], # Semelhante ao Bembé
        [2, 2, 2, 2, 2, 2, 4], # Um ritmo regular com uma pausa
        [1, 1, 2, 2, 3, 3, 4],
    ]
}

POSITIONAL_PROPERTY_WEIGHTS = {
    "mainbeat onsets": {
        '1': 3,
        '2': 2,
        '3': 1
    }
}

DICT_PROGRESSOES = {
    'maior': {
        'progressoes': [
            # Clássicas
            ['I', 'V', 'vi', 'IV'],
            ['I', 'IV', 'V', 'I'],
            ['vi', 'IV', 'I', 'V'],
            ['I', 'vi', 'IV', 'V'],
            # Progressões de "power" do livro (Lesson 17)
            ['I', 'vi', 'ii', 'V'],  # Conhecida como "progressão dos anos 50"
            ['ii', 'V', 'I', 'I'],
            ['I', 'ii', 'iii', 'IV'],
        ],
        'substituicoes': {
            # Substituições diatônicas
            'IV': ['ii', 'IVmaj7'],
            'V': ['V7'],
            'I': ['Imaj7', 'vi'],
            'vi': ['iii'],
            'iii': ['I'],
            # Acordes emprestados e secundários (Lesson 14)
            'ii': ['V7/V'], # D7 em Dó Maior
            'iii': ['V7/vi'], # E7 em Dó Maior
            'Imaj7': ['V7/IV'], # C7 em Dó Maior
        }
    },

}

ACORDES_MIDI = {
    'I': [48, 52, 55], 'Imaj7': [48, 52, 55, 59], 'ii': [50, 53, 57], 
    'iii': [52, 55, 59], 'IV': [53, 57, 60], 'IVmaj7': [53, 57, 60, 64], 
    'V': [55, 59, 62], 'V7': [55, 59, 62, 65], 'vi': [57, 60, 64],
    'V7/IV': [48, 52, 55, 58], 'V7/V': [50, 54, 57, 60], 'V7/vi': [52, 56, 59, 62]
    }