from typing import Final

from mona.interpreter.component.arg_lst import ArgumentList
from mona.interpreter.component.component import Component
from mona.interpreter.environment.environment import Environment


class Print(Component):
    def __init__(self, seq_id: int, arg_lst: ArgumentList):
        super().__init__(seq_id=seq_id)
        self.arg_lst: Final[ArgumentList] = arg_lst

    def _eval_body(self, env: Environment) -> None:
        super()._eval_body(env=env)
        self.arg_lst.eval(env=env)

        print_elems = list()
        for i, _ in enumerate(self.arg_lst.exprs):
            tmp = env.mem_var(f"arg_{i}", self.seq_id)
            if not isinstance(tmp, str):
                tmp = str(tmp)
            print_elems.append(tmp)
        string = "".join(reversed(print_elems))
        print(string, end="")
        env.add_io_out(string)


class PrintLn(Print):
    def _eval_body(self, env: Environment) -> None:
        super()._eval_body(env=env)
        print("\n", end="")
        env.add_io_out("\n")
