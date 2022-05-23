import ply.lex as lex

tokens = (
   	'IDENTIFICATOR',
)

def t_IDIENTIFICATOR(t):
	r'\d{11}'
	t.type = 'IDENTIFICATOR'
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()


