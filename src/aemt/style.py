# style.py - Style Classes, Constants and Functions for AEMT
#
# Copyright(C) 2026, Ian Michael Dunmore
#
# License: https://github.com/idunmore/aemt/blob/master/LICENSE

# 3rd Party/External Modules
from sty import fg

class C:
    """
    Text color/effect aliases (from "sty" module values).
    Use with f-strings: "{C.Err}Error text.{C.Off}
    """
    # C class = "Color"; Abbreviations are to reduce line lengths.
    Err = fg.red        # For Errors
    Prot = fg.green     # For Write-Protect 
    Unprot = fg.red     # For Writeable (Unprotected)
    Off = fg.rs         # Default Color (Color="OFF")
