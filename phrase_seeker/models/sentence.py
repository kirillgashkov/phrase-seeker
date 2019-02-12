# Copyright (c) 2019 Kirill Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import dataclasses
from typing import Tuple

from phrase_seeker import models


@dataclasses.dataclass(frozen=True)
class Sentence:
    text: str
    words: Tuple[models.Word, ...]
    start: int
    end: int
