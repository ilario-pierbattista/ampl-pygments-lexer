from pygments.lexer import RegexLexer,include
from pygments.token import *


class AmplLexer(RegexLexer):
    name = 'Ampl'
    aliases = ['ampl', 'AMPL', 'Ampl']
    filenames = ['*.mod', '*.dat', '*.run']

    KEYWORDS = [
        "set",
        "param",
        "var",
        "arc",
        "minimize",
        "maximize",
        "subject to",
        "node",
        "check",
        "in",
        "within",
        "logical",
        "integer",
        "solve",
        "option",
        "sum",
        "model",
        "data"
    ]

    char = r'[a-zA-Z$._0-9@]'
    identifier = r'(?:[a-zA-Z$_]' + char + '*|\.' + char + '+)'
    number = r'[+-]?(?:0[xX][a-zA-Z0-9]+|\d+)'
    #binary_number = r'0b[01_]+'
    #model_declaration = r'(?i)(' + '|'.join(MODEL_DECLARATIONS) + ')'
    #single_char = r"'\\?" + char + "'"
    #string = r'"(\\"|[^"])*"'

    keyword = r'(' + '|'.join(KEYWORDS) + ')[^a-z]'

    tokens = {
        'root': [
            (keyword, Keyword),
            (identifier, Name.Label),
            include('whitespace'),
            include('comments'),
            include('punctuation'),
            include('operators'),
            include('litterals'),
            include('aliases')
        ],

        'whitespace': [
            (r'\n', Text),
            (r'\s+', Text)
        ],

        'comments': [
            (r'#.*\n', Comment),
        ],

        'punctuation': [
            (r'[:{};,]', Punctuation)
        ],

        'operators': [
            (r'[\+\-<>=\[\]\*/\^]', Operator)
        ],

        'litterals': [
            (number, Number)
        ],

        'aliases': [
            (r"'.*'", String)
        ]
    }
