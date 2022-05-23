import ply.yacc as yacc

from html_tag_lex import tokens

def p_term(p):
	'''
	terminal : word 
			 | html_tag
	'''
	p[0] = p[1]


def p_word(p):
	'word : WORD'
	p[0] = p[1]

def p_html_tag(p):
	'''
	html_tag : HTMLTAG WORD HTMLTAG
			 | HTMLTAG WORD
			 | HTMLTAG
	'''
	if(len(p) == 4):
		p[0] = p[1] + p[2] + p[3]
	elif(len(p) == 3):
		p[0] = p[1] + p[2]
	else:
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