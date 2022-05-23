import ply.lex as lex

tokens = (
   	'WORD',
   	'HTMLTAG',
)

def t_WORD(t):
	r'\w'
	t.type = 'WORD'
	return t

def t_HTMLTAG(t):
	r'''\<(?:"[^"]*"['"]*|'[^']*'['"]*|[^'">])+>'''
	t.type = 'HTMLTAG'
	return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()


