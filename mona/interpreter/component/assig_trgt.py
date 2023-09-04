import abc
from typing import Final

from mona.interpreter.component.component import Component
from mona.interpreter.component.expr_type import Expr
from mona.interpreter.environment.environment import Environment


class AssigTrgt(Component, abc.ABC):
    ...


class AssigTrgtIden(AssigTrgt):
    def __init__(self, seq_id: int, iden: str):
        super(AssigTrgtIden, self).__init__(seq_id=seq_id)
        self.iden: Final[str] = iden

    def _eval_body(self, env: Environment) -> None:
        super(AssigTrgtIden, self)._eval_body(env=env)
        value = env.mem_get(self.iden)
        env.stack.append(value)


class AssigTrgtExpr(AssigTrgt):
    def __init__(self, seq_id: int, expr: Expr):
        super(AssigTrgtExpr, self).__init__(seq_id=seq_id)
        self.expr: Final[Expr] = expr

    def _eval_body(self, env: Environment) -> None:
        super(AssigTrgtExpr, self)._eval_body(env=env)
        self.expr.eval(env)
