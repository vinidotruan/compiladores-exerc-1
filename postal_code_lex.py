import ply.lex as lex

tokens = (
   	'POSTALCODE',
   	'PHONENUMBER',
)

def t_POSTALCODE(t):
	r'\(\d{2}\)'
	t.type = 'POSTALCODE'
	return t

def t_PHONENUMBER(t):
	r'\d{9}'
	t.type = 'PHONENUMBER'
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()


