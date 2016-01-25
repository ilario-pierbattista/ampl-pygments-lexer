from pygments.lexer import RegexLexer,include
from pygments.token import *


class AmplLexer(RegexLexer):
    name = 'Ampl'
    aliases = ['ampl', 'AMPL', 'Ampl']
    filenames = ['*.mod', '*.dat', '*.run']

    KEYWORDS = [
        'set',
        'param',
        'var',
        'minimize'
    ]

    MODEL_DECLARATIONS = [
        "set",
        "param",
        "var",
        "arc",
        "minimize",
        "maximize",
        "subject to",
        "node"
    ]

    char = r'[a-zA-Z$._0-9@]'
    identifier = r'(?:[a-zA-Z$_]' + char + '*|\.' + char + '+)'
    number = r'[+-]?(?:0[xX][a-zA-Z0-9]+|\d+)'
    binary_number = r'0b[01_]+'
    model_declaration = r'(?i)(' + '|'.join(MODEL_DECLARATIONS) + ')'
    single_char = r"'\\?" + char + "'"
    string = r'"(\\"|[^"])*"'

    tokens = {
        'root': [
            include('whitespace'),
            (r'#.*\n', Comment),
            #(model_declaration, Name.Function, 'declaration-args'),
        ],

        'declaration-args': [
            #(identifier, Name.Variable),
            (r'.*', Name.Variable)
        ],

        'whitespace': [
            (r'\n', Text),
            (r'\s+', Text),
            (r';', Text)
        ]
    }
