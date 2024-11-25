from wikipedia_harvester import harvest_wikipedia
from ngram_calculator import calculate_ngrams
from ngram_visualizer import visualize_frequencies
from ngram_classifier import classify_text

language_texts = {
    'czech': harvest_wikipedia('czech', [
        'https://cs.wikipedia.org/wiki/Praha',
        'https://cs.wikipedia.org/wiki/Česká_republika'
    ]),
    'english': harvest_wikipedia('english', [
        'https://en.wikipedia.org/wiki/London',
        'https://en.wikipedia.org/wiki/United_Kingdom'
    ]),
    'german': harvest_wikipedia('german', [
        'https://de.wikipedia.org/wiki/Berlin',
        'https://de.wikipedia.org/wiki/Deutschland'
    ]),
    'french': harvest_wikipedia('french', [
        'https://fr.wikipedia.org/wiki/Paris',
        'https://fr.wikipedia.org/wiki/France'
    ]),
    'slovak': harvest_wikipedia('slovak', [
        'https://sk.wikipedia.org/wiki/Bratislava',
        'https://sk.wikipedia.org/wiki/Slovenská_republika'
    ])
}

unigrams, bigrams, trigrams, total_ngrams = calculate_ngrams(language_texts)

visualize_frequencies(
    unigrams=unigrams, 
    bigrams=bigrams, 
    trigrams=trigrams, 
    total_ngrams=total_ngrams, 
    language_texts=language_texts, 
    n=10
)

text = "Bratislava je hlavné mesto Slovenskej republiky."
probabilities = classify_text(text, unigrams, bigrams, trigrams, total_ngrams, N=5)
print(probabilities)
