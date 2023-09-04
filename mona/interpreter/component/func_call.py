import abc
import math
from typing import Final, Any

from mona.interpreter.component.arg_lst import ArgumentList
from mona.interpreter.component.expr_type import Expr
from mona.interpreter.component.func_decl import FunctionDeclaration
from mona.interpreter.component.ret_stmt import ReturnValue
from mona.interpreter.component.stmt_block import StmtBlock
from mona.interpreter.environment.environment import Environment

class FunctionCall(Expr, abc.ABC):
    def __init__(self, seq_id: int, iden: str, arg_lst: ArgumentList):
        super().__init__(seq_id=seq_id)
        self.iden: Final[str] = iden
        self.arg_lst: Final[ArgumentList] = arg_lst


class FunctionCallBase(FunctionCall):
    def _eval_body(self, env: Environment) -> None:
        super()._eval_body(env=env)
        func_decl: FunctionDeclaration = env.mem_get(self.iden)
        assert len(self.arg_lst.exprs) == len(func_decl.param_lst.idens)

        env.add_trace(0)

        self.arg_lst.eval(env=env)
        for i, param_name in enumerate(reversed(func_decl.param_lst.idens)):
            value = env.mem_var(f"param_name_{i}", self.seq_id)
            env.mem_put(param_name, value)

        code_jump_entry: StmtBlock = func_decl.stmt_block
        code_jump_entry.eval(env=env)

        env.mem_var(
            "maybe_ret_value",
            self.seq_id,
            peak_cond=lambda sv: not isinstance(sv, ReturnValue),
        )

        env.rm_trace()


class MathsTransformationCall(FunctionCall, abc.ABC):
    def __init__(self, seq_id: int, iden: str, arg_lst: ArgumentList):
        super().__init__(seq_id=seq_id, iden=iden, arg_lst=arg_lst)
        assert len(arg_lst.exprs) == 1

    @abc.abstractmethod
    def _eval_math(self, arg: Any) -> Any:
        ...

    def _eval_body(self, env: Environment) -> None:
        super()._eval_body(env=env)
        self.arg_lst.eval(env=env)
        arg = env.mem_var("arg", self.seq_id)
        res = self._eval_math(arg)
        env.stack.append(res)


class SinCall(MathsTransformationCall):
    def _eval_math(self, arg: Any) -> Any:
        return math.sin(arg)


class FloorCall(MathsTransformationCall):
    def _eval_math(self, arg: Any) -> Any:
        return math.floor(arg)


class RoundCall(MathsTransformationCall):
    def _eval_math(self, arg: Any) -> Any:
        return int(arg)

class CeilCall(MathsTransformationCall):
    def _eval_math(self, arg: Any) -> Any:
        return math.ceil(arg)
