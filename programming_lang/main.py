from classifier import train, classify, explain_classification
from collections import defaultdict

# Inicializace datových struktur pro uložení frekvencí
token_frequencies = defaultdict(lambda: defaultdict(int))
keyword_frequencies = defaultdict(lambda: defaultdict(int))
pattern_frequencies = defaultdict(lambda: defaultdict(int))
total_tokens = defaultdict(int)

# Trénování na vzorcích kódu
python_samples = [
    """
    def hello_world():
        print("Hello, World!")
        return True
    """
]

javascript_samples = [
    """
    const calculateSum = (a, b) => a + b;
    """,
    """
    function helloWorld() {
        console.log("Hello, World!")
        return true
    }
    """
]

train('python', python_samples, token_frequencies, keyword_frequencies, pattern_frequencies, total_tokens)
train('javascript', javascript_samples, token_frequencies, keyword_frequencies, pattern_frequencies, total_tokens)

# Klasifikace kódu
code = """
    calculate_sum = (a, b) => a + b
"""

probabilities = classify(code, token_frequencies, total_tokens, smoothing_factor=0.1, min_probability=1e-5)
print("Probabilities:", probabilities)

explanation = explain_classification(code, token_frequencies, total_tokens)
print("Explanation:", explanation)
