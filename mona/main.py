import os
import shutil
from typing import Final

from mona import runtime_factory


DEMO_SRC: Final[str] = """
decl strlst(lst) {
    if (lenof(lst) > 0) {
        print(lst[0], "->");
        strlst(lst[1:]);
    }
}
strlst([1, 2, 3]);
"""
OUTPUT_DIR: Final[str] = os.path.join(os.getcwd(), "output_dir")
STEPS: Final[int] = 12


def main():
    # Initialise output directory.
    if os.path.isdir(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.mkdir(OUTPUT_DIR)

    # Run program.
    print(">>>>>> EVALUATING PROGRAM")
    runtime_factory.run(src=DEMO_SRC, output_dir=OUTPUT_DIR)

    print("\n>>>>>> COUNTING PROGRAM EXPRESSIONS")
    runtime_factory.run_and_count_expressions(src=DEMO_SRC, output_dir=OUTPUT_DIR)

    print("\n>>>>>> RECORDING PROGRAM EXECUTION")
    runtime_factory.run_and_record(src=DEMO_SRC, output_dir=OUTPUT_DIR, steps=STEPS)

    replay_snapshot_filepath = os.path.join(OUTPUT_DIR, "4_snap.pickle")
    output_replay_snapshot_filepath = os.path.join(OUTPUT_DIR, "4_out_snap.pickle")
    print(f"\n>>>>>> REPLAYING EXECUTION SNAPSHOT '{replay_snapshot_filepath}' into '{output_replay_snapshot_filepath}'")
    runtime_factory.replay_snapshot(src=DEMO_SRC, snapshot_filename=replay_snapshot_filepath)


if __name__ == "__main__":
    main()
