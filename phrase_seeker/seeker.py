# Copyright (c) 2019 Kirill Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from typing import Set, List, Dict, Optional

import spacy

from phrase_seeker import models, phraser, sentencer


def seek_phrases_in_text(
        phrases_as_strings: List[str],
        text: str,
        ) -> List[models.Match]:
    nlp = spacy.load('en_core_web_sm', disable=['ner', 'textcat'])

    phrases = phraser.phrases_from_strings(phrases_as_strings, nlp)
    sentences = sentencer.sentences_from_text(text, nlp)

    matches = list()
    for sentence in sentences:
        sentence_matches = _phrases_in_sentence(phrases, sentence)
        matches += sentence_matches

    return matches


#
# Phrases
#


def _phrases_in_sentence(
        phrases: Set[models.Phrase],
        sentence: models.Sentence,
        ) -> List[models.Match]:
    suspects = dict()

    for word in sentence.words:
        phrases_ = _phrases_for_word(word, phrases)
        word_suspects = {phrase: [word] for phrase in phrases_}
        _merge_suspects(suspects, word_suspects)

    return _matches_from_suspects(suspects, sentence)


_word_phrases = dict()


def _phrases_for_word(
        word: models.Word,
        all_phrases: Set[models.Phrase],
        ) -> Set[models.Phrase]:
    if word in _word_phrases:
        return _word_phrases[word]
    phrases = set(phrase for phrase in all_phrases if word in phrase)
    _word_phrases[word] = phrases
    return phrases


#
# Suspects
#


def _merge_suspects(
        suspects: Dict[models.Phrase, List[models.Word]],
        with_suspects: Dict[models.Phrase, List[models.Word]],
        ):
    for phrase, words in with_suspects.items():
        if phrase not in suspects:
            suspects[phrase] = list()
        suspects[phrase].extend(words)


#
# Matches
#


def _matches_from_suspects(
        suspects: Dict[models.Phrase, List[models.Word]],
        sentence: models.Sentence,
        ) -> List[models.Match]:
    matches = list()

    for phrase, words in suspects.items():
        if _is_a_match(phrase, words):
            match = models.Match(phrase, sentence)
            matches.append(match)

    return matches


def _is_a_match(phrase: models.Phrase, words: List[models.Word]) -> bool:
    words_copy = words.copy()
    for phrase_word in phrase.words:
        index = _index_of_phrase_word_in_list(phrase_word, words_copy)
        if index is None:
            return False
        del words_copy[index]
    return True


def _index_of_phrase_word_in_list(
        phrase_word: models.Word,
        words: List[models.Word],
        ) -> Optional[int]:
    if phrase_word.lemma == '-INDEF-':
        for i, word in enumerate(words):
            if word.dep == phrase_word.dep:
                return i
    else:
        for i, word in enumerate(words):
            if word.lemma == phrase_word.lemma:
                return i
    return None
