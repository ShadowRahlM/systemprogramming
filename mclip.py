#! /usr/bin/env python3.13
import pyperclip as pclip
import sys

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

if len(sys.argv) != 2:
    print('Usage: mclip.py [keyphrase] - copy text')
    sys.exit(1)

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pclip.copy(TEXT[keyphrase])
    print(f'Text for "{keyphrase}" copied to clipboard.')
else:
    print(f'There is no text for "{keyphrase}".')
    message = input('Enter message for keyphrase:\n')
    TEXT[keyphrase] = message
    pclip.copy(TEXT[keyphrase])
    print(f'Text for "{keyphrase}" added and copied to clipboard.')