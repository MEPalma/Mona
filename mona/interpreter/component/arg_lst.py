from typing import Final

from mona.interpreter.component.component import Component
from mona.interpreter.component.expr_type import Expr
from mona.interpreter.environment.environment import Environment


class ArgumentList(Component):
    def __init__(self, seq_id: int, exprs: list[Expr]):
        super(ArgumentList, self).__init__(seq_id=seq_id)
        self.exprs: Final[list[Expr]] = exprs

    def _eval_body(self, env: Environment) -> None:
        super()._eval_body(env=env)
        for expr in self.exprs:
            expr.eval(env=env)
