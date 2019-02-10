# Copyright (c) 2019 Kirill Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from phrase_seeker import models, processors


class Phraser:

    def __init__(self, downgrader: processors.Downgrader):
        self.downgrader = downgrader

    def phrase(self, s: str) -> models.Phrase:
        words = self.downgrader.words(s)
        lemmas = [w.lemma for w in words]
        return models.Phrase(s, words, lemmas)
