import abc
from typing import Final

from mona.interpreter.component.component import Component
from mona.interpreter.component.expr_type import Expr
from mona.interpreter.environment.environment import Environment


class IdxAccess(Component, abc.ABC):
    ...


class IdxAccessOne(IdxAccess):
    def __init__(self, seq_id: int, idx: Expr):
        super(IdxAccess, self).__init__(seq_id=seq_id)
        self.idx: Final[Expr] = idx

    def _eval_body(self, env: Environment) -> None:
        super(IdxAccess, self)._eval_body(env=env)
        lst = env.mem_var("source_list", self.seq_id)

        self.idx.eval(env=env)
        idx: int = env.mem_var("idx", self.seq_id)

        value = lst[idx]
        env.stack.append(value)


class IdxAccessFrom(IdxAccess):
    def __init__(self, seq_id: int, from_idx: Expr):
        super(IdxAccess, self).__init__(seq_id=seq_id)
        self.from_idx: Final[Expr] = from_idx

    def _eval_body(self, env: Environment) -> None:
        super(IdxAccess, self)._eval_body(env=env)
        lst = env.mem_var("source_list", self.seq_id)

        self.from_idx.eval(env=env)
        from_idx: int = env.mem_var("from_idx", self.seq_id)

        value = lst[from_idx:]
        env.stack.append(value)


class IdxAccessUntil(IdxAccess):
    def __init__(self, seq_id: int, until_idx: Expr):
        super(IdxAccess, self).__init__(seq_id=seq_id)
        self.until_idx: Final[Expr] = until_idx

    def _eval_body(self, env: Environment) -> None:
        super(IdxAccess, self)._eval_body(env=env)
        lst = env.mem_var("source_list", self.seq_id)

        self.until_idx.eval(env=env)
        until_idx: int = env.mem_var("until_idx", self.seq_id)

        value = lst[:until_idx]
        env.stack.append(value)


class IdxAccessRange(IdxAccess):
    def __init__(self, seq_id: int, from_idx: Expr, until_idx: Expr):
        super(IdxAccess, self).__init__(seq_id=seq_id)
        self.from_idx: Final[Expr] = from_idx
        self.until_idx: Final[Expr] = until_idx

    def _eval_body(self, env: Environment) -> None:
        super(IdxAccess, self)._eval_body(env=env)
        lst = env.mem_var("source_list", self.seq_id)

        self.from_idx.eval(env=env)
        from_idx: int = env.mem_var("from_idx", self.seq_id)

        self.until_idx.eval(env=env)
        until_idx: int = env.mem_var("until_idx", self.seq_id)

        value = lst[from_idx:until_idx]
        env.stack.append(value)
