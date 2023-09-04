# Generated from /Users/mep/IFI/Research/BlockChainExecVerification/execGrammar/antlr/GramParser.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,46,285,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,3,0,50,8,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,
        70,8,1,1,2,1,2,3,2,74,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,5,4,83,8,4,
        10,4,12,4,86,9,4,1,4,3,4,89,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,122,8,9,1,10,1,10,1,10,1,10,1,10,
        1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,140,
        8,11,1,12,1,12,1,12,1,12,3,12,146,8,12,1,13,1,13,1,13,5,13,151,8,
        13,10,13,12,13,154,9,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,
        3,14,164,8,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,187,
        8,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,209,8,15,10,15,12,15,
        212,9,15,1,16,1,16,1,16,1,16,1,16,3,16,219,8,16,1,17,1,17,3,17,223,
        8,17,1,17,1,17,5,17,227,8,17,10,17,12,17,230,9,17,1,17,1,17,1,18,
        1,18,1,18,1,18,5,18,238,8,18,10,18,12,18,241,9,18,1,18,1,18,1,18,
        3,18,246,8,18,1,19,1,19,1,19,1,19,5,19,252,8,19,10,19,12,19,255,
        9,19,1,19,1,19,1,19,1,19,3,19,261,8,19,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,3,20,283,8,20,1,20,0,1,30,21,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,0,5,1,0,14,15,1,0,29,32,2,0,26,
        26,28,28,1,0,24,25,1,0,11,12,311,0,45,1,0,0,0,2,69,1,0,0,0,4,73,
        1,0,0,0,6,75,1,0,0,0,8,80,1,0,0,0,10,90,1,0,0,0,12,96,1,0,0,0,14,
        103,1,0,0,0,16,106,1,0,0,0,18,121,1,0,0,0,20,123,1,0,0,0,22,139,
        1,0,0,0,24,145,1,0,0,0,26,147,1,0,0,0,28,163,1,0,0,0,30,186,1,0,
        0,0,32,218,1,0,0,0,34,220,1,0,0,0,36,245,1,0,0,0,38,260,1,0,0,0,
        40,282,1,0,0,0,42,44,3,2,1,0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,
        0,0,0,45,46,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,48,50,5,0,0,1,49,
        48,1,0,0,0,49,50,1,0,0,0,50,1,1,0,0,0,51,52,3,6,3,0,52,53,5,21,0,
        0,53,70,1,0,0,0,54,70,3,8,4,0,55,70,3,16,8,0,56,57,3,18,9,0,57,58,
        5,21,0,0,58,70,1,0,0,0,59,70,3,20,10,0,60,61,3,22,11,0,61,62,5,21,
        0,0,62,70,1,0,0,0,63,64,3,24,12,0,64,65,5,21,0,0,65,70,1,0,0,0,66,
        67,3,26,13,0,67,68,5,21,0,0,68,70,1,0,0,0,69,51,1,0,0,0,69,54,1,
        0,0,0,69,55,1,0,0,0,69,56,1,0,0,0,69,59,1,0,0,0,69,60,1,0,0,0,69,
        63,1,0,0,0,69,66,1,0,0,0,70,3,1,0,0,0,71,74,3,30,15,0,72,74,5,40,
        0,0,73,71,1,0,0,0,73,72,1,0,0,0,74,5,1,0,0,0,75,76,5,1,0,0,76,77,
        5,40,0,0,77,78,5,20,0,0,78,79,3,4,2,0,79,7,1,0,0,0,80,84,3,10,5,
        0,81,83,3,12,6,0,82,81,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,
        1,0,0,0,85,88,1,0,0,0,86,84,1,0,0,0,87,89,3,14,7,0,88,87,1,0,0,0,
        88,89,1,0,0,0,89,9,1,0,0,0,90,91,5,18,0,0,91,92,5,34,0,0,92,93,3,
        30,15,0,93,94,5,35,0,0,94,95,3,26,13,0,95,11,1,0,0,0,96,97,5,19,
        0,0,97,98,5,18,0,0,98,99,5,34,0,0,99,100,3,30,15,0,100,101,5,35,
        0,0,101,102,3,26,13,0,102,13,1,0,0,0,103,104,5,19,0,0,104,105,3,
        26,13,0,105,15,1,0,0,0,106,107,5,16,0,0,107,108,5,40,0,0,108,109,
        3,36,18,0,109,110,3,26,13,0,110,17,1,0,0,0,111,112,5,40,0,0,112,
        122,3,38,19,0,113,114,5,9,0,0,114,122,3,38,19,0,115,116,5,6,0,0,
        116,122,3,38,19,0,117,118,5,7,0,0,118,122,3,38,19,0,119,120,5,8,
        0,0,120,122,3,38,19,0,121,111,1,0,0,0,121,113,1,0,0,0,121,115,1,
        0,0,0,121,117,1,0,0,0,121,119,1,0,0,0,122,19,1,0,0,0,123,124,5,10,
        0,0,124,125,5,34,0,0,125,126,3,30,15,0,126,127,5,35,0,0,127,128,
        3,26,13,0,128,21,1,0,0,0,129,130,5,40,0,0,130,131,5,36,0,0,131,132,
        3,30,15,0,132,133,5,37,0,0,133,134,5,20,0,0,134,135,3,4,2,0,135,
        140,1,0,0,0,136,137,5,40,0,0,137,138,5,20,0,0,138,140,3,4,2,0,139,
        129,1,0,0,0,139,136,1,0,0,0,140,23,1,0,0,0,141,142,5,2,0,0,142,146,
        3,38,19,0,143,144,5,3,0,0,144,146,3,38,19,0,145,141,1,0,0,0,145,
        143,1,0,0,0,146,25,1,0,0,0,147,152,5,38,0,0,148,151,3,2,1,0,149,
        151,3,28,14,0,150,148,1,0,0,0,150,149,1,0,0,0,151,154,1,0,0,0,152,
        150,1,0,0,0,152,153,1,0,0,0,153,155,1,0,0,0,154,152,1,0,0,0,155,
        156,5,39,0,0,156,27,1,0,0,0,157,158,5,17,0,0,158,159,3,30,15,0,159,
        160,5,21,0,0,160,164,1,0,0,0,161,162,5,17,0,0,162,164,5,21,0,0,163,
        157,1,0,0,0,163,161,1,0,0,0,164,29,1,0,0,0,165,166,6,15,-1,0,166,
        167,5,34,0,0,167,168,3,30,15,0,168,169,5,35,0,0,169,187,1,0,0,0,
        170,187,3,18,9,0,171,172,5,13,0,0,172,187,3,30,15,9,173,187,3,34,
        17,0,174,187,3,32,16,0,175,176,5,4,0,0,176,177,5,34,0,0,177,178,
        3,30,15,0,178,179,5,35,0,0,179,187,1,0,0,0,180,181,5,5,0,0,181,182,
        5,34,0,0,182,183,3,30,15,0,183,184,5,35,0,0,184,187,1,0,0,0,185,
        187,5,40,0,0,186,165,1,0,0,0,186,170,1,0,0,0,186,171,1,0,0,0,186,
        173,1,0,0,0,186,174,1,0,0,0,186,175,1,0,0,0,186,180,1,0,0,0,186,
        185,1,0,0,0,187,210,1,0,0,0,188,189,10,12,0,0,189,190,7,0,0,0,190,
        209,3,30,15,13,191,192,10,11,0,0,192,193,7,1,0,0,193,209,3,30,15,
        12,194,195,10,10,0,0,195,196,5,33,0,0,196,209,3,30,15,11,197,198,
        10,8,0,0,198,199,5,27,0,0,199,209,3,30,15,9,200,201,10,7,0,0,201,
        202,7,2,0,0,202,209,3,30,15,8,203,204,10,6,0,0,204,205,7,3,0,0,205,
        209,3,30,15,7,206,207,10,13,0,0,207,209,3,40,20,0,208,188,1,0,0,
        0,208,191,1,0,0,0,208,194,1,0,0,0,208,197,1,0,0,0,208,200,1,0,0,
        0,208,203,1,0,0,0,208,206,1,0,0,0,209,212,1,0,0,0,210,208,1,0,0,
        0,210,211,1,0,0,0,211,31,1,0,0,0,212,210,1,0,0,0,213,219,5,41,0,
        0,214,219,5,42,0,0,215,219,5,43,0,0,216,219,7,4,0,0,217,219,5,44,
        0,0,218,213,1,0,0,0,218,214,1,0,0,0,218,215,1,0,0,0,218,216,1,0,
        0,0,218,217,1,0,0,0,219,33,1,0,0,0,220,222,5,36,0,0,221,223,3,30,
        15,0,222,221,1,0,0,0,222,223,1,0,0,0,223,228,1,0,0,0,224,225,5,23,
        0,0,225,227,3,30,15,0,226,224,1,0,0,0,227,230,1,0,0,0,228,226,1,
        0,0,0,228,229,1,0,0,0,229,231,1,0,0,0,230,228,1,0,0,0,231,232,5,
        37,0,0,232,35,1,0,0,0,233,234,5,34,0,0,234,239,5,40,0,0,235,236,
        5,23,0,0,236,238,5,40,0,0,237,235,1,0,0,0,238,241,1,0,0,0,239,237,
        1,0,0,0,239,240,1,0,0,0,240,242,1,0,0,0,241,239,1,0,0,0,242,246,
        5,35,0,0,243,244,5,34,0,0,244,246,5,35,0,0,245,233,1,0,0,0,245,243,
        1,0,0,0,246,37,1,0,0,0,247,248,5,34,0,0,248,253,3,30,15,0,249,250,
        5,23,0,0,250,252,3,30,15,0,251,249,1,0,0,0,252,255,1,0,0,0,253,251,
        1,0,0,0,253,254,1,0,0,0,254,256,1,0,0,0,255,253,1,0,0,0,256,257,
        5,35,0,0,257,261,1,0,0,0,258,259,5,34,0,0,259,261,5,35,0,0,260,247,
        1,0,0,0,260,258,1,0,0,0,261,39,1,0,0,0,262,263,5,36,0,0,263,264,
        3,30,15,0,264,265,5,37,0,0,265,283,1,0,0,0,266,267,5,36,0,0,267,
        268,3,30,15,0,268,269,5,22,0,0,269,270,5,37,0,0,270,283,1,0,0,0,
        271,272,5,36,0,0,272,273,5,22,0,0,273,274,3,30,15,0,274,275,5,37,
        0,0,275,283,1,0,0,0,276,277,5,36,0,0,277,278,3,30,15,0,278,279,5,
        22,0,0,279,280,3,30,15,0,280,281,5,37,0,0,281,283,1,0,0,0,282,262,
        1,0,0,0,282,266,1,0,0,0,282,271,1,0,0,0,282,276,1,0,0,0,283,41,1,
        0,0,0,23,45,49,69,73,84,88,121,139,145,150,152,163,186,208,210,218,
        222,228,239,245,253,260,282
    ]

class GramParser ( Parser ):

    grammarFileName = "GramParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'print'", "'println'", "'lenof'", 
                     "'copyof'", "'floorintof'", "'roundintof'", "'ceilintof'", 
                     "'sin'", "'while'", "'True'", "'False'", "'not'", "'and'", 
                     "'or'", "'decl'", "'ret'", "'if'", "'else'", "'='", 
                     "';'", "':'", "','", "'+'", "'-'", "'*'", "'**'", "'/'", 
                     "'<'", "'<='", "'>'", "'>='", "'=='", "'('", "')'", 
                     "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "VAR", "PRINT", "PRINTLN", "LENOF", "COPYOF", 
                      "FLOORINTOF", "ROUNDINTOF", "CEILINTOF", "SIN", "WHILE", 
                      "TRUE", "FALSE", "NOT", "AND", "OR", "DECL", "RET", 
                      "IF", "ELSE", "ASSIGN", "SEMI", "COLON", "COMMA", 
                      "PLUS", "MINUS", "TIMES", "POW", "DIV", "LESSTHAN", 
                      "LESSTHANOREQUAL", "GREATERTHAN", "GREATERTHANOREQUAL", 
                      "EQUALS", "LPAREN", "RPAREN", "LBRACK", "RBRACK", 
                      "LBRACE", "RBRACE", "IDEN", "INT", "FLOAT", "CHAR", 
                      "STRING", "LINE_COMMENT", "WS" ]

    RULE_program = 0
    RULE_stmt = 1
    RULE_assig_trgt = 2
    RULE_var_declr = 3
    RULE_if_block = 4
    RULE_if_stmt = 5
    RULE_elseif_stmt = 6
    RULE_else_stmt = 7
    RULE_func_decl = 8
    RULE_func_call_expr = 9
    RULE_while = 10
    RULE_assig = 11
    RULE_print = 12
    RULE_stmt_block = 13
    RULE_ret_stmt = 14
    RULE_expr = 15
    RULE_literal = 16
    RULE_lst_decl = 17
    RULE_param_lst = 18
    RULE_arg_lst = 19
    RULE_idx_access = 20

    ruleNames =  [ "program", "stmt", "assig_trgt", "var_declr", "if_block", 
                   "if_stmt", "elseif_stmt", "else_stmt", "func_decl", "func_call_expr", 
                   "while", "assig", "print", "stmt_block", "ret_stmt", 
                   "expr", "literal", "lst_decl", "param_lst", "arg_lst", 
                   "idx_access" ]

    EOF = Token.EOF
    VAR=1
    PRINT=2
    PRINTLN=3
    LENOF=4
    COPYOF=5
    FLOORINTOF=6
    ROUNDINTOF=7
    CEILINTOF=8
    SIN=9
    WHILE=10
    TRUE=11
    FALSE=12
    NOT=13
    AND=14
    OR=15
    DECL=16
    RET=17
    IF=18
    ELSE=19
    ASSIGN=20
    SEMI=21
    COLON=22
    COMMA=23
    PLUS=24
    MINUS=25
    TIMES=26
    POW=27
    DIV=28
    LESSTHAN=29
    LESSTHANOREQUAL=30
    GREATERTHAN=31
    GREATERTHANOREQUAL=32
    EQUALS=33
    LPAREN=34
    RPAREN=35
    LBRACK=36
    RBRACK=37
    LBRACE=38
    RBRACE=39
    IDEN=40
    INT=41
    FLOAT=42
    CHAR=43
    STRING=44
    LINE_COMMENT=45
    WS=46

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.StmtContext)
            else:
                return self.getTypedRuleContext(GramParser.StmtContext,i)


        def EOF(self):
            return self.getToken(GramParser.EOF, 0)

        def getRuleIndex(self):
            return GramParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = GramParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1374389864398) != 0):
                self.state = 42
                self.stmt()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 48
                self.match(GramParser.EOF)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Stmt_if_blockContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def if_block(self):
            return self.getTypedRuleContext(GramParser.If_blockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_if_block" ):
                listener.enterStmt_if_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_if_block" ):
                listener.exitStmt_if_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_if_block" ):
                return visitor.visitStmt_if_block(self)
            else:
                return visitor.visitChildren(self)


    class Stmt_stmt_blockContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stmt_block(self):
            return self.getTypedRuleContext(GramParser.Stmt_blockContext,0)

        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_stmt_block" ):
                listener.enterStmt_stmt_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_stmt_block" ):
                listener.exitStmt_stmt_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_stmt_block" ):
                return visitor.visitStmt_stmt_block(self)
            else:
                return visitor.visitChildren(self)


    class Stmt_func_declContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func_decl(self):
            return self.getTypedRuleContext(GramParser.Func_declContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_func_decl" ):
                listener.enterStmt_func_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_func_decl" ):
                listener.exitStmt_func_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_func_decl" ):
                return visitor.visitStmt_func_decl(self)
            else:
                return visitor.visitChildren(self)


    class Stmt_assigContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assig(self):
            return self.getTypedRuleContext(GramParser.AssigContext,0)

        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_assig" ):
                listener.enterStmt_assig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_assig" ):
                listener.exitStmt_assig(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_assig" ):
                return visitor.visitStmt_assig(self)
            else:
                return visitor.visitChildren(self)


    class Stmt_whileContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def while_(self):
            return self.getTypedRuleContext(GramParser.WhileContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_while" ):
                listener.enterStmt_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_while" ):
                listener.exitStmt_while(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_while" ):
                return visitor.visitStmt_while(self)
            else:
                return visitor.visitChildren(self)


    class Stmt_func_callContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func_call_expr(self):
            return self.getTypedRuleContext(GramParser.Func_call_exprContext,0)

        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_func_call" ):
                listener.enterStmt_func_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_func_call" ):
                listener.exitStmt_func_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_func_call" ):
                return visitor.visitStmt_func_call(self)
            else:
                return visitor.visitChildren(self)


    class Stmt_printContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def print_(self):
            return self.getTypedRuleContext(GramParser.PrintContext,0)

        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_print" ):
                listener.enterStmt_print(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_print" ):
                listener.exitStmt_print(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_print" ):
                return visitor.visitStmt_print(self)
            else:
                return visitor.visitChildren(self)


    class Stmt_var_declrContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def var_declr(self):
            return self.getTypedRuleContext(GramParser.Var_declrContext,0)

        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_var_declr" ):
                listener.enterStmt_var_declr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_var_declr" ):
                listener.exitStmt_var_declr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_var_declr" ):
                return visitor.visitStmt_var_declr(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = GramParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = GramParser.Stmt_var_declrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.var_declr()
                self.state = 52
                self.match(GramParser.SEMI)
                pass

            elif la_ == 2:
                localctx = GramParser.Stmt_if_blockContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.if_block()
                pass

            elif la_ == 3:
                localctx = GramParser.Stmt_func_declContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.func_decl()
                pass

            elif la_ == 4:
                localctx = GramParser.Stmt_func_callContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.func_call_expr()
                self.state = 57
                self.match(GramParser.SEMI)
                pass

            elif la_ == 5:
                localctx = GramParser.Stmt_whileContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 59
                self.while_()
                pass

            elif la_ == 6:
                localctx = GramParser.Stmt_assigContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 60
                self.assig()
                self.state = 61
                self.match(GramParser.SEMI)
                pass

            elif la_ == 7:
                localctx = GramParser.Stmt_printContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 63
                self.print_()
                self.state = 64
                self.match(GramParser.SEMI)
                pass

            elif la_ == 8:
                localctx = GramParser.Stmt_stmt_blockContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 66
                self.stmt_block()
                self.state = 67
                self.match(GramParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assig_trgtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramParser.RULE_assig_trgt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Assig_trgt_exprContext(Assig_trgtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Assig_trgtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssig_trgt_expr" ):
                listener.enterAssig_trgt_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssig_trgt_expr" ):
                listener.exitAssig_trgt_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssig_trgt_expr" ):
                return visitor.visitAssig_trgt_expr(self)
            else:
                return visitor.visitChildren(self)


    class Assig_trgt_idenContext(Assig_trgtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Assig_trgtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDEN(self):
            return self.getToken(GramParser.IDEN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssig_trgt_iden" ):
                listener.enterAssig_trgt_iden(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssig_trgt_iden" ):
                listener.exitAssig_trgt_iden(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssig_trgt_iden" ):
                return visitor.visitAssig_trgt_iden(self)
            else:
                return visitor.visitChildren(self)



    def assig_trgt(self):

        localctx = GramParser.Assig_trgtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assig_trgt)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = GramParser.Assig_trgt_exprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = GramParser.Assig_trgt_idenContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.match(GramParser.IDEN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(GramParser.VAR, 0)

        def IDEN(self):
            return self.getToken(GramParser.IDEN, 0)

        def ASSIGN(self):
            return self.getToken(GramParser.ASSIGN, 0)

        def assig_trgt(self):
            return self.getTypedRuleContext(GramParser.Assig_trgtContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_var_declr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_declr" ):
                listener.enterVar_declr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_declr" ):
                listener.exitVar_declr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declr" ):
                return visitor.visitVar_declr(self)
            else:
                return visitor.visitChildren(self)




    def var_declr(self):

        localctx = GramParser.Var_declrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_declr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(GramParser.VAR)
            self.state = 76
            self.match(GramParser.IDEN)
            self.state = 77
            self.match(GramParser.ASSIGN)
            self.state = 78
            self.assig_trgt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(GramParser.If_stmtContext,0)


        def elseif_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.Elseif_stmtContext)
            else:
                return self.getTypedRuleContext(GramParser.Elseif_stmtContext,i)


        def else_stmt(self):
            return self.getTypedRuleContext(GramParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_if_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_block" ):
                listener.enterIf_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_block" ):
                listener.exitIf_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_block" ):
                return visitor.visitIf_block(self)
            else:
                return visitor.visitChildren(self)




    def if_block(self):

        localctx = GramParser.If_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_if_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.if_stmt()
            self.state = 84
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 81
                    self.elseif_stmt() 
                self.state = 86
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 87
                self.else_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(GramParser.IF, 0)

        def LPAREN(self):
            return self.getToken(GramParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(GramParser.RPAREN, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(GramParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = GramParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(GramParser.IF)
            self.state = 91
            self.match(GramParser.LPAREN)
            self.state = 92
            self.expr(0)
            self.state = 93
            self.match(GramParser.RPAREN)
            self.state = 94
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(GramParser.ELSE, 0)

        def IF(self):
            return self.getToken(GramParser.IF, 0)

        def LPAREN(self):
            return self.getToken(GramParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(GramParser.RPAREN, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(GramParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_elseif_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseif_stmt" ):
                listener.enterElseif_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseif_stmt" ):
                listener.exitElseif_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stmt" ):
                return visitor.visitElseif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stmt(self):

        localctx = GramParser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_elseif_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(GramParser.ELSE)
            self.state = 97
            self.match(GramParser.IF)
            self.state = 98
            self.match(GramParser.LPAREN)
            self.state = 99
            self.expr(0)
            self.state = 100
            self.match(GramParser.RPAREN)
            self.state = 101
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(GramParser.ELSE, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(GramParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_else_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_stmt" ):
                listener.enterElse_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_stmt" ):
                listener.exitElse_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = GramParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(GramParser.ELSE)
            self.state = 104
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECL(self):
            return self.getToken(GramParser.DECL, 0)

        def IDEN(self):
            return self.getToken(GramParser.IDEN, 0)

        def param_lst(self):
            return self.getTypedRuleContext(GramParser.Param_lstContext,0)


        def stmt_block(self):
            return self.getTypedRuleContext(GramParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_func_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_decl" ):
                listener.enterFunc_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_decl" ):
                listener.exitFunc_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_decl" ):
                return visitor.visitFunc_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_decl(self):

        localctx = GramParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_func_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(GramParser.DECL)
            self.state = 107
            self.match(GramParser.IDEN)
            self.state = 108
            self.param_lst()
            self.state = 109
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_call_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramParser.RULE_func_call_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Sin_callContext(Func_call_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Func_call_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIN(self):
            return self.getToken(GramParser.SIN, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSin_call" ):
                listener.enterSin_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSin_call" ):
                listener.exitSin_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSin_call" ):
                return visitor.visitSin_call(self)
            else:
                return visitor.visitChildren(self)


    class Floor_callContext(Func_call_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Func_call_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOORINTOF(self):
            return self.getToken(GramParser.FLOORINTOF, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloor_call" ):
                listener.enterFloor_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloor_call" ):
                listener.exitFloor_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloor_call" ):
                return visitor.visitFloor_call(self)
            else:
                return visitor.visitChildren(self)


    class Ceil_callContext(Func_call_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Func_call_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CEILINTOF(self):
            return self.getToken(GramParser.CEILINTOF, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCeil_call" ):
                listener.enterCeil_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCeil_call" ):
                listener.exitCeil_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCeil_call" ):
                return visitor.visitCeil_call(self)
            else:
                return visitor.visitChildren(self)


    class Round_callContext(Func_call_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Func_call_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ROUNDINTOF(self):
            return self.getToken(GramParser.ROUNDINTOF, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRound_call" ):
                listener.enterRound_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRound_call" ):
                listener.exitRound_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRound_call" ):
                return visitor.visitRound_call(self)
            else:
                return visitor.visitChildren(self)


    class Func_callContext(Func_call_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Func_call_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDEN(self):
            return self.getToken(GramParser.IDEN, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)



    def func_call_expr(self):

        localctx = GramParser.Func_call_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_func_call_expr)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [40]:
                localctx = GramParser.Func_callContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.match(GramParser.IDEN)
                self.state = 112
                self.arg_lst()
                pass
            elif token in [9]:
                localctx = GramParser.Sin_callContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(GramParser.SIN)
                self.state = 114
                self.arg_lst()
                pass
            elif token in [6]:
                localctx = GramParser.Floor_callContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self.match(GramParser.FLOORINTOF)
                self.state = 116
                self.arg_lst()
                pass
            elif token in [7]:
                localctx = GramParser.Round_callContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 117
                self.match(GramParser.ROUNDINTOF)
                self.state = 118
                self.arg_lst()
                pass
            elif token in [8]:
                localctx = GramParser.Ceil_callContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 119
                self.match(GramParser.CEILINTOF)
                self.state = 120
                self.arg_lst()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(GramParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(GramParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(GramParser.RPAREN, 0)

        def stmt_block(self):
            return self.getTypedRuleContext(GramParser.Stmt_blockContext,0)


        def getRuleIndex(self):
            return GramParser.RULE_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = GramParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(GramParser.WHILE)
            self.state = 124
            self.match(GramParser.LPAREN)
            self.state = 125
            self.expr(0)
            self.state = 126
            self.match(GramParser.RPAREN)
            self.state = 127
            self.stmt_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramParser.RULE_assig

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Assign_accessContext(AssigContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.AssigContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDEN(self):
            return self.getToken(GramParser.IDEN, 0)
        def LBRACK(self):
            return self.getToken(GramParser.LBRACK, 0)
        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)

        def RBRACK(self):
            return self.getToken(GramParser.RBRACK, 0)
        def ASSIGN(self):
            return self.getToken(GramParser.ASSIGN, 0)
        def assig_trgt(self):
            return self.getTypedRuleContext(GramParser.Assig_trgtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_access" ):
                listener.enterAssign_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_access" ):
                listener.exitAssign_access(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_access" ):
                return visitor.visitAssign_access(self)
            else:
                return visitor.visitChildren(self)


    class Assign_idenContext(AssigContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.AssigContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDEN(self):
            return self.getToken(GramParser.IDEN, 0)
        def ASSIGN(self):
            return self.getToken(GramParser.ASSIGN, 0)
        def assig_trgt(self):
            return self.getTypedRuleContext(GramParser.Assig_trgtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_iden" ):
                listener.enterAssign_iden(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_iden" ):
                listener.exitAssign_iden(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_iden" ):
                return visitor.visitAssign_iden(self)
            else:
                return visitor.visitChildren(self)



    def assig(self):

        localctx = GramParser.AssigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assig)
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = GramParser.Assign_accessContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(GramParser.IDEN)
                self.state = 130
                self.match(GramParser.LBRACK)
                self.state = 131
                self.expr(0)
                self.state = 132
                self.match(GramParser.RBRACK)
                self.state = 133
                self.match(GramParser.ASSIGN)
                self.state = 134
                self.assig_trgt()
                pass

            elif la_ == 2:
                localctx = GramParser.Assign_idenContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 136
                self.match(GramParser.IDEN)
                self.state = 137
                self.match(GramParser.ASSIGN)
                self.state = 138
                self.assig_trgt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramParser.RULE_print

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Print_nlContext(PrintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.PrintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINTLN(self):
            return self.getToken(GramParser.PRINTLN, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_nl" ):
                listener.enterPrint_nl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_nl" ):
                listener.exitPrint_nl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_nl" ):
                return visitor.visitPrint_nl(self)
            else:
                return visitor.visitChildren(self)


    class Print_baseContext(PrintContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.PrintContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(GramParser.PRINT, 0)
        def arg_lst(self):
            return self.getTypedRuleContext(GramParser.Arg_lstContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_base" ):
                listener.enterPrint_base(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_base" ):
                listener.exitPrint_base(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_base" ):
                return visitor.visitPrint_base(self)
            else:
                return visitor.visitChildren(self)



    def print_(self):

        localctx = GramParser.PrintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_print)
        try:
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = GramParser.Print_baseContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(GramParser.PRINT)
                self.state = 142
                self.arg_lst()
                pass
            elif token in [3]:
                localctx = GramParser.Print_nlContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.match(GramParser.PRINTLN)
                self.state = 144
                self.arg_lst()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(GramParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(GramParser.RBRACE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.StmtContext)
            else:
                return self.getTypedRuleContext(GramParser.StmtContext,i)


        def ret_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.Ret_stmtContext)
            else:
                return self.getTypedRuleContext(GramParser.Ret_stmtContext,i)


        def getRuleIndex(self):
            return GramParser.RULE_stmt_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_block" ):
                listener.enterStmt_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_block" ):
                listener.exitStmt_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_block" ):
                return visitor.visitStmt_block(self)
            else:
                return visitor.visitChildren(self)




    def stmt_block(self):

        localctx = GramParser.Stmt_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmt_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(GramParser.LBRACE)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1374389995470) != 0):
                self.state = 150
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2, 3, 6, 7, 8, 9, 10, 16, 18, 38, 40]:
                    self.state = 148
                    self.stmt()
                    pass
                elif token in [17]:
                    self.state = 149
                    self.ret_stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 155
            self.match(GramParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ret_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RET(self):
            return self.getToken(GramParser.RET, 0)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(GramParser.SEMI, 0)

        def getRuleIndex(self):
            return GramParser.RULE_ret_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRet_stmt" ):
                listener.enterRet_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRet_stmt" ):
                listener.exitRet_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRet_stmt" ):
                return visitor.visitRet_stmt(self)
            else:
                return visitor.visitChildren(self)




    def ret_stmt(self):

        localctx = GramParser.Ret_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ret_stmt)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(GramParser.RET)
                self.state = 158
                self.expr(0)
                self.state = 159
                self.match(GramParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.match(GramParser.RET)
                self.state = 162
                self.match(GramParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Bool_expr_prefContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(GramParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_expr_pref" ):
                listener.enterBool_expr_pref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_expr_pref" ):
                listener.exitBool_expr_pref(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_expr_pref" ):
                return visitor.visitBool_expr_pref(self)
            else:
                return visitor.visitChildren(self)


    class Expr_lst_declContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lst_decl(self):
            return self.getTypedRuleContext(GramParser.Lst_declContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_lst_decl" ):
                listener.enterExpr_lst_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_lst_decl" ):
                listener.exitExpr_lst_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_lst_decl" ):
                return visitor.visitExpr_lst_decl(self)
            else:
                return visitor.visitChildren(self)


    class Bool_expr_comp_mathContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)

        def LESSTHAN(self):
            return self.getToken(GramParser.LESSTHAN, 0)
        def LESSTHANOREQUAL(self):
            return self.getToken(GramParser.LESSTHANOREQUAL, 0)
        def GREATERTHAN(self):
            return self.getToken(GramParser.GREATERTHAN, 0)
        def GREATERTHANOREQUAL(self):
            return self.getToken(GramParser.GREATERTHANOREQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_expr_comp_math" ):
                listener.enterBool_expr_comp_math(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_expr_comp_math" ):
                listener.exitBool_expr_comp_math(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_expr_comp_math" ):
                return visitor.visitBool_expr_comp_math(self)
            else:
                return visitor.visitChildren(self)


    class Expr_parenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(GramParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(GramParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_paren" ):
                listener.enterExpr_paren(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_paren" ):
                listener.exitExpr_paren(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_paren" ):
                return visitor.visitExpr_paren(self)
            else:
                return visitor.visitChildren(self)


    class Bool_expr_binaryContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)

        def AND(self):
            return self.getToken(GramParser.AND, 0)
        def OR(self):
            return self.getToken(GramParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_expr_binary" ):
                listener.enterBool_expr_binary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_expr_binary" ):
                listener.exitBool_expr_binary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_expr_binary" ):
                return visitor.visitBool_expr_binary(self)
            else:
                return visitor.visitChildren(self)


    class Expr_idenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDEN(self):
            return self.getToken(GramParser.IDEN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_iden" ):
                listener.enterExpr_iden(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_iden" ):
                listener.exitExpr_iden(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_iden" ):
                return visitor.visitExpr_iden(self)
            else:
                return visitor.visitChildren(self)


    class Expr_len_ofContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LENOF(self):
            return self.getToken(GramParser.LENOF, 0)
        def LPAREN(self):
            return self.getToken(GramParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(GramParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_len_of" ):
                listener.enterExpr_len_of(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_len_of" ):
                listener.exitExpr_len_of(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_len_of" ):
                return visitor.visitExpr_len_of(self)
            else:
                return visitor.visitChildren(self)


    class Expr_litContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(GramParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_lit" ):
                listener.enterExpr_lit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_lit" ):
                listener.exitExpr_lit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_lit" ):
                return visitor.visitExpr_lit(self)
            else:
                return visitor.visitChildren(self)


    class Bool_expr_equalsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)

        def EQUALS(self):
            return self.getToken(GramParser.EQUALS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_expr_equals" ):
                listener.enterBool_expr_equals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_expr_equals" ):
                listener.exitBool_expr_equals(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_expr_equals" ):
                return visitor.visitBool_expr_equals(self)
            else:
                return visitor.visitChildren(self)


    class Expr_accessContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)

        def idx_access(self):
            return self.getTypedRuleContext(GramParser.Idx_accessContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_access" ):
                listener.enterExpr_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_access" ):
                listener.exitExpr_access(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_access" ):
                return visitor.visitExpr_access(self)
            else:
                return visitor.visitChildren(self)


    class Expr_copy_ofContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COPYOF(self):
            return self.getToken(GramParser.COPYOF, 0)
        def LPAREN(self):
            return self.getToken(GramParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(GramParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_copy_of" ):
                listener.enterExpr_copy_of(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_copy_of" ):
                listener.exitExpr_copy_of(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_copy_of" ):
                return visitor.visitExpr_copy_of(self)
            else:
                return visitor.visitChildren(self)


    class Math_expr_binaryContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)

        def POW(self):
            return self.getToken(GramParser.POW, 0)
        def TIMES(self):
            return self.getToken(GramParser.TIMES, 0)
        def DIV(self):
            return self.getToken(GramParser.DIV, 0)
        def PLUS(self):
            return self.getToken(GramParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(GramParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMath_expr_binary" ):
                listener.enterMath_expr_binary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMath_expr_binary" ):
                listener.exitMath_expr_binary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMath_expr_binary" ):
                return visitor.visitMath_expr_binary(self)
            else:
                return visitor.visitChildren(self)


    class Expr_func_callContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func_call_expr(self):
            return self.getTypedRuleContext(GramParser.Func_call_exprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_func_call" ):
                listener.enterExpr_func_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_func_call" ):
                listener.exitExpr_func_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_func_call" ):
                return visitor.visitExpr_func_call(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GramParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = GramParser.Expr_parenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 166
                self.match(GramParser.LPAREN)
                self.state = 167
                self.expr(0)
                self.state = 168
                self.match(GramParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = GramParser.Expr_func_callContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 170
                self.func_call_expr()
                pass

            elif la_ == 3:
                localctx = GramParser.Bool_expr_prefContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 171
                self.match(GramParser.NOT)
                self.state = 172
                self.expr(9)
                pass

            elif la_ == 4:
                localctx = GramParser.Expr_lst_declContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 173
                self.lst_decl()
                pass

            elif la_ == 5:
                localctx = GramParser.Expr_litContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 174
                self.literal()
                pass

            elif la_ == 6:
                localctx = GramParser.Expr_len_ofContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 175
                self.match(GramParser.LENOF)
                self.state = 176
                self.match(GramParser.LPAREN)
                self.state = 177
                self.expr(0)
                self.state = 178
                self.match(GramParser.RPAREN)
                pass

            elif la_ == 7:
                localctx = GramParser.Expr_copy_ofContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 180
                self.match(GramParser.COPYOF)
                self.state = 181
                self.match(GramParser.LPAREN)
                self.state = 182
                self.expr(0)
                self.state = 183
                self.match(GramParser.RPAREN)
                pass

            elif la_ == 8:
                localctx = GramParser.Expr_idenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 185
                self.match(GramParser.IDEN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 208
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = GramParser.Bool_expr_binaryContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 188
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 189
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 190
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = GramParser.Bool_expr_comp_mathContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 191
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 192
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8053063680) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 193
                        self.expr(12)
                        pass

                    elif la_ == 3:
                        localctx = GramParser.Bool_expr_equalsContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 194
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 195
                        self.match(GramParser.EQUALS)
                        self.state = 196
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = GramParser.Math_expr_binaryContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 197
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 198
                        self.match(GramParser.POW)
                        self.state = 199
                        self.expr(9)
                        pass

                    elif la_ == 5:
                        localctx = GramParser.Math_expr_binaryContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 200
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 201
                        _la = self._input.LA(1)
                        if not(_la==26 or _la==28):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 202
                        self.expr(8)
                        pass

                    elif la_ == 6:
                        localctx = GramParser.Math_expr_binaryContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 203
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 204
                        _la = self._input.LA(1)
                        if not(_la==24 or _la==25):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 205
                        self.expr(7)
                        pass

                    elif la_ == 7:
                        localctx = GramParser.Expr_accessContext(self, GramParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 206
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 207
                        self.idx_access()
                        pass

             
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Int_litContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(GramParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_lit" ):
                listener.enterInt_lit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_lit" ):
                listener.exitInt_lit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_lit" ):
                return visitor.visitInt_lit(self)
            else:
                return visitor.visitChildren(self)


    class Float_litContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(GramParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_lit" ):
                listener.enterFloat_lit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_lit" ):
                listener.exitFloat_lit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_lit" ):
                return visitor.visitFloat_lit(self)
            else:
                return visitor.visitChildren(self)


    class String_litContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(GramParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_lit" ):
                listener.enterString_lit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_lit" ):
                listener.exitString_lit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_lit" ):
                return visitor.visitString_lit(self)
            else:
                return visitor.visitChildren(self)


    class Char_litContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CHAR(self):
            return self.getToken(GramParser.CHAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar_lit" ):
                listener.enterChar_lit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar_lit" ):
                listener.exitChar_lit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChar_lit" ):
                return visitor.visitChar_lit(self)
            else:
                return visitor.visitChildren(self)


    class Bool_litContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(GramParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(GramParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_lit" ):
                listener.enterBool_lit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_lit" ):
                listener.exitBool_lit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_lit" ):
                return visitor.visitBool_lit(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = GramParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                localctx = GramParser.Int_litContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(GramParser.INT)
                pass
            elif token in [42]:
                localctx = GramParser.Float_litContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.match(GramParser.FLOAT)
                pass
            elif token in [43]:
                localctx = GramParser.Char_litContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 215
                self.match(GramParser.CHAR)
                pass
            elif token in [11, 12]:
                localctx = GramParser.Bool_litContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 216
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [44]:
                localctx = GramParser.String_litContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 217
                self.match(GramParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lst_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(GramParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(GramParser.RBRACK, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramParser.COMMA)
            else:
                return self.getToken(GramParser.COMMA, i)

        def getRuleIndex(self):
            return GramParser.RULE_lst_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLst_decl" ):
                listener.enterLst_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLst_decl" ):
                listener.exitLst_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLst_decl" ):
                return visitor.visitLst_decl(self)
            else:
                return visitor.visitChildren(self)




    def lst_decl(self):

        localctx = GramParser.Lst_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_lst_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(GramParser.LBRACK)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34170759822320) != 0):
                self.state = 221
                self.expr(0)


            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 224
                self.match(GramParser.COMMA)
                self.state = 225
                self.expr(0)
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 231
            self.match(GramParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(GramParser.LPAREN, 0)

        def IDEN(self, i:int=None):
            if i is None:
                return self.getTokens(GramParser.IDEN)
            else:
                return self.getToken(GramParser.IDEN, i)

        def RPAREN(self):
            return self.getToken(GramParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramParser.COMMA)
            else:
                return self.getToken(GramParser.COMMA, i)

        def getRuleIndex(self):
            return GramParser.RULE_param_lst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_lst" ):
                listener.enterParam_lst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_lst" ):
                listener.exitParam_lst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_lst" ):
                return visitor.visitParam_lst(self)
            else:
                return visitor.visitChildren(self)




    def param_lst(self):

        localctx = GramParser.Param_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_param_lst)
        self._la = 0 # Token type
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(GramParser.LPAREN)
                self.state = 234
                self.match(GramParser.IDEN)
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==23:
                    self.state = 235
                    self.match(GramParser.COMMA)
                    self.state = 236
                    self.match(GramParser.IDEN)
                    self.state = 241
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 242
                self.match(GramParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.match(GramParser.LPAREN)
                self.state = 244
                self.match(GramParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_lstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(GramParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(GramParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramParser.COMMA)
            else:
                return self.getToken(GramParser.COMMA, i)

        def getRuleIndex(self):
            return GramParser.RULE_arg_lst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_lst" ):
                listener.enterArg_lst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_lst" ):
                listener.exitArg_lst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_lst" ):
                return visitor.visitArg_lst(self)
            else:
                return visitor.visitChildren(self)




    def arg_lst(self):

        localctx = GramParser.Arg_lstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arg_lst)
        self._la = 0 # Token type
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(GramParser.LPAREN)
                self.state = 248
                self.expr(0)
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==23:
                    self.state = 249
                    self.match(GramParser.COMMA)
                    self.state = 250
                    self.expr(0)
                    self.state = 255
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 256
                self.match(GramParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                self.match(GramParser.LPAREN)
                self.state = 259
                self.match(GramParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idx_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GramParser.RULE_idx_access

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Idx_access_oneContext(Idx_accessContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Idx_accessContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACK(self):
            return self.getToken(GramParser.LBRACK, 0)
        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)

        def RBRACK(self):
            return self.getToken(GramParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdx_access_one" ):
                listener.enterIdx_access_one(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdx_access_one" ):
                listener.exitIdx_access_one(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdx_access_one" ):
                return visitor.visitIdx_access_one(self)
            else:
                return visitor.visitChildren(self)


    class Idx_access_fromContext(Idx_accessContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Idx_accessContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACK(self):
            return self.getToken(GramParser.LBRACK, 0)
        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)

        def COLON(self):
            return self.getToken(GramParser.COLON, 0)
        def RBRACK(self):
            return self.getToken(GramParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdx_access_from" ):
                listener.enterIdx_access_from(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdx_access_from" ):
                listener.exitIdx_access_from(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdx_access_from" ):
                return visitor.visitIdx_access_from(self)
            else:
                return visitor.visitChildren(self)


    class Idx_access_untilContext(Idx_accessContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Idx_accessContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACK(self):
            return self.getToken(GramParser.LBRACK, 0)
        def COLON(self):
            return self.getToken(GramParser.COLON, 0)
        def expr(self):
            return self.getTypedRuleContext(GramParser.ExprContext,0)

        def RBRACK(self):
            return self.getToken(GramParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdx_access_until" ):
                listener.enterIdx_access_until(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdx_access_until" ):
                listener.exitIdx_access_until(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdx_access_until" ):
                return visitor.visitIdx_access_until(self)
            else:
                return visitor.visitChildren(self)


    class Idx_access_rangeContext(Idx_accessContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GramParser.Idx_accessContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRACK(self):
            return self.getToken(GramParser.LBRACK, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GramParser.ExprContext)
            else:
                return self.getTypedRuleContext(GramParser.ExprContext,i)

        def COLON(self):
            return self.getToken(GramParser.COLON, 0)
        def RBRACK(self):
            return self.getToken(GramParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdx_access_range" ):
                listener.enterIdx_access_range(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdx_access_range" ):
                listener.exitIdx_access_range(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdx_access_range" ):
                return visitor.visitIdx_access_range(self)
            else:
                return visitor.visitChildren(self)



    def idx_access(self):

        localctx = GramParser.Idx_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_idx_access)
        try:
            self.state = 282
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = GramParser.Idx_access_oneContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.match(GramParser.LBRACK)
                self.state = 263
                self.expr(0)
                self.state = 264
                self.match(GramParser.RBRACK)
                pass

            elif la_ == 2:
                localctx = GramParser.Idx_access_fromContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.match(GramParser.LBRACK)
                self.state = 267
                self.expr(0)
                self.state = 268
                self.match(GramParser.COLON)
                self.state = 269
                self.match(GramParser.RBRACK)
                pass

            elif la_ == 3:
                localctx = GramParser.Idx_access_untilContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 271
                self.match(GramParser.LBRACK)
                self.state = 272
                self.match(GramParser.COLON)
                self.state = 273
                self.expr(0)
                self.state = 274
                self.match(GramParser.RBRACK)
                pass

            elif la_ == 4:
                localctx = GramParser.Idx_access_rangeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 276
                self.match(GramParser.LBRACK)
                self.state = 277
                self.expr(0)
                self.state = 278
                self.match(GramParser.COLON)
                self.state = 279
                self.expr(0)
                self.state = 280
                self.match(GramParser.RBRACK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 13)
         




