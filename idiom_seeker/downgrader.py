# Copyright (c) 2019 Kirill Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import dataclasses
from typing import List

import spacy


@dataclasses.dataclass
class Word:
    """
    A container for original and downgraded versions of word as well as its
    lemma and part of speech.
    """
    text: str
    lemma: str
    pos: str
    dep: str


def downgrade(s: str) -> List[Word]:
    """
    Downgrades text into a list of lemmatized words.
    """
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(s)
    return [Word(tkn.text, tkn.lemma_, tkn.pos_, tkn.dep_) for tkn in doc]
