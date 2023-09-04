from __future__ import annotations

import abc
from typing import Final

from mona.gen.GramLexer import GramLexer
from mona.interpreter.component.expr_type import Expr
from mona.interpreter.environment.environment import Environment


class MathExpr(Expr, abc.ABC):
    ...


class MathBinaryOperator(int):
    PLUS = GramLexer.PLUS
    MINUS = GramLexer.MINUS
    TIMES = GramLexer.TIMES
    POW = GramLexer.POW
    DIV = GramLexer.DIV


class MathExprBinary(MathExpr, abc.ABC):
    def __init__(
        self,
        seq_id: int,
        operator: MathBinaryOperator,
        left: MathExpr,
        right: MathExpr,
    ):
        super(MathExprBinary, self).__init__(seq_id=seq_id)
        self.operator: Final[MathBinaryOperator] = operator
        self.left: Final[MathExpr] = left
        self.right: Final[MathExpr] = right

    def _eval_body(self, env: Environment) -> None:
        super(MathExprBinary, self)._eval_body(env=env)
        self.left.eval(env)
        left_value = env.mem_var("left_value", self.seq_id)

        self.right.eval(env)
        right_value = env.mem_var("right_value", self.seq_id)

        result = None
        if self.operator == MathBinaryOperator.PLUS:
            result = left_value + right_value
        elif self.operator == MathBinaryOperator.MINUS:
            result = left_value - right_value
        elif self.operator == MathBinaryOperator.TIMES:
            result = left_value * right_value
        elif self.operator == MathBinaryOperator.DIV:
            result = left_value / right_value
        elif self.operator == MathBinaryOperator.POW:
            result = left_value**right_value
        else:
            raise TypeError(f"Unsupported operator value '{self.operator}'.")
        env.stack.append(result)
