import ply.lex as lex

tokens = (
   	'CARPLATE',
)

def t_CARPLATE(t):
	r'(\d{3})[A-Z]{4}'
	t.type = 'CARPLATE'
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()


