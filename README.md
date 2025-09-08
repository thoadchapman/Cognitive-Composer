# Cognitive Composer: Um Gerador de Melodias

Um projeto em Python que procura aplicar as técnicas de composição discutidas em materiais de Berklee e na ciência da cognição musical.

---

### Filosofia

Esse projeto é a culminação de 7 anos de estudo de composição musical. É uma forma de automatizar a aplicação de técnicas ensinadas por músicos e neurocientistas a fim de produzir um resultado mais musicalmente satisfatório do que uma simples Cadeia de Markov.

O algoritmo trabalha com uma consciência de motivos e figuras melódicas ao invés de pura probabilidade, buscando tornar a geração mais semelhante à forma como o cérebro humano processa música.

### Como Funciona

O processo de composição é dividido em módulos lógicos para simular uma abordagem mais humana:

1.  Geração de Ritmo: Cria a base rítmica para cada frase, utilizando um banco de dados de claves e padrões rítmicos populares. A ideia de analisar o ritmo através de suas propriedades geométricas foi inspirada pelo livro "The Geometry of Musical Rhythm" de Godfried T. Toussaint.
2.  Geração de Melodia Seleciona notas com base em uma combinação de probabilidades estatísticas (inspirado em David Huron) e um sistema de pontuação heurística que modela universais melódicas.
3.  Determinação de Seções: Organiza a peça em estruturas musicais reconhecíveis, como verso e refrão.
4.  Variação de Motivos: Desenvolve as ideias musicais iniciais através de técnicas de variação (inversão, variação rítmica, etc.), garantindo coesão.
5.  Criação de Harmonia Determina e complexifica progressões de acordes comuns para acompanhar a melodia.

### Como Rodar

1.  Certifique-se de ter Python 3 instalado.
2.  Instale as dependências necessárias:
    ```bash
    pip install midiutil
    ```
3.  Execute o script principal:
    ```bash
    python compositor.py
    ```

### Próximos Passos

O objetivo é integrar o maior número de técnicas de forma a otimizar a qualidade generativa do algoritmo. Pretendo aumentar a database de progressões de acordes, tal como adicionar mais formas de variação melódica e rítmica.