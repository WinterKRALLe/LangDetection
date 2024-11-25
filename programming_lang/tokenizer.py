import re
from typing import List


def tokenize(code: str) -> List[str]:
    """Tokenizuje kód na jednotlivé tokeny"""
    # Odstranění komentářů
    code = re.sub(r'#.*$|//.*$|/\*[\s\S]*?\*/', '', code, flags=re.MULTILINE)
    # Rozdělení na tokeny
    tokens = re.findall(r'\b\w+\b|[^\w\s]', code)
    return tokens
