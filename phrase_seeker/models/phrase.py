# Copyright (c) 2019 Kirill Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import dataclasses
from typing import Tuple

from phrase_seeker import models


@dataclasses.dataclass(frozen=True)
class Phrase:
    text: str
    words: Tuple[models.Word, ...]
    lemmas: Tuple[str, ...] = dataclasses.field(init=False)
    indefinte_deps: Tuple[str, ...] = dataclasses.field(init=False)

    def __post_init__(self):
        lemmas = tuple(w.lemma for w in self.words if w.lemma != '-INDEF-')
        indef_deps = tuple([w.dep for w in self.words if w.lemma == '-INDEF-'])
        object.__setattr__(self, 'lemmas', lemmas)
        object.__setattr__(self, 'indefinte_deps', indef_deps)

    def __contains__(self, item):
        if type(item) is not models.Word:
            return False
        lemma_check = item.lemma in self.lemmas
        indefinte_check = item.dep in self.indefinte_deps
        return lemma_check or indefinte_check
