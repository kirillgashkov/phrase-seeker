# Copyright (c) 2019 Kirill Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import dataclasses
from typing import List

from phrase_seeker import models


@dataclasses.dataclass
class Sentence:
    text: str
    words: List[models.Word]
    start: int
    end: int
