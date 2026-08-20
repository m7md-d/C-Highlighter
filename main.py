"""
read a C file and highlight keywords in the code and generate HTML.
"""
import re
from sys import argv

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

styles = {
    "type": "color: blue; font-weight: bold;",
    "control": "color: green; font-weight: bold;"
}

def generate_html(code):
    
    # escape HTML special characters to prevent breaking the HTML structure
    code = code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    # Highlight keywords
    for keyword, token_type in symbols.items():
        pattern = r'\b' + re.escape(keyword) + r'\b'
        # Use a lambda function to replace the matched keyword with a span element that applies the appropriate style
        replacement = lambda m: f'<span style="{styles[token_type]}">{m.group(0)}</span>'
        code = re.sub(pattern, replacement, code)

    return f'<body style="background-color: black; color: white;"><pre>{code}</pre></body>'

code = argv[1] if len(argv) > 1 else "test.c"

with open(code, "r") as f:
    code_content = f.read()

html_content = generate_html(code_content)
output_file = code.rsplit(".", 1)[0] + ".html"

with open(output_file, "w") as f:
    f.write(html_content)