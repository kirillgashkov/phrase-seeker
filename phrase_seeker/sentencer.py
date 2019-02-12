# Copyright (c) 2019 Kirill Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from typing import List

from phrase_seeker import models


def sentences_from_text(text: str, nlp: callable) -> List[models.Sentence]:
    sentences = list()

    for sent in nlp(text).sents:
        text = sent.text
        words = tuple(models.Word(w.text, w.lemma_, w.dep_) for w in sent)
        sentence = models.Sentence(text, words, sent.start, sent.end)
        sentences.append(sentence)

    return sentences
