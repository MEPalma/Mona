from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GramParser import GramParser
else:
    from GramParser import GramParser

# This class defines a complete listener for a parse tree produced by GramParser.
class GramParserListener(ParseTreeListener):

    # Enter a parse tree produced by GramParser#program.
    def enterProgram(self, ctx:GramParser.ProgramContext):
        pass

    # Exit a parse tree produced by GramParser#program.
    def exitProgram(self, ctx:GramParser.ProgramContext):
        pass


    # Enter a parse tree produced by GramParser#stmt_var_declr.
    def enterStmt_var_declr(self, ctx:GramParser.Stmt_var_declrContext):
        pass

    # Exit a parse tree produced by GramParser#stmt_var_declr.
    def exitStmt_var_declr(self, ctx:GramParser.Stmt_var_declrContext):
        pass


    # Enter a parse tree produced by GramParser#stmt_if_block.
    def enterStmt_if_block(self, ctx:GramParser.Stmt_if_blockContext):
        pass

    # Exit a parse tree produced by GramParser#stmt_if_block.
    def exitStmt_if_block(self, ctx:GramParser.Stmt_if_blockContext):
        pass


    # Enter a parse tree produced by GramParser#stmt_func_decl.
    def enterStmt_func_decl(self, ctx:GramParser.Stmt_func_declContext):
        pass

    # Exit a parse tree produced by GramParser#stmt_func_decl.
    def exitStmt_func_decl(self, ctx:GramParser.Stmt_func_declContext):
        pass


    # Enter a parse tree produced by GramParser#stmt_func_call.
    def enterStmt_func_call(self, ctx:GramParser.Stmt_func_callContext):
        pass

    # Exit a parse tree produced by GramParser#stmt_func_call.
    def exitStmt_func_call(self, ctx:GramParser.Stmt_func_callContext):
        pass


    # Enter a parse tree produced by GramParser#stmt_while.
    def enterStmt_while(self, ctx:GramParser.Stmt_whileContext):
        pass

    # Exit a parse tree produced by GramParser#stmt_while.
    def exitStmt_while(self, ctx:GramParser.Stmt_whileContext):
        pass


    # Enter a parse tree produced by GramParser#stmt_assig.
    def enterStmt_assig(self, ctx:GramParser.Stmt_assigContext):
        pass

    # Exit a parse tree produced by GramParser#stmt_assig.
    def exitStmt_assig(self, ctx:GramParser.Stmt_assigContext):
        pass


    # Enter a parse tree produced by GramParser#stmt_print.
    def enterStmt_print(self, ctx:GramParser.Stmt_printContext):
        pass

    # Exit a parse tree produced by GramParser#stmt_print.
    def exitStmt_print(self, ctx:GramParser.Stmt_printContext):
        pass


    # Enter a parse tree produced by GramParser#stmt_stmt_block.
    def enterStmt_stmt_block(self, ctx:GramParser.Stmt_stmt_blockContext):
        pass

    # Exit a parse tree produced by GramParser#stmt_stmt_block.
    def exitStmt_stmt_block(self, ctx:GramParser.Stmt_stmt_blockContext):
        pass


    # Enter a parse tree produced by GramParser#assig_trgt_expr.
    def enterAssig_trgt_expr(self, ctx:GramParser.Assig_trgt_exprContext):
        pass

    # Exit a parse tree produced by GramParser#assig_trgt_expr.
    def exitAssig_trgt_expr(self, ctx:GramParser.Assig_trgt_exprContext):
        pass


    # Enter a parse tree produced by GramParser#assig_trgt_iden.
    def enterAssig_trgt_iden(self, ctx:GramParser.Assig_trgt_idenContext):
        pass

    # Exit a parse tree produced by GramParser#assig_trgt_iden.
    def exitAssig_trgt_iden(self, ctx:GramParser.Assig_trgt_idenContext):
        pass


    # Enter a parse tree produced by GramParser#var_declr.
    def enterVar_declr(self, ctx:GramParser.Var_declrContext):
        pass

    # Exit a parse tree produced by GramParser#var_declr.
    def exitVar_declr(self, ctx:GramParser.Var_declrContext):
        pass


    # Enter a parse tree produced by GramParser#if_block.
    def enterIf_block(self, ctx:GramParser.If_blockContext):
        pass

    # Exit a parse tree produced by GramParser#if_block.
    def exitIf_block(self, ctx:GramParser.If_blockContext):
        pass


    # Enter a parse tree produced by GramParser#if_stmt.
    def enterIf_stmt(self, ctx:GramParser.If_stmtContext):
        pass

    # Exit a parse tree produced by GramParser#if_stmt.
    def exitIf_stmt(self, ctx:GramParser.If_stmtContext):
        pass


    # Enter a parse tree produced by GramParser#elseif_stmt.
    def enterElseif_stmt(self, ctx:GramParser.Elseif_stmtContext):
        pass

    # Exit a parse tree produced by GramParser#elseif_stmt.
    def exitElseif_stmt(self, ctx:GramParser.Elseif_stmtContext):
        pass


    # Enter a parse tree produced by GramParser#else_stmt.
    def enterElse_stmt(self, ctx:GramParser.Else_stmtContext):
        pass

    # Exit a parse tree produced by GramParser#else_stmt.
    def exitElse_stmt(self, ctx:GramParser.Else_stmtContext):
        pass


    # Enter a parse tree produced by GramParser#func_decl.
    def enterFunc_decl(self, ctx:GramParser.Func_declContext):
        pass

    # Exit a parse tree produced by GramParser#func_decl.
    def exitFunc_decl(self, ctx:GramParser.Func_declContext):
        pass


    # Enter a parse tree produced by GramParser#func_call.
    def enterFunc_call(self, ctx:GramParser.Func_callContext):
        pass

    # Exit a parse tree produced by GramParser#func_call.
    def exitFunc_call(self, ctx:GramParser.Func_callContext):
        pass


    # Enter a parse tree produced by GramParser#sin_call.
    def enterSin_call(self, ctx:GramParser.Sin_callContext):
        pass

    # Exit a parse tree produced by GramParser#sin_call.
    def exitSin_call(self, ctx:GramParser.Sin_callContext):
        pass


    # Enter a parse tree produced by GramParser#floor_call.
    def enterFloor_call(self, ctx:GramParser.Floor_callContext):
        pass

    # Exit a parse tree produced by GramParser#floor_call.
    def exitFloor_call(self, ctx:GramParser.Floor_callContext):
        pass


    # Enter a parse tree produced by GramParser#round_call.
    def enterRound_call(self, ctx:GramParser.Round_callContext):
        pass

    # Exit a parse tree produced by GramParser#round_call.
    def exitRound_call(self, ctx:GramParser.Round_callContext):
        pass


    # Enter a parse tree produced by GramParser#ceil_call.
    def enterCeil_call(self, ctx:GramParser.Ceil_callContext):
        pass

    # Exit a parse tree produced by GramParser#ceil_call.
    def exitCeil_call(self, ctx:GramParser.Ceil_callContext):
        pass


    # Enter a parse tree produced by GramParser#while.
    def enterWhile(self, ctx:GramParser.WhileContext):
        pass

    # Exit a parse tree produced by GramParser#while.
    def exitWhile(self, ctx:GramParser.WhileContext):
        pass


    # Enter a parse tree produced by GramParser#assign_access.
    def enterAssign_access(self, ctx:GramParser.Assign_accessContext):
        pass

    # Exit a parse tree produced by GramParser#assign_access.
    def exitAssign_access(self, ctx:GramParser.Assign_accessContext):
        pass


    # Enter a parse tree produced by GramParser#assign_iden.
    def enterAssign_iden(self, ctx:GramParser.Assign_idenContext):
        pass

    # Exit a parse tree produced by GramParser#assign_iden.
    def exitAssign_iden(self, ctx:GramParser.Assign_idenContext):
        pass


    # Enter a parse tree produced by GramParser#print_base.
    def enterPrint_base(self, ctx:GramParser.Print_baseContext):
        pass

    # Exit a parse tree produced by GramParser#print_base.
    def exitPrint_base(self, ctx:GramParser.Print_baseContext):
        pass


    # Enter a parse tree produced by GramParser#print_nl.
    def enterPrint_nl(self, ctx:GramParser.Print_nlContext):
        pass

    # Exit a parse tree produced by GramParser#print_nl.
    def exitPrint_nl(self, ctx:GramParser.Print_nlContext):
        pass


    # Enter a parse tree produced by GramParser#stmt_block.
    def enterStmt_block(self, ctx:GramParser.Stmt_blockContext):
        pass

    # Exit a parse tree produced by GramParser#stmt_block.
    def exitStmt_block(self, ctx:GramParser.Stmt_blockContext):
        pass


    # Enter a parse tree produced by GramParser#ret_stmt.
    def enterRet_stmt(self, ctx:GramParser.Ret_stmtContext):
        pass

    # Exit a parse tree produced by GramParser#ret_stmt.
    def exitRet_stmt(self, ctx:GramParser.Ret_stmtContext):
        pass


    # Enter a parse tree produced by GramParser#bool_expr_pref.
    def enterBool_expr_pref(self, ctx:GramParser.Bool_expr_prefContext):
        pass

    # Exit a parse tree produced by GramParser#bool_expr_pref.
    def exitBool_expr_pref(self, ctx:GramParser.Bool_expr_prefContext):
        pass


    # Enter a parse tree produced by GramParser#expr_lst_decl.
    def enterExpr_lst_decl(self, ctx:GramParser.Expr_lst_declContext):
        pass

    # Exit a parse tree produced by GramParser#expr_lst_decl.
    def exitExpr_lst_decl(self, ctx:GramParser.Expr_lst_declContext):
        pass


    # Enter a parse tree produced by GramParser#bool_expr_comp_math.
    def enterBool_expr_comp_math(self, ctx:GramParser.Bool_expr_comp_mathContext):
        pass

    # Exit a parse tree produced by GramParser#bool_expr_comp_math.
    def exitBool_expr_comp_math(self, ctx:GramParser.Bool_expr_comp_mathContext):
        pass


    # Enter a parse tree produced by GramParser#expr_paren.
    def enterExpr_paren(self, ctx:GramParser.Expr_parenContext):
        pass

    # Exit a parse tree produced by GramParser#expr_paren.
    def exitExpr_paren(self, ctx:GramParser.Expr_parenContext):
        pass


    # Enter a parse tree produced by GramParser#bool_expr_binary.
    def enterBool_expr_binary(self, ctx:GramParser.Bool_expr_binaryContext):
        pass

    # Exit a parse tree produced by GramParser#bool_expr_binary.
    def exitBool_expr_binary(self, ctx:GramParser.Bool_expr_binaryContext):
        pass


    # Enter a parse tree produced by GramParser#expr_iden.
    def enterExpr_iden(self, ctx:GramParser.Expr_idenContext):
        pass

    # Exit a parse tree produced by GramParser#expr_iden.
    def exitExpr_iden(self, ctx:GramParser.Expr_idenContext):
        pass


    # Enter a parse tree produced by GramParser#expr_len_of.
    def enterExpr_len_of(self, ctx:GramParser.Expr_len_ofContext):
        pass

    # Exit a parse tree produced by GramParser#expr_len_of.
    def exitExpr_len_of(self, ctx:GramParser.Expr_len_ofContext):
        pass


    # Enter a parse tree produced by GramParser#expr_lit.
    def enterExpr_lit(self, ctx:GramParser.Expr_litContext):
        pass

    # Exit a parse tree produced by GramParser#expr_lit.
    def exitExpr_lit(self, ctx:GramParser.Expr_litContext):
        pass


    # Enter a parse tree produced by GramParser#bool_expr_equals.
    def enterBool_expr_equals(self, ctx:GramParser.Bool_expr_equalsContext):
        pass

    # Exit a parse tree produced by GramParser#bool_expr_equals.
    def exitBool_expr_equals(self, ctx:GramParser.Bool_expr_equalsContext):
        pass


    # Enter a parse tree produced by GramParser#expr_access.
    def enterExpr_access(self, ctx:GramParser.Expr_accessContext):
        pass

    # Exit a parse tree produced by GramParser#expr_access.
    def exitExpr_access(self, ctx:GramParser.Expr_accessContext):
        pass


    # Enter a parse tree produced by GramParser#expr_copy_of.
    def enterExpr_copy_of(self, ctx:GramParser.Expr_copy_ofContext):
        pass

    # Exit a parse tree produced by GramParser#expr_copy_of.
    def exitExpr_copy_of(self, ctx:GramParser.Expr_copy_ofContext):
        pass


    # Enter a parse tree produced by GramParser#math_expr_binary.
    def enterMath_expr_binary(self, ctx:GramParser.Math_expr_binaryContext):
        pass

    # Exit a parse tree produced by GramParser#math_expr_binary.
    def exitMath_expr_binary(self, ctx:GramParser.Math_expr_binaryContext):
        pass


    # Enter a parse tree produced by GramParser#expr_func_call.
    def enterExpr_func_call(self, ctx:GramParser.Expr_func_callContext):
        pass

    # Exit a parse tree produced by GramParser#expr_func_call.
    def exitExpr_func_call(self, ctx:GramParser.Expr_func_callContext):
        pass


    # Enter a parse tree produced by GramParser#int_lit.
    def enterInt_lit(self, ctx:GramParser.Int_litContext):
        pass

    # Exit a parse tree produced by GramParser#int_lit.
    def exitInt_lit(self, ctx:GramParser.Int_litContext):
        pass


    # Enter a parse tree produced by GramParser#float_lit.
    def enterFloat_lit(self, ctx:GramParser.Float_litContext):
        pass

    # Exit a parse tree produced by GramParser#float_lit.
    def exitFloat_lit(self, ctx:GramParser.Float_litContext):
        pass


    # Enter a parse tree produced by GramParser#char_lit.
    def enterChar_lit(self, ctx:GramParser.Char_litContext):
        pass

    # Exit a parse tree produced by GramParser#char_lit.
    def exitChar_lit(self, ctx:GramParser.Char_litContext):
        pass


    # Enter a parse tree produced by GramParser#bool_lit.
    def enterBool_lit(self, ctx:GramParser.Bool_litContext):
        pass

    # Exit a parse tree produced by GramParser#bool_lit.
    def exitBool_lit(self, ctx:GramParser.Bool_litContext):
        pass


    # Enter a parse tree produced by GramParser#string_lit.
    def enterString_lit(self, ctx:GramParser.String_litContext):
        pass

    # Exit a parse tree produced by GramParser#string_lit.
    def exitString_lit(self, ctx:GramParser.String_litContext):
        pass


    # Enter a parse tree produced by GramParser#lst_decl.
    def enterLst_decl(self, ctx:GramParser.Lst_declContext):
        pass

    # Exit a parse tree produced by GramParser#lst_decl.
    def exitLst_decl(self, ctx:GramParser.Lst_declContext):
        pass


    # Enter a parse tree produced by GramParser#param_lst.
    def enterParam_lst(self, ctx:GramParser.Param_lstContext):
        pass

    # Exit a parse tree produced by GramParser#param_lst.
    def exitParam_lst(self, ctx:GramParser.Param_lstContext):
        pass


    # Enter a parse tree produced by GramParser#arg_lst.
    def enterArg_lst(self, ctx:GramParser.Arg_lstContext):
        pass

    # Exit a parse tree produced by GramParser#arg_lst.
    def exitArg_lst(self, ctx:GramParser.Arg_lstContext):
        pass


    # Enter a parse tree produced by GramParser#idx_access_one.
    def enterIdx_access_one(self, ctx:GramParser.Idx_access_oneContext):
        pass

    # Exit a parse tree produced by GramParser#idx_access_one.
    def exitIdx_access_one(self, ctx:GramParser.Idx_access_oneContext):
        pass


    # Enter a parse tree produced by GramParser#idx_access_from.
    def enterIdx_access_from(self, ctx:GramParser.Idx_access_fromContext):
        pass

    # Exit a parse tree produced by GramParser#idx_access_from.
    def exitIdx_access_from(self, ctx:GramParser.Idx_access_fromContext):
        pass


    # Enter a parse tree produced by GramParser#idx_access_until.
    def enterIdx_access_until(self, ctx:GramParser.Idx_access_untilContext):
        pass

    # Exit a parse tree produced by GramParser#idx_access_until.
    def exitIdx_access_until(self, ctx:GramParser.Idx_access_untilContext):
        pass


    # Enter a parse tree produced by GramParser#idx_access_range.
    def enterIdx_access_range(self, ctx:GramParser.Idx_access_rangeContext):
        pass

    # Exit a parse tree produced by GramParser#idx_access_range.
    def exitIdx_access_range(self, ctx:GramParser.Idx_access_rangeContext):
        pass



del GramParser
