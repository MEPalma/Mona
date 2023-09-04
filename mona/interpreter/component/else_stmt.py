from typing import Final

from mona.interpreter.component.component import Component
from mona.interpreter.component.stmt_block import StmtBlock
from mona.interpreter.environment.environment import Environment


class ElseStmt(Component):
    def __init__(self, seq_id: int, stmt_block: StmtBlock):
        super().__init__(seq_id=seq_id)
        self.stmt_block: Final[StmtBlock] = stmt_block

    def _eval_body(self, env: Environment) -> None:
        super()._eval_body(env=env)
        self.stmt_block.eval(env=env)
