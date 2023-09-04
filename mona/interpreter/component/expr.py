import copy
from typing import Final

from mona.interpreter.component.expr_type import Expr
from mona.interpreter.component.idx_access import IdxAccess
from mona.interpreter.environment.environment import Environment


class ExprIden(Expr):
    def __init__(self, seq_id: int, iden: str):
        super(ExprIden, self).__init__(seq_id=seq_id)
        self.iden: Final[str] = iden

    def _eval_body(self, env: Environment) -> None:
        super(ExprIden, self)._eval_body(env=env)
        val = env.mem_get(self.iden)
        env.stack.append(val)


class ExprAccess(Expr):
    def __init__(self, seq_id: int, source: Expr, idx: IdxAccess):
        super(ExprAccess, self).__init__(seq_id=seq_id)
        self.source: Final[Expr] = source
        self.idx: Final[IdxAccess] = idx

    def _eval_body(self, env: Environment) -> None:
        super(ExprAccess, self)._eval_body(env=env)
        self.source.eval(env)
        self.idx.eval(env)


class ExprLenOf(Expr):
    def __init__(self, seq_id: int, expr: Expr):
        super(ExprLenOf, self).__init__(seq_id=seq_id)
        self.expr: Final[Expr] = expr

    def _eval_body(self, env: Environment) -> None:
        super(ExprLenOf, self)._eval_body(env=env)
        self.expr.eval(env=env)
        expr = env.mem_var("expr", self.seq_id)
        res = len(expr)
        env.stack.append(res)


class ExprCopyOf(Expr):
    def __init__(self, seq_id: int, expr: Expr):
        super(ExprCopyOf, self).__init__(seq_id=seq_id)
        self.expr: Final[Expr] = expr

    def _eval_body(self, env: Environment) -> None:
        super(ExprCopyOf, self)._eval_body(env=env)
        self.expr.eval(env=env)
        expr = env.mem_var("expr", self.seq_id)
        res = copy.deepcopy(expr)
        env.stack.append(res)
