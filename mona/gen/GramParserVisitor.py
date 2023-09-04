# Generated from /Users/mep/IFI/Research/BlockChainExecVerification/execGrammar/antlr/GramParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GramParser import GramParser
else:
    from GramParser import GramParser

# This class defines a complete generic visitor for a parse tree produced by GramParser.

class GramParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GramParser#program.
    def visitProgram(self, ctx:GramParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#stmt_var_declr.
    def visitStmt_var_declr(self, ctx:GramParser.Stmt_var_declrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#stmt_if_block.
    def visitStmt_if_block(self, ctx:GramParser.Stmt_if_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#stmt_func_decl.
    def visitStmt_func_decl(self, ctx:GramParser.Stmt_func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#stmt_func_call.
    def visitStmt_func_call(self, ctx:GramParser.Stmt_func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#stmt_while.
    def visitStmt_while(self, ctx:GramParser.Stmt_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#stmt_assig.
    def visitStmt_assig(self, ctx:GramParser.Stmt_assigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#stmt_print.
    def visitStmt_print(self, ctx:GramParser.Stmt_printContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#stmt_stmt_block.
    def visitStmt_stmt_block(self, ctx:GramParser.Stmt_stmt_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#assig_trgt_expr.
    def visitAssig_trgt_expr(self, ctx:GramParser.Assig_trgt_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#assig_trgt_iden.
    def visitAssig_trgt_iden(self, ctx:GramParser.Assig_trgt_idenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#var_declr.
    def visitVar_declr(self, ctx:GramParser.Var_declrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#if_block.
    def visitIf_block(self, ctx:GramParser.If_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#if_stmt.
    def visitIf_stmt(self, ctx:GramParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#elseif_stmt.
    def visitElseif_stmt(self, ctx:GramParser.Elseif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#else_stmt.
    def visitElse_stmt(self, ctx:GramParser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#func_decl.
    def visitFunc_decl(self, ctx:GramParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#func_call.
    def visitFunc_call(self, ctx:GramParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#sin_call.
    def visitSin_call(self, ctx:GramParser.Sin_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#floor_call.
    def visitFloor_call(self, ctx:GramParser.Floor_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#round_call.
    def visitRound_call(self, ctx:GramParser.Round_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#ceil_call.
    def visitCeil_call(self, ctx:GramParser.Ceil_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#while.
    def visitWhile(self, ctx:GramParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#assign_access.
    def visitAssign_access(self, ctx:GramParser.Assign_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#assign_iden.
    def visitAssign_iden(self, ctx:GramParser.Assign_idenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#print_base.
    def visitPrint_base(self, ctx:GramParser.Print_baseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#print_nl.
    def visitPrint_nl(self, ctx:GramParser.Print_nlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#stmt_block.
    def visitStmt_block(self, ctx:GramParser.Stmt_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#ret_stmt.
    def visitRet_stmt(self, ctx:GramParser.Ret_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#bool_expr_pref.
    def visitBool_expr_pref(self, ctx:GramParser.Bool_expr_prefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#expr_lst_decl.
    def visitExpr_lst_decl(self, ctx:GramParser.Expr_lst_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#bool_expr_comp_math.
    def visitBool_expr_comp_math(self, ctx:GramParser.Bool_expr_comp_mathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#expr_paren.
    def visitExpr_paren(self, ctx:GramParser.Expr_parenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#bool_expr_binary.
    def visitBool_expr_binary(self, ctx:GramParser.Bool_expr_binaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#expr_iden.
    def visitExpr_iden(self, ctx:GramParser.Expr_idenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#expr_len_of.
    def visitExpr_len_of(self, ctx:GramParser.Expr_len_ofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#expr_lit.
    def visitExpr_lit(self, ctx:GramParser.Expr_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#bool_expr_equals.
    def visitBool_expr_equals(self, ctx:GramParser.Bool_expr_equalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#expr_access.
    def visitExpr_access(self, ctx:GramParser.Expr_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#expr_copy_of.
    def visitExpr_copy_of(self, ctx:GramParser.Expr_copy_ofContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#math_expr_binary.
    def visitMath_expr_binary(self, ctx:GramParser.Math_expr_binaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#expr_func_call.
    def visitExpr_func_call(self, ctx:GramParser.Expr_func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#int_lit.
    def visitInt_lit(self, ctx:GramParser.Int_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#float_lit.
    def visitFloat_lit(self, ctx:GramParser.Float_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#char_lit.
    def visitChar_lit(self, ctx:GramParser.Char_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#bool_lit.
    def visitBool_lit(self, ctx:GramParser.Bool_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#string_lit.
    def visitString_lit(self, ctx:GramParser.String_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#lst_decl.
    def visitLst_decl(self, ctx:GramParser.Lst_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#param_lst.
    def visitParam_lst(self, ctx:GramParser.Param_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#arg_lst.
    def visitArg_lst(self, ctx:GramParser.Arg_lstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#idx_access_one.
    def visitIdx_access_one(self, ctx:GramParser.Idx_access_oneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#idx_access_from.
    def visitIdx_access_from(self, ctx:GramParser.Idx_access_fromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#idx_access_until.
    def visitIdx_access_until(self, ctx:GramParser.Idx_access_untilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramParser#idx_access_range.
    def visitIdx_access_range(self, ctx:GramParser.Idx_access_rangeContext):
        return self.visitChildren(ctx)



del GramParser