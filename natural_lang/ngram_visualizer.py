import matplotlib.pyplot as plt


def visualize_frequencies(unigrams: dict, bigrams: dict, trigrams: dict, 
                          total_ngrams: dict, language_texts: dict, n=10):
    plt.figure(figsize=(20, 5))

    # Unigrams
    plt.subplot(131)
    for language in language_texts.keys():
        freq = {k: v/total_ngrams[language]['uni'] for k, v in unigrams[language].items()}
        top_chars = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:n])
        plt.plot(range(len(top_chars)), list(top_chars.values()), 
                 label=language, marker='o')
        plt.xticks(range(len(top_chars)), list(top_chars.keys()))
    plt.title('Top Unigram Frequencies')
    plt.legend()

    # Bigrams
    plt.subplot(132)
    for language in language_texts.keys():
        freq = {k: v/total_ngrams[language]['bi'] for k, v in bigrams[language].items()}
        top_bigrams = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:n])
        plt.plot(range(len(top_bigrams)), list(top_bigrams.values()), 
                 label=language, marker='o')
        plt.xticks(range(len(top_bigrams)), list(top_bigrams.keys()), rotation=45)
    plt.title('Top Bigram Frequencies')
    plt.legend()

    # Trigrams
    plt.subplot(133)
    for language in language_texts.keys():
        freq = {k: v/total_ngrams[language]['tri'] for k, v in trigrams[language].items()}
        top_trigrams = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:n])
        plt.plot(range(len(top_trigrams)), list(top_trigrams.values()), 
                 label=language, marker='o')
        plt.xticks(range(len(top_trigrams)), list(top_trigrams.keys()), rotation=45)
    plt.title('Top Trigram Frequencies')
    plt.legend()

    plt.tight_layout()
    plt.savefig("results/top_ngrams.png")
