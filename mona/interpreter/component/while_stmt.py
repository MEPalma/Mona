from typing import Final

from mona.interpreter.component.bool_expr import BoolExpr
from mona.interpreter.component.component import Component
from mona.interpreter.component.stmt_block import StmtBlock
from mona.interpreter.environment.environment import Environment


class While(Component):
    def __init__(self, seq_id: int, bool_expr: BoolExpr, stmt_block: StmtBlock):
        super().__init__(seq_id=seq_id)
        self.bool_expr: Final[BoolExpr] = bool_expr
        self.stmt_block: Final[StmtBlock] = stmt_block

    def _eval_body(self, env: Environment) -> None:
        super()._eval_body(env=env)

        env.add_trace(0)
        self.bool_expr.eval(env=env)
        is_condition = env.mem_var("bool_expr_res", self.seq_id)

        while is_condition:
            self.stmt_block.eval(env=env)
            env.rm_trace()

            env.add_trace(0)
            self.bool_expr.eval(env=env)
            is_condition = env.mem_var("bool_expr_res", self.seq_id)

        env.rm_trace()
