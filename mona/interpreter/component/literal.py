import abc
from typing import Any, Final

from mona.interpreter.component.expr_type import Expr
from mona.interpreter.environment.environment import Environment


class Literal(Expr, abc.ABC):
    value: Final[Any]

    def __init__(self, seq_id: int, value: Any):
        super().__init__(seq_id=seq_id)
        self.value = value

    def _eval_body(self, env: Environment) -> None:
        super()._eval_body(env=env)
        env.stack.append(self.value)


class LiteralInt(Literal):
    value: Final[int]  # noqa

    def __init__(self, seq_id: int, integer: int):
        super().__init__(seq_id=seq_id, value=integer)


class LiteralFloat(Literal):
    value: Final[float]  # noqa

    def __init__(self, seq_id: int, float_num: float):
        super().__init__(seq_id=seq_id, value=float_num)


class LiteralChar(Literal):
    value: Final[str]  # noqa

    def __init__(self, seq_id: int, char: str):
        super().__init__(seq_id=seq_id, value=char)


class LiteralString(Literal):
    value: Final[str]  # noqa

    def __init__(self, seq_id: int, string: str):
        super().__init__(seq_id=seq_id, value=string)


class LiteralBool(Literal):
    value: Final[bool]  # noqa

    def __init__(self, seq_id: int, boolean: bool):
        super().__init__(seq_id=seq_id, value=boolean)
