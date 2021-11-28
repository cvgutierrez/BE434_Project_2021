#!/usr/bin/env python3
"""
Author : caro <caro@localhost>
Date   : 2021-11-10
Purpose: Final Project BE 434 Fall 2021
"""

import argparse
import os
from translate import Translator
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate a file or string into a different language with new files as an output in an output directory',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-l1',
                        '--language1',
                        help="Input file's language",
                        metavar='str',
                        type=str,
                        default='Korean')

    parser.add_argument('-l2',
                        '--language2',
                        help="Language the file or string is being translated to",
                        metavar='str',
                        type=str,
                        default='English')
    
    parser.add_argument('file',
                        help='Input file to translate',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None,
                        nargs='*')
    
    parser.add_argument('string',
                        help="Input string to translate",
                        metavar='str',
                        type=str,
                        default=None,
                        nargs='*')
      
    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        type=str,
                        metavar='DIR',
                        default='sys.stdout')

    return parser.parse_args()


# --------------------------------------------------
def main():
    '''Main Function that calls upon other functions to translate'''

    args = get_args()
    str_arg = args.arg
    
    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    if args.string:
        translated = string_translate(args.string, agrs.language1, args.language2)
        print(translated, file = args.outdir)

    if args.file:
        translated = file_translate(args.file, agrs.language1, args.language2)
        print(translated, file = args.outdir)

    if not args.file and not args.string:
        print("There's nothing to translate. Please input a string or file to translate.")

    

# --------------------------------------------------
def string_translate(string, in_lang, out_lang):
    '''translate strings'''

    interpreter = Translator(from_lang=in_lang, to_lang=out_lang)
    return translator.translate(string)

  
# --------------------------------------------------
def file_translate(file, in_lang, out_lang):
    '''translate files'''

    interpreter = Translator(from_lang=in_lang, to_lang=out_lang)
    lines = []
    for line in file:
        new_line = translator.translate(line.rstrip())
        lines.append(new_line)
    return "\n".join(lines)

  
# --------------------------------------------------
if __name__ == '__main__':
    main()
