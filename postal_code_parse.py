import ply.yacc as yacc

from phone_number_lex import tokens

def p_term(p):
	'''
	terminal : phone_number
	'''
	p[0] = p[1]

def p_phone_number(p):
	'phone_number : POSTALCODE PHONENUMBER'
	p[0] = p[1]+p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
	try:
		s = input('digite: ')
	except EOFError:
		break
	if not s: continue
	result = parser.parse(s)
	print(result)