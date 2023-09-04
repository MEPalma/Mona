from typing import Final

from mona.interpreter.component.component import Component
from mona.interpreter.component.param_lst import ParameterList
from mona.interpreter.component.stmt_block import StmtBlock
from mona.interpreter.environment.environment import Environment


class FunctionDeclaration(Component):
    def __init__(
        self, seq_id: int, iden: str, param_lst: ParameterList, stmt_block: StmtBlock
    ):
        super(FunctionDeclaration, self).__init__(seq_id=seq_id)
        self.iden: Final[str] = iden
        self.param_lst: Final[ParameterList] = param_lst
        self.stmt_block: Final[StmtBlock] = stmt_block

    def _eval_body(self, env: Environment) -> None:
        super()._eval_body(env=env)
        if env.mem_exists(self.iden):
            raise RuntimeError(f"Redeclaration of function '{self}'.")
        env.mem_put(self.iden, self)
