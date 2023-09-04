lexer grammar GramLexer;

VAR: 'var';
PRINT: 'print';
PRINTLN: 'println';
LENOF: 'lenof';
COPYOF: 'copyof';
FLOORINTOF: 'floorintof';
ROUNDINTOF: 'roundintof';
CEILINTOF: 'ceilintof';
SIN: 'sin';
WHILE: 'while';

TRUE: 'True';
FALSE: 'False';

NOT: 'not';
AND: 'and';
OR: 'or';

DECL: 'decl';
RET:  'ret';

IF: 'if';
ELSE: 'else';

ASSIGN: '=';
SEMI: ';';
COLON: ':';
COMMA: ',';
PLUS: '+';
MINUS: '-';
TIMES: '*';
POW: '**';
DIV: '/';
LESSTHAN: '<';
LESSTHANOREQUAL: '<=';
GREATERTHAN: '>';
GREATERTHANOREQUAL: '>=';
EQUALS: '==';
LPAREN: '(';
RPAREN: ')';
LBRACK: '[';
RBRACK: ']';
LBRACE: '{';
RBRACE: '}';

IDEN
    : [A-Za-z_]+ [A-Za-z_0-9]*
    ;

INT
   : '-'? ('0' | [1-9]) [0-9]*
   ;

FLOAT
   : '-'? INT ('.' [0-9]+)?
   ;

CHAR
    : '\'' ('\'' | ~["\n\r]) '\''
    ;

STRING
    : '"'
      ( '\\"'
      | ~["\n\r]
      )*
      '"'
    ;

LINE_COMMENT
    : '//' ~[\n]* -> channel(HIDDEN)
    ;

WS
    : [ \n\t\r]+ -> skip
    ;
