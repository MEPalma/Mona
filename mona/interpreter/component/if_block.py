from typing import Final, Optional

from mona.interpreter.component.component import Component
from mona.interpreter.component.else_stmt import ElseStmt
from mona.interpreter.component.elseif_stmt import ElseIfStmt
from mona.interpreter.component.if_outcome import IfOutcome
from mona.interpreter.component.if_stmt import IfStmt
from mona.interpreter.environment.environment import Environment


class IfBlock(Component):
    def __init__(
        self,
        seq_id: int,
        if_stmt: IfStmt,
        elseifs: list[ElseIfStmt],
        else_stmt: Optional[ElseStmt],
    ):
        super().__init__(seq_id=seq_id)
        self.if_stmt: Final[IfStmt] = if_stmt
        self.elseifs: Final[list[ElseIfStmt]] = elseifs
        self.else_stmt: Final[ElseStmt] = else_stmt

    def _eval_body(self, env: Environment) -> None:
        super()._eval_body(env=env)

        for i, if_stmt in enumerate([self.if_stmt, *self.elseifs]):
            if_stmt.eval(env=env)
            res: IfOutcome = env.mem_var(f"if_stmt_{i}", self.seq_id)
            if res == IfOutcome.Entered:
                return

        if self.else_stmt:
            self.else_stmt.eval(env=env)
