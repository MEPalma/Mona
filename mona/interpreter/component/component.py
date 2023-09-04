from __future__ import annotations

import abc
import pickle
import sys
from typing import Final

from mona.interpreter.environment.environment import Environment

DEBUG = False


class Component(abc.ABC):
    def __init__(self, seq_id: int):
        self.seq_id: Final[int] = seq_id

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"({self.__class__.__name__}| {str(self.__dict__)})"

    def _log_exec_point(self, env: Environment) -> str:
        return f"[{self.seq_id}] -> {env.trace_idx}, {env.call_trace}"

    def _get_decorated_components(self) -> list[Component]:
        decorated_components: list[Component] = list()
        for member in self.__dict__.values():
            if isinstance(member, Component):
                decorated_components.append(member)
            elif isinstance(member, list):
                decorated_components.extend(
                    [
                        sub_member
                        for sub_member in member
                        if isinstance(sub_member, Component)
                    ]
                )
            elif isinstance(member, dict):
                decorated_components.extend(
                    [
                        sub_member
                        for sub_member in member.values()
                        if isinstance(sub_member, Component)
                    ]
                )
        return decorated_components

    def eval(self, env: Environment) -> None:
        # Don't execute this code point is env point to the next, as it already was.
        if self.seq_id <= env.seq_id:
            if DEBUG:
                print(f"[DEBUG] [prun] {self._log_exec_point(env)} -> {self}")
            return

        # Execute exactly this code point (self.seq_id == env.seq_id).
        if DEBUG:
            print(f"[DEBUG] [eval] {self._log_exec_point(env)} -> {self}")

        # Run sub-logic.
        self._eval_body(env)

        # Set the code point to the next (all children logic had smaller indexes).
        env.seq_id = self.seq_id

        env.after_statement()

    @abc.abstractmethod
    def _eval_body(self, env: Environment) -> None:
        ...


class CodeJumpComponent(Component, abc.ABC):
    def eval(self, env: Environment) -> None:
        env.add_trace(0)
        super().eval(env=env)
        env.rm_trace()
