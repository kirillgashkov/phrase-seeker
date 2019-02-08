# Copyright (c) 2019 Kirill Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from typing import List

import spacy

from phrase_seeker import models


class Downgrader:

    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def downgrade(self, s: str) -> List[models.Word]:
        doc = self.nlp(s)
        return [models.Word(tkn.text, tkn.lemma_) for tkn in doc]
