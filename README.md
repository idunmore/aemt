# [A]tari [E]ight-bit [M]ulti-[T]ool - aemt

![GitHub License](https://img.shields.io/github/license/idunmore/aemt)&nbsp;![PyPI - Version](https://img.shields.io/pypi/v/aemt)&nbsp;![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aemt)

This is a command-line tool, intended to provide some "quality of life" improvements to managing large game/program libraries, on USB Media, for the "Atari THE400 Mini" (with utilities for other Atari 8-bit emulators).

Current functionality includes:

* Manipulates Atari 8-bit .ATR disk images.

* Moving files, in bulk, to organized folder structures - with the ability
  to control how the organization is done and to limit the number of files
  per folder (to avoid exceeding "THE400 Minis" 255 files-per-folder limit).

* Creating, applying, and updating .cfg files automatically, WITHOUT having
  to set them individually, one game at a time, from within "THE400 Mini's"
  file browser.

* Identify and validate CARTRIDGE files (".car" and ".c01" to ".c70"),
  including decoding the header, showing the stored ROM data checksum and
  computing the actual checksum of the contained ROM data.

  Only the ".cfg" file functionality is specific to "THE400 Mini"; the other
  functions can be used with any Atari 8-bit emulators/systems.


## Usage: ##

    Usage: aemt [OPTIONS] COMMAND [ARGS]...
    
      [A]tari [E]ight-bit [M]ulti-[T]ool
    
        Manipulates Atari 8-bit .ATR disk images.

	    Moves files to organized folder structures, with an optionally
	    limited number of files per folder.

        Creates, applies and updates .cfg files for Atari THE400 Mini
        games on USB media.

	    Identifies and verifies Atari 8-bit cartridge images.
    
    Options:
      --version  Show the version and exit.
      --help     Show this message and exit.
    
    Commands:
      atr     Manipulates Atari 8-bit .ATR disk images.
      cart    Identifies and validates Atari 8-bit cartridges.
      config  Creates and updates .CFG files for THE400 Mini USB Media games.
      split   Moves files to organized folder structures.


## Installing

For all installation options, the first step is to install [Python 3.14.3](https://python.org) or later (may work with earlier versions, provided they have built-in type-hint support, but not tested).

### Install via PIP

Run:

    pip install aemt

Run:

    aemt --version

You should see something like:

    aemt, version 1.0.0
    
### Install via PIPX

You can install AEMT in an isolated environment (recommended) using [pipx](https://pipx.pypa.io/stable/).

See the [installation instructions](https://pipx.pypa.io/stable/) for pipx, and then:

Run:

    pipx install aemt

Run:

    aemt --version

You should see something like:

    aemt, version 1.0.0
