#!python3

# AEMT.py - [A]tari [E]ight-bit [M]ulti-[T]ool
#
# Copyright(C) 2026, Ian Michael Dunmore
#
# License: https://github.com/idunmore/aemt/blob/master/LICENSE

# 3rd Party/External Modules
import sys
import click

# Local Application Modules
from .atr import atr

# Constants

# Error Messages and Command Result Exit Codes
ERROR_TEXT ='Error: '
ERROR = 1
SUCCESS = 0

# Verbosity Values
SILENT = 0
PROGRESS = 1
VERBOSE = 2

# Command Line Interface

@click.group()
@click.version_option('0.1.0.0')
def aemt():
    '''[A]tari [E]ight-bit [M]ulti-[T]ool

            \b
                Manipulates Atari 8-bit .ATR disk images.                        
            
            \b
                Moves files to organized folder structures, with an optionally
                limited number of files per folder.
            
            \b           
                Creates, applies and updates .cfg files for Atari THE400 Mini
                games on USB media.
            
            \b
                Identifies and verifies Atari 8-bit cartridge images.'''
    pass
    
# Run!
if __name__ == 'aemt.cli':
    aemt.add_command(atr)
    aemt()

if __name__ == '__main__':
    sys.exit(aemt())
