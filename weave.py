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
        Build html from specified files, using pweave.
    """

    # Get the pweave files from the source directoy : 
    files = [f for f in os.listdir("src/") if f[-4:] == ".pmd"]
   
    for f in files:
        pweave.publish(
            os.path.join("src", f), 
            output = os.path.join("build", f.replace("pmd", "html"))
        )
##

if __name__ == "__main__":
    main()

