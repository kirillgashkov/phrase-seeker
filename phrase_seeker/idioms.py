# Copyright (c) 2019 Kirill Gashkov
#
# Distributed under MIT License. See LICENSE file for details.


import copy
import dataclasses
import itertools
from typing import List

from idiom_seeker import downgrader


SBJ_DEPS = {'nsubj', 'csubj', 'dobj', 'pobj', 'dative'}
SBJDLR_DEPS = {'poss'}


@dataclasses.dataclass
class Idiom:
    """
    A container for the words of the idiom, textual representation, lemmas and
    placeholder deps.
    """

    words: List[downgrader.Word]
    text: str = dataclasses.field(init=False)
    lemmas: List[str] = dataclasses.field(init=False)
    placeholder_deps: List[str] = dataclasses.field(init=False)

    def __post_init__(self):
        self.text = ' '.join([w.text for w in self.words])
        self.lemmas = [w.lemma for w in self.words]

        self.placeholder_deps = set()
        if '-SBJ-' in self.lemmas:
            self.placeholder_deps |= SBJ_DEPS
        if '-SBJ$-' in self.lemmas:
            self.placeholder_deps |= SBJDLR_DEPS


def _adapt_idiom(source_idiom):
    adapted_words = []
    for source_word in source_idiom.split():
        if source_word == 'SBJ$':
            adapted_words.append('her')
        elif source_word == 'SBJ':
            adapted_words.append('she')
        else:
            word, pos = source_word.split(sep='/')
            shortened_words = {"'m", "'s", "'re", "n't"}
            if word in shortened_words:
                adapted_words[-1] += word
            else:
                adapted_words.append(word)
    return ' '.join(adapted_words)


def _insert_placeholders(words):
    cleaned_words = []
    for word in words:
        cleaned_word = copy.copy(word)
        if word.text == 'her':
            cleaned_word.text = 'SBJ$'
            cleaned_word.lemma = '-SBJ$-'
        elif word.text == 'she':
            cleaned_word.text = 'SBJ'
            cleaned_word.lemma = '-SBJ-'
        cleaned_words.append(cleaned_word)
    return cleaned_words


def get_idioms(filename: str) -> List[Idiom]:
    with open(filename, 'r') as f:
        source_idioms = f.readlines()
    adapted_idioms = [_adapt_idiom(i) for i in source_idioms]
    downgraded_words = downgrader.downgrade('\n'.join(adapted_idioms))
    cleaned_words = _insert_placeholders(downgraded_words)
    grouped_words = itertools.groupby(cleaned_words, lambda x: x.text == '\n')
    downgraded_idioms = [list(g) for k, g in grouped_words if not k]
    return [Idiom(i) for i in downgraded_idioms]
