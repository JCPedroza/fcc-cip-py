from string import punctuation
from collections import Counter


def word_split(text: str) -> list[str]:
    punctuation_remover = str.maketrans('', '', punctuation)
    return (text
            .translate(punctuation_remover)
            .lower()
            .split())


def word_count(text: str) -> Counter:
    return Counter(word_split(text))


def word_frequency(text: str = '', topn: int = 1) -> list[tuple[str, int]]:
    return sorted(list(word_count(text).items()),
                  key=lambda item: item[1],
                  reverse=True)[0:topn]
