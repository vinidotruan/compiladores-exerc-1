import ply.yacc as yacc

from real_number_lex import tokens

def p_term(p):
	'''
	terminal : natural_number
	'''
	p[0] = p[1]


def p_natural_number(p):
	'natural_number : NATURALNUMBERS'
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