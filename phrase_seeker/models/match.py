# Copyright (c) 2019 Kirill Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import dataclasses

from phrase_seeker import models


@dataclasses.dataclass(frozen=True)
class Match:
    phrase: models.Phrase
    sentence: models.Sentence
