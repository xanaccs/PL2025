import ply.lex as lex

frase_exemplo = '''
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000
'''

tokens = (
    'COMMENT', 'SELECT', 'WHERE', 'LIMIT',
    'VAR', 'PREFIXO', 'PREDICADO', 
    'STRING', 'NUMERO', 'PALAVRA',
    'PONTO', 'ACHAVE', 'FCHAVE'
)

t_ACHAVE = r'\{'
t_FCHAVE = r'\}'
t_PONTO = r'\.'

def t_COMMENT(t):
    r'\#.*'
    return t

def t_SELECT(t):
    #r'(?i)SELECT'
    r'SELECT'
    t.value = t.value.upper()
    return t

def t_WHERE(t):
    #r'(i?)WHERE'
    r'WHERE'
    t.value = t.value.upper()
    return t

def t_LIMIT(t):
    #r'(?i)LIMIT'
    r'LIMIT'
    t.value = t.value.upper()
    return t

def t_VAR(t):
    r'\?[a-zA-Z_]\w+'
    return t

def t_STRING(t):
    r'\"[^\"]*\"'
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int (t.value)
    return t

def t_PREFIXO(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*\.'
    return t

def t_PREDICADO(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

t_ignore = " \t"  # Ignorar espaços e tabulações

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
    
def t_error(t):
    print("Simbolo inválido na linha {t.lineno}: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
lexer.input(frase_exemplo)

# le todos os tokens 
while r := lexer.token():
    print(r)