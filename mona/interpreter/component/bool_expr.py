import abc
from typing import Final

from mona.gen.GramLexer import GramLexer
from mona.interpreter.component.component import Component
from mona.interpreter.component.expr_type import Expr
from mona.interpreter.environment.environment import Environment


class BoolExpr(Expr, abc.ABC):
    ...


class BoolExprBinary(Component, abc.ABC):
    def __init__(self, seq_id: int, left: BoolExpr, right: BoolExpr):
        super(BoolExprBinary, self).__init__(seq_id=seq_id)
        self.left: Final[BoolExpr] = left
        self.right: Final[BoolExpr] = right

    def _eval_body(self, env: Environment) -> None:
        super(BoolExprBinary, self)._eval_body(env=env)
        self.left.eval(env)
        self.right.eval(env)


class BoolExprBinaryAnd(BoolExprBinary):
    def _eval_body(self, env: Environment) -> None:
        super(BoolExprBinaryAnd, self)._eval_body(env=env)
        right = env.mem_var("right", self.seq_id)
        left = env.mem_var("left", self.seq_id)
        env.stack.append(bool(left and right))


class BoolExprBinaryOr(BoolExprBinary):
    def _eval_body(self, env: Environment) -> None:
        super(BoolExprBinaryOr, self)._eval_body(env=env)
        right = env.mem_var("right", self.seq_id)
        left = env.mem_var("left", self.seq_id)
        env.stack.append(bool(left or right))


class BoolExprPref(BoolExpr, abc.ABC):
    def __init__(self, seq_id: int, expr: BoolExpr):
        super(BoolExprPref, self).__init__(seq_id=seq_id)
        self.expr: Final[BoolExpr] = expr


class BoolExprPrefNot(BoolExprPref):
    def __init__(self, seq_id: int, expr: BoolExpr):
        super(BoolExprPrefNot, self).__init__(seq_id=seq_id, expr=expr)

    def _eval_body(self, env: Environment) -> None:
        super(BoolExprPrefNot, self)._eval_body(env=env)
        self.expr.eval(env)
        tmp = env.mem_var("tmp", self.seq_id)
        env.stack.append(bool(not tmp))


class ComparisonOperator(int):
    LESSTHAN = GramLexer.LESSTHAN
    LESSTHANOREQUAL = GramLexer.LESSTHANOREQUAL
    GREATERTHAN = GramLexer.GREATERTHAN
    GREATERTHANOREQUAL = GramLexer.GREATERTHANOREQUAL


class BoolExprComparisonMath(BoolExpr):
    def __init__(
        self, seq_id: int, operator: ComparisonOperator, left: Expr, right: Expr
    ):
        super(BoolExprComparisonMath, self).__init__(seq_id=seq_id)
        self.operator: Final[ComparisonOperator] = operator
        self.left: Final[Expr] = left
        self.right: Final[Expr] = right

    def _eval_body(self, env: Environment) -> None:
        super(BoolExprComparisonMath, self)._eval_body(env=env)
        self.left.eval(env=env)
        left = env.mem_var("left", self.seq_id)

        self.right.eval(env=env)
        right = env.mem_var("right", self.seq_id)

        result = None
        if self.operator == ComparisonOperator.LESSTHAN:
            result = left < right
        elif self.operator == ComparisonOperator.LESSTHANOREQUAL:
            result = left <= right
        elif self.operator == ComparisonOperator.GREATERTHAN:
            result = left > right
        elif self.operator == ComparisonOperator.GREATERTHANOREQUAL:
            result = left >= right
        env.stack.append(result)


class BoolExprEquals(BoolExpr):
    def __init__(self, seq_id: int, left: Expr, right: Expr):
        super(BoolExprEquals, self).__init__(seq_id=seq_id)
        self.left: Final[Expr] = left
        self.right: Final[Expr] = right

    def _eval_body(self, env: Environment) -> None:
        super(BoolExprEquals, self)._eval_body(env=env)
        self.left.eval(env=env)
        left = env.mem_var("left", self.seq_id)

        self.right.eval(env=env)
        right = env.mem_var("right", self.seq_id)

        result = left == right
        env.stack.append(result)
