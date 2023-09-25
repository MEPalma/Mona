import os.path
import pickle
import threading

from mona.interpreter.environment.environment import (
    Environment, ExecModeRun, ExecModeRecord, ExecModeStmtCount,
)
from mona.interpreter.parsing import Parser


def _execute(src: str, env: Environment) -> None:
    def _inner():
        program, cmp_store = Parser.parse(src)
        env.before_execution()
        program.eval(env=env)
        env.after_execution()
    thread = threading.Thread(target=_inner)
    thread.start()
    thread.join()


def run(src: str, output_dir: str) -> None:
    env = Environment(exec_mode=ExecModeRun(dump_dir=output_dir))
    _execute(src=src, env=env)


def run_and_count_expressions(src: str, output_dir: str) -> None:
    env = Environment(exec_mode=ExecModeStmtCount(dump_dir=output_dir))
    _execute(src=src, env=env)
    with open(os.path.join(output_dir, "stmt_count_snap.pickle"), "rb") as df:
        env = pickle.load(df)
    print("\nExpressions count: ", env.__dict__["_exec_mode"].stmts_run)


def run_and_record(src: str, output_dir: str, steps: int) -> None:
    env = Environment(exec_mode=ExecModeRecord(dump_dir=output_dir, steps=steps))
    _execute(src=src, env=env)


def replay_snapshot(src: str, snapshot_filename: str) -> None:
    with open(snapshot_filename, "rb") as df:
        snapshot_env = pickle.load(df)
    _execute(src=src, env=snapshot_env)
