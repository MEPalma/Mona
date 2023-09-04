from typing import Any, Optional, Final

from mona.interpreter.component.component import Component
from mona.interpreter.component.expr_type import Expr
from mona.interpreter.environment.environment import Environment


class ReturnValue:
    pass
    # value: Optional[Any]
    #
    # def __init__(self, value: Optional[Any]):
    #     self.value = value


class Return(Component):
    def __init__(self, seq_id: int, expr: Optional[Expr]):
        super(Return, self).__init__(seq_id=seq_id)
        self.expr: Final[Optional[Expr]] = expr

    def _eval_body(self, env: Environment) -> None:
        super()._eval_body(env=env)
        if self.expr is not None:
            self.expr.eval(env=env)
        env.stack.append(ReturnValue())
