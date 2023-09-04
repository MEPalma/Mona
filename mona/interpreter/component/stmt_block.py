from typing import Final

from mona.interpreter.component.component import Component, CodeJumpComponent
from mona.interpreter.component.ret_stmt import ReturnValue
from mona.interpreter.environment.environment import Environment


class StmtBlock(CodeJumpComponent):
    def __init__(self, seq_id: int, stmts: list[Component]):
        super(StmtBlock, self).__init__(seq_id=seq_id)
        self.stmts: Final[list[Component]] = stmts

    def _eval_body(self, env: Environment) -> None:
        super()._eval_body(env=env)
        for i, stmt in enumerate(self.stmts):
            stmt.eval(env=env)
            stmt_res = env.mem_var(
                f"stmt_res_{i}", self.seq_id, peak_cond=lambda _: True
            )
            if isinstance(stmt_res, ReturnValue):
                return
