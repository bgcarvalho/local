#!/usr/bin/env python

import click

@click.command()
@click.argument('pattern')
@click.option('--cutprefix', default=None, help='Cut substring at the beginning of name')
@click.option('--cutsuffix', default=None, help='Cut substring at the end (ignoring file extension)')
@click.option('--addsubstring', default=None, help='Add substring at --addsubstringat')
@click.option('--addsubstringat', default=None, help='Position for adding a substring')
@click.option('--addprefix', default=None)
@click.option('--addsuffix', default=None)
@click.option('--replace', default=None)
@click.option('--addcounter', default=None)
@click.option('--replaceext', default=None)
def renamer():
    """
    Renamer
    
    Variables
    ---------
    - $N - counter
    - $ATIME - Creation time
    - $MTIME - Modified time
    - $CTIME - Changed time
    - $EXT - Extension
    """
    pass

if __name__ == "__main__":
    renamer()
