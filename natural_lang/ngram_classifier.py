import re
import random
import math
from collections import defaultdict


def select_random_ngrams(text: str, N: int):
    text = re.sub(r'[^a-zA-ZáčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ\s]', '', text.lower())
    
    # Vytvoření všech možných n-gramů
    unigrams = [(i, text[i]) for i in range(len(text)) if text[i].strip()]
    bigrams = [(i, text[i:i+2]) for i in range(len(text)-1) if text[i:i+2].strip()]
    trigrams = [(i, text[i:i+3]) for i in range(len(text)-2) if text[i:i+3].strip()]

    # Náhodný výběr
    selected_unigrams = random.sample(unigrams, min(N, len(unigrams)))
    selected_bigrams = random.sample(bigrams, min(N, len(bigrams)))
    selected_trigrams = random.sample(trigrams, min(N, len(trigrams)))

    return selected_unigrams, selected_bigrams, selected_trigrams

def classify_text(text: str, unigrams: dict, bigrams: dict, trigrams: dict, total_ngrams: dict, N: int = 5, min_probability: float = 1e-10):
    """Classify text based on n-gram analysis."""
    selected_uni, selected_bi, selected_tri = select_random_ngrams(text, N)
    
    scores = defaultdict(float)
    
    for language in total_ngrams.keys():
        # Unigrams
        for _, ngram in selected_uni:
            prob = (unigrams[language].get(ngram, 0) + 1) / \
                   (total_ngrams[language]['uni'] + len(unigrams[language]))
            scores[language] += math.log(max(prob, min_probability))

        # Bigrams
        for _, ngram in selected_bi:
            prob = (bigrams[language].get(ngram, 0) + 1) / \
                   (total_ngrams[language]['bi'] + len(bigrams[language]))
            scores[language] += math.log(max(prob, min_probability))

        # Trigrams
        for _, ngram in selected_tri:
            prob = (trigrams[language].get(ngram, 0) + 1) / \
                   (total_ngrams[language]['tri'] + len(trigrams[language]))
            scores[language] += math.log(max(prob, min_probability))

    # Normalizace a převod zpět z logaritmického prostoru
    max_score = max(scores.values())
    probabilities = {lang: math.exp(score - max_score) for lang, score in scores.items()}
    
    # Normalizace na součet 1
    total = sum(probabilities.values())
    probabilities = {lang: prob / total for lang, prob in probabilities.items()}
    
    return probabilities
