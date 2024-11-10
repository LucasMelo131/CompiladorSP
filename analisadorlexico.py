'''

Autor: Lucas Melo de Carvalho

'''

#comentários são definidos por --
#comentários multilinha são definidos por /* */

import ply.lex as lex

class Lexico:

    def __init__(self):
        #constroi o lexer
        self.lexer = lex.lex(module=self)
        #lista de tokens
        self.tokens_lista = []
        #lista de erros lexicos
        self.erros = []


    #palavras reservadas
    reservado = {
        'begin' : 'BEGIN',
        'end' : 'END',
        'const' : 'CONST',
        'type' : 'TYPE',
        'var' : 'VAR',
        'integer' : 'INTEGER',
        'real' : 'REAL',
        'char' : 'CHAR',
        'boolean' : 'BOOLEAN',
        'array' : 'ARRAY',
        'of' : 'OF',
        'record' : 'RECORD',
        'function' : 'FUNCTION',
        'procedure' : 'PROCEDURE',
        'while' : 'WHILE',
        'do' : 'DO',
        'if' : 'IF',
        'then' : 'THEN',
        'for' : 'FOR',
        'write' : 'WRITE',
        'read' : 'READ',
        'to' : 'TO',
        'else' : 'ELSE',
        'false' : 'FALSE',
        'true' : 'TRUE',
        'and' : 'AND',
        'or' : 'OR'
    }

    tokens = [
        'CONST_VALOR',
        'ID',
        'NUMERO',
        'IGUAL',
        'PONTOEVIRGULA',
        'VIRGULA',
        'DOISPONTOS',
        'PARENTESISESQ',
        'PARENTESISDIR',
        'ATRIBUICAO',
        #'OP_LOGICO',
        'OP_COMP',
        'OP_MAT',
        'PONTO',
        'COMENTARIO',
        'COLCHETEESQ',
        'COLCHETEDIR',
        'COMENTARIOMULTILINHAS'
    ] + list(reservado.values())

    #expressões regulares para cada token

    t_CONST_VALOR = r'\"[a-zA-Z0-9 ]*\"'
    t_NUMERO = r'[-+]?[0-9]+(\.[0-9]*)?'
    t_IGUAL = r'\='
    t_PONTOEVIRGULA = r'\;'
    t_VIRGULA = r'\,'
    t_DOISPONTOS = r'\:'
    t_PARENTESISESQ = r'\('
    t_PARENTESISDIR = r'\)'
    t_ATRIBUICAO = r'\:\='
    t_PONTO = r'\.'
    t_OP_COMP = r'\>|\<|\=\=|\!\=|\>\=|\<\='
    t_OP_MAT = r'\+|\-|\*|\/'
    t_COLCHETEESQ = r'\['
    t_COLCHETEDIR = r'\]'

    t_ignore = ' \t' #ply ignora whitespace por padrao

    def t_ID(self,t):
        r'[a-zA-Z][a-zA-Z0-9]*'
        t.type = self.reservado.get(t.value,'ID')
        return t

    def t_COMENTARIO(self,t):
        r'\-\-.*'
        pass

    #definir comentario multilinha
    def t_COMENTARIOMULTILINHAS(self,t):
        r'/\*([\s\S]*?)\*/'
        t.lexer.lineno += t.value.count('\n')
        pass
    

    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    #Aponta mensagem de erro e pula para o próximo caracter
    def t_error(self,t):
        self.erros.append((t.value,t.lineno))
        t.lexer.skip(1)
        print(f"Caracter inválido {t.value[0]} na linha {t.lineno} ")

    def addt(self,t):
        #token = (tipo,valor,linha,coluna)
        self.tokens_lista.append((t.type,t.value,t.lineno))
    
    def tokenizacao(self,arquivo):
        self.lexer.input(arquivo)
        while True:
            t = self.lexer.token()
            if not t:
                break

            self.addt(t)

    def imprimir_tokens(self):
        print("\nOs tokens estão no seguinte formato: (nomedotoken,valor,linha):")
        for token in self.tokens_lista:
            print(token)
