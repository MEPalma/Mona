parser grammar GramParser;

options {
    tokenVocab=GramLexer;
}


//#####################
//# Compilation Point #
//#####################
program
    : stmt* EOF?
    ;


//##############
//# Statements #
//##############
stmt
    : var_declr SEMI       #stmt_var_declr
    | if_block             #stmt_if_block
    | func_decl            #stmt_func_decl
    | func_call_expr SEMI  #stmt_func_call
    | while                #stmt_while
    | assig SEMI           #stmt_assig
    | print SEMI           #stmt_print
    | stmt_block SEMI      #stmt_stmt_block
    ;
//
assig_trgt
    : expr  #assig_trgt_expr
    | IDEN  #assig_trgt_iden
    ;
//
var_declr
    : VAR IDEN ASSIGN assig_trgt
    ;
//
if_block
    : if_stmt elseif_stmt* else_stmt?
    ;
if_stmt
    : IF LPAREN expr RPAREN stmt_block
    ;
elseif_stmt
    : ELSE IF LPAREN expr RPAREN stmt_block
    ;
else_stmt
    : ELSE stmt_block
    ;
//
func_decl
    : DECL
      IDEN
      param_lst
      stmt_block
    ;
//
func_call_expr
    : IDEN arg_lst        #func_call
    | SIN arg_lst         #sin_call
    | FLOORINTOF arg_lst   #floor_call
    | ROUNDINTOF arg_lst  #round_call
    | CEILINTOF arg_lst   #ceil_call
    ;
//
while
    : WHILE LPAREN expr RPAREN stmt_block
    ;
//
assig
    : IDEN LBRACK expr RBRACK ASSIGN assig_trgt  #assign_access
    | IDEN ASSIGN assig_trgt                     #assign_iden
    ;
//
print
    : PRINT arg_lst    #print_base
    | PRINTLN arg_lst  #print_nl
    ;
//
//###################
//# Statement Scope #
//###################
stmt_block
    : LBRACE
      (stmt | ret_stmt)*
      RBRACE
    ;
ret_stmt
    : RET expr SEMI
    | RET SEMI
    ;

//###############
//# Expressions #
//###############
expr
    : LPAREN expr RPAREN                #expr_paren
    | func_call_expr                    #expr_func_call
    | expr idx_access                   #expr_access
    // boolean expressions
    | expr (AND | OR) expr              #bool_expr_binary
    | expr
      ( LESSTHAN
      | LESSTHANOREQUAL
      | GREATERTHAN
      | GREATERTHANOREQUAL
      )
      expr                              #bool_expr_comp_math
    | expr EQUALS expr                  #bool_expr_equals
    | NOT expr                          #bool_expr_pref
    // maths expressions
    | expr POW expr                     #math_expr_binary
    | expr (TIMES | DIV) expr           #math_expr_binary
    | expr (PLUS | MINUS) expr          #math_expr_binary
    // terminals
    | lst_decl                          #expr_lst_decl
    | literal                           #expr_lit
    | LENOF LPAREN expr RPAREN          #expr_len_of
    | COPYOF LPAREN expr RPAREN         #expr_copy_of
    | IDEN                              #expr_iden
    ;
//
literal
    : INT             #int_lit
    | FLOAT           #float_lit
    | CHAR            #char_lit
    | (TRUE | FALSE)  #bool_lit
    | STRING          #string_lit
    ;
//
lst_decl
    : LBRACK
      expr? (COMMA expr)*
      RBRACK
    ;

//##########
//# Common #
//##########
param_lst
    : LPAREN IDEN (COMMA IDEN)* RPAREN
    | LPAREN RPAREN
    ;
//
arg_lst
    : LPAREN expr (COMMA expr)* RPAREN
    | LPAREN RPAREN
    ;
//
idx_access
    : LBRACK expr RBRACK           #idx_access_one
    | LBRACK expr COLON RBRACK     #idx_access_from
    | LBRACK COLON expr RBRACK     #idx_access_until
    | LBRACK expr COLON expr RBRACK #idx_access_range
    ;
