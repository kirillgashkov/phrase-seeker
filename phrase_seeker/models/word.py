# Copyright (c) 2019 Kirill Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import dataclasses


@dataclasses.dataclass
class Word:
    text: str
    lemma: str
