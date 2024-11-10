from analisadorlexico import Lexico

file = open("exemplo2.sp","r")
programa = file.read()

lexico = Lexico()
lexico.tokenizacao(programa)
lexico.imprimir_tokens()