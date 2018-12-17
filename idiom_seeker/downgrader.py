"""
Downgrades strings to lists of words
"""

from typing import List
import spacy


class Word:
    def __init__(self, text: str, lemma: str, pos: str, dep: str):
        self.text = text
        self.lemma = lemma
        self.pos = pos
        self.dep = dep


    def __repr__(self):
        return f'<{self.text} {self.lemma} {self.pos} {self.dep}>'


def downgrade(s: str) -> List[Word]:
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(s)
    return [Word(tkn.text, tkn.lemma_, tkn.pos_, tkn.dep_) for tkn in doc]
