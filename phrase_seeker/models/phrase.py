# Copyright (c) 2019 Kirill Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import dataclasses
from typing import List

from phrase_seeker import models


@dataclasses.dataclass
class Phrase:
    text: str
    words: List[models.Word]
    lemmas: List[str] = dataclasses.field(init=False)
    deps_of_indefinites: List[str] = dataclasses.field(init=False)

    def __post_init__(self):
        self.lemmas = [
            w.lemma for w in self.words if w.lemma != '-INDEF-'
        ]
        self.deps_of_indefinites = [
            w.dep for w in self.words if w.lemma == '-INDEF-'
        ]
