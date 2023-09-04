from __future__ import annotations
from typing import Final

from mona.interpreter.component.component import Component
from mona.interpreter.environment.environment import Environment


class Program(Component):
    def __init__(self, seq_id: int, stmts: list[Component]):
        super(Program, self).__init__(seq_id=seq_id)
        self.stmts: Final[list[Component]] = stmts

    def _eval_body(self, env: Environment) -> None:
        super(Program, self)._eval_body(env=env)
        for stmt in self.stmts:
            stmt.eval(env=env)
