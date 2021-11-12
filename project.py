#!/usr/bin/env python3
"""
Author : caro <caro@localhost>
Date   : 2021-11-10
Purpose: Final Project BE 434 Fall 2021
"""

import argparse
import os
from translate import Translator


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
    
    parser.add_argument('-s',
                        '--string',
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
                        default='outdir')

    return parser.parse_args()


# --------------------------------------------------
def main():
    '''Main Function that calls upon other functions to translate'''

    args = get_args()
    str_arg = args.arg
    
    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)
        
    interpreter = Translator(from_lang="{args.language1}", to_lang="{args.language2}")
    

# --------------------------------------------------
def string_translate(string, languages):
  original = open(os.path.join(args.outdir, root + '_' + "{args.language1}" + ext), 'wt')
  translated = open(os.path.join(args.outdir, root + '_' + "{args.language2}" + ext), 'wt')
  print(string, file=original)
  print(languages.translate(string), file=translated)
  
# --------------------------------------------------
def file_translate(file, languages):
  for fh in args.file:
        root, ext = os.path.splitext(os.path.basename(fh.name))
        original = open(os.path.join(args.outdir, root + '_' + "{args.language1}" + ext), 'wt')
        translated = open(os.path.join(args.outdir, root + '_' + "{args.language2}" + ext), 'wt')
  
# --------------------------------------------------
if __name__ == '__main__':
    main()
