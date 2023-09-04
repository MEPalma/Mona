import os
import pickle
import shutil
import sys
import threading

from mona.demo_programs.environment_comparer import EnvironmentComparer
from mona.interpreter.environment.environment import (
    Environment,
    ExecModeRecord,
    ExecModeRun,
    ExecModeStmtCount,
)
from mona.interpreter.parsing.parser import Parser

sys.setrecursionlimit(2147483647)

def run_env() -> Environment:
    return Environment(exec_mode=ExecModeRun(dump_dir="dump_dir"))


def record_env() -> Environment:
    return Environment(exec_mode=ExecModeRecord(steps=128, dump_dir="dump_dir/"))


def count_env() -> Environment:
    return Environment(exec_mode=ExecModeStmtCount(dump_dir="./"))


def read_stmt_count(filepath: str) -> None:
    with open(filepath, "rb") as df:
        env = pickle.load(df)
    print(env.__dict__["_exec_mode"].stmts_run)


def load_replay(filepath: str):
    with open(filepath, "rb") as df:
        env = pickle.load(df)
    return env


def eval_replay(program, filepath: str):
    env = load_replay(filepath)
    env.before_execution()
    program.eval(env)
    env.after_execution()


def test_record_replay(file_path: str):
    with open(file_path, "r") as df:
        src = df.read()

    program, cmp_store = Parser.parse(src)

    # Prep directory.
    dump_dir = "dump_dir"
    if os.path.isdir(dump_dir):
        shutil.rmtree(dump_dir)
    os.mkdir(dump_dir)

    # Run with snaps.
    env = record_env()
    env.before_execution()
    program.eval(env)
    env.after_execution()

    # Replay and check.
    num_snapshots = len([filename for filename in os.listdir(dump_dir) if filename.endswith("_snap.pickle")])
    print("="*100)
    print(f"Validating {num_snapshots} snapshots.")
    print("=" * 100)

    for snapshot_num in range(num_snapshots - 1):
        snapshot_filename = os.path.join(dump_dir, f"{snapshot_num}_snap.pickle")
        replayed_filename = os.path.join(dump_dir, f"{snapshot_num}_out_snap.pickle")
        target_filename = os.path.join(dump_dir, f"{snapshot_num + 1}_snap.pickle")

        thread = threading.Thread(target=eval_replay, args=(program, snapshot_filename))
        thread.start()
        thread.join()

        comparer = EnvironmentComparer()
        num_diffs, diffs = comparer.compare(target_filename, replayed_filename)
        if num_diffs > 0:
            print(
                "[ ERROR ]\n",
                f"Snap ID: {snapshot_num}, "
                f"SrcSnap: {snapshot_filename}, "
                f"OurSnap: {replayed_filename}, "
                f"TrgSnap: {target_filename}\n"
                "[ DIFF ]\n",
                diffs,
                "\n",
                file=sys.stderr
            )
            break


def test_run(filename: str):
    with open(filename, "r") as df:
        src = df.read()

    program, cmp_store = Parser.parse(src)

    # Run with not snaps.
    env = count_env()

    # Run with snaps.
    program.eval(env)
    env.after_execution()

    read_stmt_count("stmt_count_snap.pickle")


if __name__ == "__main__":
    test_record_replay("programs/fibonacci_iterative_pretty.mona")
