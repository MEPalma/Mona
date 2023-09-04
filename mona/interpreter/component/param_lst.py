from typing import Final

from mona.interpreter.component.component import Component
from mona.interpreter.environment.environment import Environment


class ParameterList(Component):
    def __init__(self, seq_id: int, idens: list[str]):
        super(ParameterList, self).__init__(seq_id=seq_id)
        self.idens: Final[list[str]] = idens

    def _eval_body(self, env: Environment) -> None:
        super()._eval_body(env=env)
        for iden in self.idens:
            cmp: Component = env.mem_get(iden)
            cmp.eval(env=env)
