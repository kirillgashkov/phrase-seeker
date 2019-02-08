# Copyright (c) 2019 Kirill Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from typing import List, Dict
import downgrader
from idioms import Idiom


class Seeker:
    def __init__(self, idioms: List[Idiom]):
        self.idioms = idioms
        self.word_idioms = dict()

    def _idioms_for_word(self, word):
        if word not in self.word_idioms:
            word_idioms = list()
            for idiom in self.idioms:
                if word.lemma in idiom.lemmas:
                    word_idioms.append(idiom)
                if word.dep in idiom.placeholder_deps:
                    word_idioms.append(idiom)
            self.word_idioms[word] = word_idioms
        return self.word_idioms[word]

    @staticmethod
    def _check_suspect(suspect_words, matches, idiom):
        if len(suspect_words[0]) == len(idiom.words):
            t_idiom = idiom.text
            matched = True
            for got, expected in zip(suspect_words[0], idiom.words):
                equal_lemmas = got.lemma == expected.lemma
                expected_placeholder = expected.lemma in {'-SBJ-', '-SBJ$-'}
                equal_deps = got.dep == expected.dep
                if not (equal_lemmas or expected_placeholder and equal_deps):
                    matched = False
                    break
            if matched:
                if t_idiom not in matches:
                    matches[t_idiom] = 0
                matches[t_idiom] += 1
            del suspect_words

    def _handle_suspects(self, suspects, matches, idioms, word):
        for idiom in idioms:
            t_idiom = idiom.text
            if t_idiom not in suspects:
                suspects[t_idiom] = [list(), 0]
            suspect_words = suspects[t_idiom]
            suspect_words[0].append(word)
            self._check_suspect(suspect_words, matches, idiom)

    @staticmethod
    def _increment_suspects(suspects):
        for suspect in suspects.values():
            suspect[1] += 1
            if suspect[1] == 10:
                del suspect

    def seek(self, text: List[downgrader.Word]) -> Dict[str, int]:
        matches, suspects = dict(), dict()
        for word in text:
            word_idioms = self._idioms_for_word(word)
            self._handle_suspects(suspects, matches, word_idioms, word)
            self._increment_suspects(suspects)
        return matches
