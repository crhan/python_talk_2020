#%%
class IRedisLexer(Lexer):
    tokens = {ID, QUOTE, ESCAPE, SPACE}

    QUOTE = r"['\"]"
    ESCAPE = r"\\"
    SPACE = r"\s"
    ID = r"[^'\"\\\s]+"
