from collections import defaultdict


def calculate_ngrams(language_texts: dict):
    """Calculate n-gram frequencies for all languages."""
    unigrams = defaultdict(lambda: defaultdict(int))
    bigrams = defaultdict(lambda: defaultdict(int))
    trigrams = defaultdict(lambda: defaultdict(int))
    total_ngrams = defaultdict(lambda: {'uni': 0, 'bi': 0, 'tri': 0})

    for language, text in language_texts.items():
        # Unigrams
        for char in text:
            if char.strip():
                unigrams[language][char] += 1
                total_ngrams[language]['uni'] += 1

        # Bigrams
        for i in range(len(text) - 1):
            bigram = text[i:i+2]
            if bigram.strip():
                bigrams[language][bigram] += 1
                total_ngrams[language]['bi'] += 1

        # Trigrams
        for i in range(len(text) - 2):
            trigram = text[i:i+3]
            if trigram.strip():
                trigrams[language][trigram] += 1
                total_ngrams[language]['tri'] += 1

    return unigrams, bigrams, trigrams, total_ngrams
