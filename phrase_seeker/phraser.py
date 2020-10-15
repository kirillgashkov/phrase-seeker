# Copyright (c) 2019 Kirill Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from typing import Any, Callable, List, Set, Tuple

from phrase_seeker import models


def phrases_from_strings(
    strings: List[str], nlp: Callable[..., Any]
) -> Set[models.Phrase]:
    phrases = set()

    for string in strings:
        doc = nlp(string)
        words = tuple(models.Word(w.text, w.lemma_, w.dep_) for w in doc)
        phrase_words = _convert_to_phrase_words(words)
        phrase = models.Phrase(string, phrase_words)
        phrases.add(phrase)

    return phrases


def _convert_to_phrase_words(
    words: Tuple[models.Word, ...],
) -> Tuple[models.Word, ...]:
    indefinites = {"-PRON-", "someone", "somebody", "something", "somewhere"}

    def should_be_phrase_word(word):
        return word.dep != "case"

    def substitute_for_phrase_word(word):
        if word.lemma in indefinites:
            return models.Word(word.text, "-INDEF-", word.dep)
        return word

    filtered = filter(should_be_phrase_word, words)
    mapped = map(substitute_for_phrase_word, filtered)
    return tuple(mapped)
