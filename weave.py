"""
    Build script for pwave files.
    See pweave for further details. 
        http://mpastell.com/pweave/
        https://github.com/mpastell/Pweave
"""

from pweave import publish, weave
from pathlib import Path


def main():
    """
    Build html from specified files, using pweave.
    """

    src_dir = Path("src")
    build_dir = Path("build")
    # Get the pweave files from the source directory as strings
    files = [f.name for f in src_dir.joinpath("markdown").glob("*.pmd")]

    for f in files:
        # Turn python markdown into HTML
        publish(
            src_dir.joinpath("markdown").joinpath(f),
            output=build_dir.joinpath(f.replace("pmd", "html")),
        )
        # Create a script
        weave(
            src_dir.joinpath("markdown").joinpath(f),
            output=src_dir.joinpath("scripts").joinpath(f.replace("pmd", "py")),
        )


##

if __name__ == "__main__":
    main()
