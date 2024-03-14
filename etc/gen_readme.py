#!/usr/bin/env python
# *----------------------------------------------------------------------*
# * NAME: gen_readme.py
# *
# * DESC: Use pdm readmecov to produce coverage summary and replace
# * token in docs/README.md.in for generating a new README.md
# *----------------------------------------------------------------------*

import os
import subprocess

# * Constants
SRC = 'docs/README.md.in'
TRG = 'README.md'

TOKEN = '~~COVERAGE~~'

CMD = ['pdm', 'readmecov']


def main() -> None:
    text = ''
    with open(SRC, 'r') as f_in:
        text = f_in.read()

    summary = subprocess.check_output(CMD, encoding='utf-8')

    content = text.replace(TOKEN, summary)

    with open(TRG, 'w', encoding='utf-8') as f_out:
        f_out.write(content)


if __name__ == '__main__':
    main()
