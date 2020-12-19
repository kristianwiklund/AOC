from antlr4 import *
from antlr4.error.ErrorListener import *

from apListener import apListener
from apLexer import apLexer
from apParser import apParser
import sys

class VerboseListener(ErrorListener) :
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        stack = recognizer.getRuleInvocationStack()
        stack.reverse()
        print("ERROR!")
        sys.exit(1)
        
def main():
   input = InputStream(sys.stdin.readline())
   lexer = apLexer(input)
   stream = CommonTokenStream(lexer)
   parser = apParser(stream)
   parser.removeErrorListeners()
   parser.addErrorListener(VerboseListener())
   tree = parser.start()
   
if __name__ == '__main__':
   main()
