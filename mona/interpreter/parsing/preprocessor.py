from typing import Optional, Final

from mona.interpreter.component.arg_lst import ArgumentList
from mona.interpreter.component.component import Component
from mona.interpreter.component.else_stmt import ElseStmt
from mona.interpreter.component.elseif_stmt import ElseIfStmt
from mona.interpreter.component.func_call import FunctionCall, FunctionCallBase, SinCall
from mona.interpreter.component.func_decl import FunctionDeclaration
from mona.interpreter.component.while_stmt import While
from mona.interpreter.component.func_call import FunctionCall, FunctionCallBase, SinCall, FloorCall, RoundCall, CeilCall
from mona.interpreter.component.idx_access import (
    IdxAccessOne,
    IdxAccessFrom,
    IdxAccessUntil,
    IdxAccessRange,
    IdxAccess,
)
from mona.interpreter.component.if_block import IfBlock
from mona.interpreter.component.if_stmt import IfStmt
from mona.interpreter.component.literal import (
    LiteralInt,
    LiteralFloat,
    LiteralChar,
    LiteralBool,
    Literal,
    LiteralString,
)
from mona.interpreter.component.lst_decl import ListDeclaration
from mona.interpreter.component.math_expr import (
    MathExpr,
    MathExprBinary,
    MathBinaryOperator,
)
from mona.interpreter.component.param_lst import ParameterList
from mona.interpreter.component.ret_stmt import Return
from mona.interpreter.component.stmt_block import StmtBlock
from mona.interpreter.component_store import ComponentStore
from mona.gen.GramLexer import GramLexer
from mona.gen.GramParser import GramParser
from mona.gen.GramParserVisitor import GramParserVisitor
from antlr4.tree.Tree import ParseTree, TerminalNodeImpl

from mona.interpreter.component.assig import AssigIden, AssigAccess, Assig
from mona.interpreter.component.assig_trgt import AssigTrgt, AssigTrgtExpr, AssigTrgtIden
from mona.interpreter.component.bool_expr import (
    BoolExprPrefNot,
    BoolExpr,
    BoolExprPref,
    BoolExprBinary,
    BoolExprBinaryAnd,
    BoolExprBinaryOr,
    BoolExprComparisonMath,
    BoolExprEquals,
    ComparisonOperator,
)
from mona.interpreter.component.print import Print, PrintLn
from mona.interpreter.component.expr_type import Expr
from mona.interpreter.component.expr import (
    ExprIden,
    ExprAccess,
    ExprCopyOf,
    ExprLenOf,
)
from mona.interpreter.component.program import Program
from mona.interpreter.component.var_declr import VarDeclr
from mona.interpreter.utils.antlr4utils import Antlr4Utils


class Preprocessor(GramParserVisitor):
    def __init__(self):
        super(Preprocessor, self).__init__()
        self.comp_store: Final[ComponentStore] = ComponentStore()

    def _register(self, cmp):
        self.comp_store.register(cmp)
        return cmp

    @staticmethod
    def _iden_text(parse_tree: ParseTree) -> Optional[str]:
        iden_prod: Optional[TerminalNodeImpl] = Antlr4Utils.is_term(
            parse_tree, GramLexer.IDEN
        )
        if iden_prod:
            return iden_prod.symbol.text
        raise ValueError("Could not extract text")

    ###########
    # program #
    ###########
    def visitProgram(self, ctx: GramParser.ProgramContext) -> Program:
        stmts: list[Component] = list()
        for child in ctx.children:
            cmp = self.visit(child)
            if isinstance(cmp, Component):
                stmts.append(cmp)
        cmp = Program(seq_id=self.comp_store.next_seq_id, stmts=stmts)
        return self._register(cmp)

    ########
    # stmt #
    ########

    def visitStmt_var_declr(self, ctx: GramParser.Stmt_var_declrContext) -> VarDeclr:
        return self.visitVar_declr(ctx.var_declr())

    def visitStmt_if_block(self, ctx: GramParser.Stmt_if_blockContext) -> IfBlock:
        return self.visitIf_block(ctx.if_block())

    def visitStmt_func_decl(
        self, ctx: GramParser.Stmt_func_declContext
    ) -> FunctionDeclaration:
        return self.visitFunc_decl(ctx.func_decl())

    def visitStmt_func_call(
        self, ctx: GramParser.Stmt_func_callContext
    ) -> FunctionCall:
        return self.visitFunc_call(ctx.func_call_expr())

    def visitStmt_assig(self, ctx: GramParser.Stmt_assigContext) -> Assig:
        return self.visit(ctx.assig())

    def visitStmt_print(self, ctx: GramParser.Stmt_printContext) -> Print:
        return self.visit(ctx.print_())

    def visitStmt_stmt_block(self, ctx: GramParser.Stmt_stmt_blockContext) -> StmtBlock:
        return self.visitStmt_block(ctx.stmt_block())

    def visitWhile(self, ctx:GramParser.WhileContext) -> While:
        bool_expr: BoolExpr = self.visit(ctx.expr())
        stmt_block: StmtBlock = self.visit(ctx.stmt_block())
        cmp = While(
            seq_id=self.comp_store.next_seq_id,
            bool_expr=bool_expr,
            stmt_block=stmt_block,
        )
        return self._register(cmp)

    def visitStmt_while(self, ctx:GramParser.Stmt_whileContext) -> While:
        return self.visitWhile(ctx.while_())

    ########
    # expr #
    ########
    def visitExpr_paren(self, ctx: GramParser.Expr_parenContext) -> Expr:
        return self.visit(ctx.expr())

    def visitExpr_iden(self, ctx: GramParser.Expr_idenContext) -> ExprIden:
        iden: str = self._iden_text(ctx.IDEN())
        cmp = ExprIden(seq_id=self.comp_store.next_seq_id, iden=iden)
        return self._register(cmp)

    def visitExpr_lit(self, ctx: GramParser.Expr_litContext) -> Literal:
        return self.visit(ctx.literal())

    def visitExpr_lst_decl(
        self, ctx: GramParser.Expr_lst_declContext
    ) -> ListDeclaration:
        return self.visitLst_decl(ctx.lst_decl())

    def visitExpr_func_call(self, ctx:GramParser.Expr_func_callContext) -> FunctionCall:
        return self.visit(ctx.children[0])

    #########
    # print #
    #########
    def visitPrint_base(self, ctx: GramParser.Print_baseContext) -> Print:
        arg_lst: ArgumentList = self.visitArg_lst(ctx.arg_lst())
        cmp = Print(seq_id=self.comp_store.next_seq_id, arg_lst=arg_lst)
        return self._register(cmp)

    def visitPrint_nl(self, ctx: GramParser.Print_nlContext) -> PrintLn:
        arg_lst: ArgumentList = self.visitArg_lst(ctx.arg_lst())
        cmp = PrintLn(seq_id=self.comp_store.next_seq_id, arg_lst=arg_lst)
        return self._register(cmp)

    ############
    # var_decl #
    ############
    def visitVar_declr(self, ctx: GramParser.Var_declrContext) -> VarDeclr:
        iden: str = self._iden_text(ctx.IDEN())
        assig_trgt: AssigTrgt = self.visit(ctx.assig_trgt())
        cmp = VarDeclr(
            seq_id=self.comp_store.next_seq_id, iden=iden, assig_trgt=assig_trgt
        )
        return self._register(cmp)

    def visitAssign_iden(self, ctx: GramParser.Assign_idenContext) -> AssigIden:
        iden: str = self._iden_text(ctx.IDEN())
        trgt: AssigTrgt = self.visit(ctx.assig_trgt())
        cmp = AssigIden(
            seq_id=self.comp_store.next_seq_id,
            iden=iden,
            trgt=trgt,
        )
        return self._register(cmp)

    def visitAssign_access(self, ctx: GramParser.Assign_accessContext) -> AssigAccess:
        iden: str = self._iden_text(ctx.IDEN())
        expr: Expr = self.visit(ctx.expr())
        trgt: AssigTrgt = self.visit(ctx.assig_trgt())
        cmp = AssigAccess(
            seq_id=self.comp_store.next_seq_id,
            iden=iden,
            idx=expr,
            trgt=trgt,
        )
        return self._register(cmp)

    def visitAssig_trgt_expr(
        self, ctx: GramParser.Assig_trgt_exprContext
    ) -> AssigTrgtExpr:
        expr: Expr = self.visit(ctx.expr())
        cmp = AssigTrgtExpr(seq_id=self.comp_store.next_seq_id, expr=expr)
        return self._register(cmp)

    def visitAssig_trgt_iden(
        self, ctx: GramParser.Assig_trgt_idenContext
    ) -> AssigTrgtIden:
        iden: str = self._iden_text(ctx.IDEN())
        cmp = AssigTrgtIden(seq_id=self.comp_store.next_seq_id, iden=iden)
        return self._register(cmp)

    def visitExpr_copy_of(self, ctx: GramParser.Expr_copy_ofContext) -> ExprCopyOf:
        expr: Expr = self.visit(ctx.expr())
        cmp = ExprCopyOf(seq_id=self.comp_store.next_seq_id, expr=expr)
        return self._register(cmp)

    def visitExpr_len_of(self, ctx: GramParser.Expr_len_ofContext) -> ExprLenOf:
        expr: Expr = self.visit(ctx.expr())
        cmp = ExprLenOf(seq_id=self.comp_store.next_seq_id, expr=expr)
        return self._register(cmp)

    #############
    # bool_expr #
    #############

    def visitBool_expr_pref(
        self, ctx: GramParser.Bool_expr_prefContext
    ) -> BoolExprPref:
        c0_idx: int = ctx.children[0].symbol.type
        bool_expr: BoolExpr = self.visit(ctx.bool_expr())
        if c0_idx == GramLexer.NOT:
            cmp = BoolExprPrefNot(seq_id=self.comp_store.next_seq_id, expr=bool_expr)
            return self._register(cmp)
        raise RuntimeError(f"Unknown boolean operator in '{ctx.getText()}'.")

    def visitBool_expr_binary(
        self, ctx: GramParser.Bool_expr_binaryContext
    ) -> BoolExprBinary:
        bool_op_idx: int = ctx.children[1].symbol.type
        left: BoolExpr = self.visit(ctx.children[0])
        right: BoolExpr = self.visit(ctx.children[2])
        if bool_op_idx == GramLexer.AND:
            cmp = BoolExprBinaryAnd(
                seq_id=self.comp_store.next_seq_id, left=left, right=right
            )
        elif bool_op_idx == GramLexer.OR:
            cmp = BoolExprBinaryOr(
                seq_id=self.comp_store.next_seq_id, left=left, right=right
            )
        else:
            raise RuntimeError(f"Unknown boolean operator in '{ctx.getText()}'.")
        return self._register(cmp)

    def visitBool_expr_equals(
        self, ctx: GramParser.Bool_expr_equalsContext
    ) -> BoolExprEquals:
        left: Expr = self.visit(ctx.children[0])
        right: Expr = self.visit(ctx.children[2])
        cmp = BoolExprEquals(
            seq_id=self.comp_store.next_seq_id,
            left=left,
            right=right,
        )
        return self._register(cmp)

    def visitBool_expr_comp_math(
        self, ctx: GramParser.Bool_expr_comp_mathContext
    ) -> BoolExprComparisonMath:
        operator = ComparisonOperator(ctx.children[1].symbol.type)
        left: MathExpr = self.visit(ctx.children[0])
        right: MathExpr = self.visit(ctx.children[2])
        cmp = BoolExprComparisonMath(
            seq_id=self.comp_store.next_seq_id,
            operator=operator,
            left=left,
            right=right,
        )
        return self._register(cmp)

    ###########
    # literal #
    ###########
    def visitInt_lit(self, ctx: GramParser.Int_litContext) -> LiteralInt:
        integer = int(ctx.INT().getText())
        return LiteralInt(seq_id=self.comp_store.next_seq_id, integer=integer)

    def visitFloat_lit(self, ctx: GramParser.Float_litContext) -> LiteralFloat:
        float_num = float(ctx.FLOAT().getText())
        cmp = LiteralFloat(seq_id=self.comp_store.next_seq_id, float_num=float_num)
        return self._register(cmp)

    def visitChar_lit(self, ctx: GramParser.Char_litContext) -> LiteralChar:
        char = ctx.getText()[1:-1]
        cmp = LiteralChar(seq_id=self.comp_store.next_seq_id, char=char)
        return self._register(cmp)

    def visitBool_lit(self, ctx: GramParser.Bool_litContext) -> LiteralBool:
        boolean = ctx.children[0].symbol.type == GramLexer.TRUE
        cmp = LiteralBool(seq_id=self.comp_store.next_seq_id, boolean=boolean)
        return self._register(cmp)

    def visitString_lit(self, ctx: GramParser.String_litContext) -> LiteralString:
        string = ctx.STRING().getText()[1:-1]
        string = bytes(string, "utf-8").decode("unicode_escape")
        cmp = LiteralString(seq_id=self.comp_store.next_seq_id, string=string)
        return self._register(cmp)

    #############
    # param_lst #
    #############
    def visitParam_lst(self, ctx: GramParser.Param_lstContext) -> ParameterList:
        idens: list[str] = list()
        for child in ctx.children:
            is_iden = Antlr4Utils.is_term(child, token_type=GramLexer.IDEN)
            if is_iden is not None:
                iden_text: str = self._iden_text(is_iden)
                idens.append(iden_text)
        cmp = ParameterList(seq_id=self.comp_store.next_seq_id, idens=idens)
        return self._register(cmp)

    ###########
    # arg_lst #
    ###########
    def visitArg_lst(self, ctx: GramParser.Arg_lstContext) -> ArgumentList:
        exprs: list[Expr] = list()
        for child in ctx.children:
            cmp = self.visit(child)
            if isinstance(cmp, Expr):
                exprs.append(cmp)
        cmp = ArgumentList(seq_id=self.comp_store.next_seq_id, exprs=exprs)
        return self._register(cmp)

    ############
    # lst_decl #
    ############
    def visitLst_decl(self, ctx: GramParser.Lst_declContext) -> ListDeclaration:
        exprs: list[Expr] = list()
        for child in ctx.children:
            cmp = self.visit(child)
            if isinstance(cmp, Expr):
                exprs.append(cmp)
        cmp = ListDeclaration(seq_id=self.comp_store.next_seq_id, exprs=exprs)
        return self._register(cmp)

    ############
    # ret_stmt #
    ############
    def visitRet_stmt(self, ctx: GramParser.Ret_stmtContext) -> Return:
        expr = None
        if len(ctx.children) > 2:
            expr = self.visit(ctx.expr())
        cmp = Return(seq_id=self.comp_store.next_seq_id, expr=expr)
        return self._register(cmp)

    ##############
    # stmt_block #
    ##############
    def visitStmt_block(self, ctx: GramParser.Stmt_blockContext):
        stmts: list[Component] = list()
        for child in ctx.children:
            cmp = self.visit(child)
            if isinstance(cmp, Component):
                stmts.append(cmp)
        cmp = StmtBlock(seq_id=self.comp_store.next_seq_id, stmts=stmts)
        return self._register(cmp)

    #############
    # func_decl #
    #############
    def visitFunc_decl(self, ctx: GramParser.Func_declContext) -> FunctionDeclaration:
        iden: str = self._iden_text(ctx.IDEN())
        param_lst: ParameterList = self.visit(ctx.param_lst())
        stmt_block: StmtBlock = self.visit(ctx.stmt_block())
        cmp = FunctionDeclaration(
            seq_id=self.comp_store.next_seq_id,
            iden=iden,
            param_lst=param_lst,
            stmt_block=stmt_block,
        )
        return self._register(cmp)

    #############
    # func_call #
    #############
    def visitFunc_call(self, ctx: GramParser.Func_callContext) -> FunctionCallBase:
        iden: str = self._iden_text(ctx.IDEN())
        arg_lst: ArgumentList = self.visit(ctx.arg_lst())
        cmp = FunctionCallBase(
            seq_id=self.comp_store.next_seq_id, iden=iden, arg_lst=arg_lst
        )
        return self._register(cmp)

    def visitSin_call(self, ctx:GramParser.Sin_callContext) -> SinCall:
        arg_lst: ArgumentList = self.visit(ctx.arg_lst())
        cmp = SinCall(
            seq_id=self.comp_store.next_seq_id, iden=ctx.SIN().getText(), arg_lst=arg_lst
        )
        return self._register(cmp)

    def visitFloor_call(self, ctx:GramParser.Floor_callContext) -> FloorCall:
        arg_lst: ArgumentList = self.visit(ctx.arg_lst())
        cmp = FloorCall(
            seq_id=self.comp_store.next_seq_id, iden=ctx.FLOORINTOF().getText(), arg_lst=arg_lst
        )
        return self._register(cmp)

    def visitRound_call(self, ctx:GramParser.Round_callContext) -> RoundCall:
        arg_lst: ArgumentList = self.visit(ctx.arg_lst())
        cmp = RoundCall(
            seq_id=self.comp_store.next_seq_id, iden=ctx.ROUNDINTOF().getText(), arg_lst=arg_lst
        )
        return self._register(cmp)

    def visitCeil_call(self, ctx:GramParser.Ceil_callContext) -> CeilCall:
        arg_lst: ArgumentList = self.visit(ctx.arg_lst())
        cmp = CeilCall(
            seq_id=self.comp_store.next_seq_id, iden=ctx.CEILINTOF().getText(), arg_lst=arg_lst
        )
        return self._register(cmp)


    ###########
    # if_stmt #
    ###########
    def visitIf_stmt(self, ctx: GramParser.If_stmtContext) -> IfStmt:
        bool_expr: BoolExpr = self.visit(ctx.expr())
        stmt_block: StmtBlock = self.visit(ctx.stmt_block())
        cmp = IfStmt(
            seq_id=self.comp_store.next_seq_id,
            bool_expr=bool_expr,
            stmt_block=stmt_block,
        )
        return self._register(cmp)

    ###############
    # elseif_stmt #
    ###############
    def visitElseif_stmt(self, ctx: GramParser.Elseif_stmtContext) -> ElseIfStmt:
        bool_expr: BoolExpr = self.visit(ctx.expr())
        stmt_block: StmtBlock = self.visit(ctx.stmt_block())
        cmp = ElseIfStmt(
            seq_id=self.comp_store.next_seq_id,
            bool_expr=bool_expr,
            stmt_block=stmt_block,
        )
        return self._register(cmp)

    #############
    # else_stmt #
    #############
    def visitElse_stmt(self, ctx: GramParser.Else_stmtContext) -> ElseStmt:
        stmt_block: StmtBlock = self.visit(ctx.stmt_block())
        cmp = ElseStmt(seq_id=self.comp_store.next_seq_id, stmt_block=stmt_block)
        return self._register(cmp)

    ############
    # if_block #
    ############
    def visitIf_block(self, ctx: GramParser.If_blockContext) -> IfBlock:
        if_stmt: IfStmt = self.visit(ctx.if_stmt())

        elseifs: list[ElseIfStmt] = list()
        else_stmt: Optional[ElseStmt] = None
        for child in ctx.children[1:]:
            cmp = self.visit(child)
            if isinstance(cmp, ElseIfStmt):
                elseifs.append(cmp)
            elif isinstance(cmp, ElseStmt):
                assert else_stmt is None
                else_stmt = cmp

        cmp = IfBlock(
            seq_id=self.comp_store.next_seq_id,
            if_stmt=if_stmt,
            elseifs=elseifs,
            else_stmt=else_stmt,
        )
        return self._register(cmp)

    ####################
    # math_expr_binary #
    ####################
    def visitMath_expr_binary(
        self, ctx: GramParser.Math_expr_binaryContext
    ) -> MathExprBinary:
        operator = MathBinaryOperator(ctx.children[1].symbol.type)
        left: MathExpr = self.visit(ctx.children[0])
        right: MathExpr = self.visit(ctx.children[2])
        cmp = MathExprBinary(
            seq_id=self.comp_store.next_seq_id,
            operator=operator,
            left=left,
            right=right,
        )
        return self._register(cmp)

    def visitIdx_access_one(
        self, ctx: GramParser.Idx_access_oneContext
    ) -> IdxAccessOne:
        expr: Expr = self.visit(ctx.expr())
        cmp = IdxAccessOne(seq_id=self.comp_store.next_seq_id, idx=expr)
        return self._register(cmp)

    def visitIdx_access_from(
        self, ctx: GramParser.Idx_access_fromContext
    ) -> IdxAccessFrom:
        expr: Expr = self.visit(ctx.expr())
        cmp = IdxAccessFrom(seq_id=self.comp_store.next_seq_id, from_idx=expr)
        return self._register(cmp)

    def visitIdx_access_until(
        self, ctx: GramParser.Idx_access_untilContext
    ) -> IdxAccessUntil:
        expr: Expr = self.visit(ctx.children[3])
        cmp = IdxAccessUntil(seq_id=self.comp_store.next_seq_id, until_idx=expr)
        return self._register(cmp)

    def visitIdx_access_range(
        self, ctx: GramParser.Idx_access_rangeContext
    ) -> IdxAccessRange:
        from_expr: Expr = self.visit(ctx.children[1])
        until_expr: Expr = self.visit(ctx.children[3])
        cmp = IdxAccessRange(
            seq_id=self.comp_store.next_seq_id, from_idx=from_expr, until_idx=until_expr
        )
        return self._register(cmp)

    def visitExpr_access(self, ctx: GramParser.Expr_accessContext) -> ExprAccess:
        source: Expr = self.visit(ctx.expr())
        idx: IdxAccess = self.visit(ctx.idx_access())
        cmp = ExprAccess(seq_id=self.comp_store.next_seq_id, source=source, idx=idx)
        return self._register(cmp)
