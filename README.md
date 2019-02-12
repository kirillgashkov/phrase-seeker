# Phrase Seeker

Searches for phrases in texts regardless of their form and words between.

## Features

- Search for phrases in texts;
- Set multiple phrases to search for;
- Find phrases even if they aren't in normalized form;
- Find phrases even if there are words between (e.g. adjectives);
- Get the sentence where the phrase was found;
- Get the location of the sentence in the text

## Requirements

- Python 3.7.1

## Installation

1. Clone this repository.
2. Install required packages. See the ([requirements.txt](requirements.txt)).

## Usage

**Warning:** by default seeking function won't leave cache after itself. You can change this behavior by passing `should_delete_cache=False` as an additional argument to the function. However, if the phrases are changed, you must delete the cache before using the function again (call `phrase_seeker.delete_cache()` to do so).

```python
# import `seek_phrases_in_text` function
from phrase_seeker import seek_phrases_in_text

# get the text to search in and the phrases to search for
text = 'Insert your awesome text here'
phrases = ['inserted text']

# pass them as arguments to the imported function
matches = seek_phrases_in_text(phrases, text)

# operate on the matches
for match in matches:
	print(match.phrase.text)
    print(match.sentence.start, match.sentence.end, '-', match.sentence.text)
```

## License

Distributed under the MIT License. See the [LICENSE.md](LICENSE.md) for details.

## Acknowledgments

- [Spacy](https://github.com/explosion/spaCy)
