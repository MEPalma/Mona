from typing import Final

from mona.interpreter.component.assig_trgt import AssigTrgt
from mona.interpreter.component.component import Component
from mona.interpreter.environment.environment import Environment


class VarDeclr(Component):
    def __init__(self, seq_id: int, iden: str, assig_trgt: AssigTrgt):
        super(VarDeclr, self).__init__(seq_id=seq_id)
        self.iden: Final[str] = iden
        self.assig_trgt: Final[AssigTrgt] = assig_trgt

    def _eval_body(self, env: Environment) -> None:
        super(VarDeclr, self)._eval_body(env=env)
        self.assig_trgt.eval(env)
        tmp = env.mem_var("tmp", self.seq_id)
        env.mem_put(self.iden, tmp)
