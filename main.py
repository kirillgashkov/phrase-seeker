# Copyright (c) 2019 Kirill Gashkov
#
# Distributed under MIT License. See LICENSE file for details.

import json
import downgrader
import idioms
from seeker import Seeker


textfiles = [
    'text.txt',
    'b-harry-potter-1.txt',
    'b-murder-on-the-orient-express.txt',
    'b-the-lord-of-rings-1.txt',
    'm-the-green-mile.txt',
    'm-the-mask.txt',
    'm-the-wizard-of-oz.txt',
]


def seek_for_idioms(seeker, textfile):
    print(f'operating on {textfile}...')

    print('\tgetting text...')
    with open(f'texts/{textfile}', 'r') as f:
        text = f.read()
    text_ = downgrader.downgrade(text)

    print('\tseeking...')
    matches = seeker.seek(text_)

    print('\twriting response...')
    with open(f'responses/{textfile}', 'w+') as f:
        f.write(json.dumps(matches, indent=1))

    print('\tDone.')



def main():
    print('getting idioms...')
    idioms_ = idioms.get_idioms('idioms.txt')
    seeker = Seeker(idioms_)
    for textfile in textfiles:
        seek_for_idioms(seeker, textfile)


if __name__ == '__main__':
    main()
