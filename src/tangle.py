"""
    Build script for pwave files.
    See pweave for further details. 
        http://mpastell.com/pweave/
        https://github.com/mpastell/Pweave
"""

import pweave
import os
import sys


def main():
    """
        Extract python source code from pweave files.
        Only works if .pmd files are found in the same directory as this script.
    """

    # Get the pweave files from the source directoy : 
    files = [f for f in os.listdir(".") if f[-4:] == ".pmd"]
   
    for f in files:
        pweave.tangle(f)
##

if __name__ == "__main__":
    main()

