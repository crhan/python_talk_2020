#%%
from lib import CalcLexer
from sly import Parser
"""
expr       : expr + term
           | expr - term
           | term

term       : term * factor
           | term / factor
           | factor

factor     : NUMBER
           | ( expr )
"""

class CalcParser(Parser):
    # Get the token list from the lexer (required)
    tokens = CalcLexer.tokens

    # Grammar rules and actions
    @_('expr PLUS term')
    def expr(self, p):
        return p.expr + p.term

    @_('expr MINUS term')
    def expr(self, p):
        return p.expr - p.term

    @_('term')
    def expr(self, p):
        return p.term

    @_('term TIMES factor')
    def term(self, p):
        return p.term * p.factor

    @_('term DIVIDE factor')
    def term(self, p):
        return p.term / p.factor

    @_('factor')
    def term(self, p):
        return p.factor

    @_('NUMBER')
    def factor(self, p):
        return p.NUMBER

    @_('LPAREN expr RPAREN')
    def factor(self, p):
        return p.expr

# %%
lexer = CalcLexer()
parser = CalcParser()

data = '1 + 2 * (5 - 1)'
tokens = lexer.tokenize(data)
result = parser.parse(tokens)
print(result)


# %%
