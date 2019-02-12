# Copyright (c) 2019 Kirill Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

from timeit import default_timer as timer

from phrase_seeker import seek_phrases_in_text


def with_time(function):
    def wrapper():
        start = timer()
        function()
        end = timer()
        print(
            f'--- elapsed time ---\n'
            f'{end - start:.3f}s'
        )
    return wrapper


@with_time
def main():
    text = 'Insert your awesome text here'

    phrases = ['inserted text']

    matches = seek_phrases_in_text(phrases, text)

    for match in matches:
        print(match.phrase.text)
        print(f'    [{match.sentence.start}:{match.sentence.end}] {match.sentence.text}')


if __name__ == '__main__':
    main()
