import abc
from typing import Final

from mona.interpreter.component.assig_trgt import AssigTrgt
from mona.interpreter.component.component import Component
from mona.interpreter.component.expr_type import Expr
from mona.interpreter.environment.environment import Environment


class Assig(Component, abc.ABC):
    ...


class AssigIden(Assig):
    def __init__(self, seq_id: int, iden: str, trgt: AssigTrgt):
        super(AssigIden, self).__init__(seq_id=seq_id)
        self.iden: Final[str] = iden
        self.trgt: Final[AssigTrgt] = trgt

    def _eval_body(self, env: Environment) -> None:
        super(AssigIden, self)._eval_body(env=env)
        self.trgt.eval(env)
        tmp = env.mem_var("assign_target", self.seq_id)
        env.mem_update(self.iden, tmp)


class AssigAccess(Assig):
    def __init__(self, seq_id: int, iden: str, idx: Expr, trgt: AssigTrgt):
        super(AssigAccess, self).__init__(seq_id=seq_id)
        self.iden: Final[str] = iden
        self.idx: Final[Expr] = idx
        self.trgt: Final[AssigTrgt] = trgt

    def _eval_body(self, env: Environment) -> None:
        super(AssigAccess, self)._eval_body(env=env)

        self.idx.eval(env)
        idx = env.mem_var("idx", self.seq_id)

        self.trgt.eval(env)
        target = env.mem_var("assign_target", self.seq_id)

        if not env.mem_exists(self.iden):
            raise RuntimeError(f"No such variable '{self.iden}' for Assig '{self}'.")

        source = env.mem_get(self.iden)
        source[idx] = target
