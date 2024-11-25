import math
import re
from collections import defaultdict
from tokenizer import tokenize
from lang_keywords import get_keywords
from lang_patterns import get_patterns


def train(language: str, code_samples: list, token_frequencies: defaultdict,
          keyword_frequencies: defaultdict, pattern_frequencies: defaultdict,
          total_tokens: defaultdict):
    """Natrénuje klasifikátor na vzorcích kódu"""
    keywords = get_keywords()
    patterns = get_patterns()

    for sample in code_samples:
        # Tokenizace kódu
        tokens = tokenize(sample)
        for token in tokens:
            token_frequencies[language][token] += 1
            total_tokens[language] += 1

        # Zpracování klíčových slov
        if language in keywords:
            for keyword in keywords[language]:
                count = len(re.findall(r'\b' + re.escape(keyword) + r'\b', sample))
                keyword_frequencies[language][keyword] += count

        # Zpracování vzorů
        if language in patterns:
            for pattern in patterns[language]:
                count = len(re.findall(pattern, sample))
                pattern_frequencies[language][pattern] += count


def calculate_probability(feature: str, frequencies: defaultdict, total: int,
                          language: str, vocab_size: int, smoothing_factor: float) -> float:
    """Vypočítá pravděpodobnost pro daný feature"""
    count = frequencies[language].get(feature, 0)
    return (count + smoothing_factor) / (total + smoothing_factor * vocab_size)


def classify(code: str, token_frequencies: defaultdict, total_tokens: defaultdict,
             smoothing_factor: float, min_probability: float) -> dict:
    """Klasifikuje kód a vrátí pravděpodobnosti pro jednotlivé jazyky"""
    scores = defaultdict(float)
    keywords = get_keywords()
    patterns = get_patterns()

    tokens = tokenize(code)

    for language in total_tokens.keys():
        # Token skóre
        vocab_size = len(token_frequencies[language])
        for token in tokens:
            prob = calculate_probability(token, token_frequencies, total_tokens[language],
                                         language, vocab_size, smoothing_factor)
            scores[language] += math.log(max(prob, min_probability))

        # Keyword skóre
        if language in keywords:
            for keyword in keywords[language]:
                count = len(re.findall(r'\b' + re.escape(keyword) + r'\b', code))
                if count > 0:
                    scores[language] += math.log(0.8)  # bonus za každé klíčové slovo

        # Pattern skóre
        if language in patterns:
            for pattern in patterns[language]:
                count = len(re.findall(pattern, code))
                if count > 0:
                    scores[language] += math.log(0.9)  # bonus za každý pattern

    # Normalizace skóre
    max_score = max(scores.values())
    probabilities = {lang: math.exp(score - max_score)
                     for lang, score in scores.items()}

    total = sum(probabilities.values())
    probabilities = {lang: prob / total for lang, prob in probabilities.items()}

    return probabilities


def explain_classification(code: str, token_frequencies: defaultdict,
                           total_tokens: defaultdict) -> dict:
    """Vysvětlí, proč byl kód klasifikován daným způsobem"""
    explanation = defaultdict(list)
    keywords = get_keywords()
    patterns = get_patterns()

    for language in total_tokens.keys():
        # Nalezená klíčová slova
        if language in keywords:
            found_keywords = [
                keyword for keyword in keywords[language]
                if re.search(r'\b' + re.escape(keyword) + r'\b', code)
            ]
            if found_keywords:
                explanation[language].append(f"Found keywords: {', '.join(found_keywords)}")

        # Nalezené vzory
        if language in patterns:
            found_patterns = [
                pattern for pattern in patterns[language]
                if re.search(pattern, code)
            ]
            if found_patterns:
                explanation[language].append(f"Found {len(found_patterns)} characteristic patterns")

    return dict(explanation)
