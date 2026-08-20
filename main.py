"""
read a C file and highlight keywords in the code and generate HTML.
"""
import re

# --- constants ----------------------------------------------------------------
symbols = {
    "int": "type",
    "float": "type",
    "double": "type",
    "char": "type",
    "void": "type",
    "long": "type",
    "short": "type",
    "signed": "type",
    "unsigned": "type",
    "if": "control",
    "else": "control",
    "while": "control",
    "for": "control",
    "do": "control",
    "switch": "control"
}

