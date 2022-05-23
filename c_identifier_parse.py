import ply.yacc as yacc

from c_identifier_lex import tokens

def p_term(p):
	'''
	terminal : cidentifier
	'''
	p[0] = p[1]


def p_cidentifier(p):
	'cidentifier : CIDENTIFIERS'
	p[0] = p[1]

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

while True:
	try:
		s = input('digite: ')
	except EOFError:
		break
	if not s: continue
	result = parser.parse(s)
	print(result)