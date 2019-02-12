# Copyright (c) 2019 Kirill Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import dataclasses
from typing import List

from phrase_seeker import models


@dataclasses.dataclass(frozen=True)
class Phrase:
    text: str
    words: List[models.Word]
    lemmas: List[str] = dataclasses.field(init=False)
    indefinte_deps: List[str] = dataclasses.field(init=False)

    def __post_init__(self):
        lemmas = [w.lemma for w in self.words if w.lemma != '-INDEF-']
        indefinte_deps = [w.dep for w in self.words if w.lemma == '-INDEF-']
        object.__setattr__(self, 'lemmas', lemmas)
        object.__setattr__(self, 'indefinte_deps', indefinte_deps)
