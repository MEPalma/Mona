from typing import Final

from mona.interpreter.component.expr_type import Expr
from mona.interpreter.environment.environment import Environment


class ListDeclaration(Expr):
    def __init__(self, seq_id: int, exprs: list[Expr]):
        super(ListDeclaration, self).__init__(seq_id=seq_id)
        self.exprs: Final[list[Expr]] = exprs

    def _eval_body(self, env: Environment) -> None:
        super()._eval_body(env=env)
        values = list()
        for i, expr in enumerate(self.exprs):
            expr.eval(env=env)
            tmp = env.mem_var(f"tmp_{i}", self.seq_id)
            values.append(tmp)
        env.stack.append(values)
