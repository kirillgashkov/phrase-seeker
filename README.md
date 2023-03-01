# Phrase Seeker

Search texts for phrases regardless of their forms and words in-between.

## Features

- Search texts for phrases.
- Search for multiple pharses at once.
- Find phrases even if they weren't in their normalized forms.
- Find phrases even if there had extra words in-between (e.g. adjectives).
- Get sentence where the phrase was found.
- Get location of the sentence in the text.

## Requirements

- Python 3.7

## Installation

```sh
$ git clone git@github.com:kirillgashkov/phrase-seeker.git
$ cd phrase-seeker
$ pip install -r requirements.txt
```

## Usage

> **Note:** by default seeking function won't leave cache after itself. You can
  change this behavior by passing `should_delete_cache=False` as an additional
  argument to the function. However, if the phrases are changed, you must delete
  the cache before using the function again (call `phrase_seeker.delete_cache()`
  to do so).

```python
from phrase_seeker import seek_phrases_in_text

text = "Insert your awesome text here"
phrases = ["inserted text"]

matches = seek_phrases_in_text(phrases, text)

for match in matches:
    print(match.phrase.text)
    print(match.sentence.start, match.sentence.end, '-', match.sentence.text)
```

## License

Distributed under the MIT License. See the [LICENSE.md](LICENSE.md) for details.

## Acknowledgments

- [Spacy](https://github.com/explosion/spaCy)
