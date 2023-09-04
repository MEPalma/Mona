import pickle
from deepdiff import DeepDiff


class EnvironmentComparer:
    def __init__(self):
        self.excluded_paths = ["_exec_mode"]

    def loadEnvironment(self, path):
        with open(path, "rb") as df:
            env = pickle.load(df)
        return env

    def compare(self, path_enva: str, path_envb: str):
        envA = self.loadEnvironment(path_enva)
        envB = self.loadEnvironment(path_envb)
        diff = DeepDiff(envA, envB, exclude_paths=self.excluded_paths)
        return len(diff), diff


def main():
    comparer = EnvironmentComparer()
    diffs = comparer.compare("demo_dump/4_out_snap.pickle", "demo_dump/5_snap.pickle")
    if diffs > 0:
        print("Snapshots are different!")
    else:
        print("No differences found")


if __name__ == "__main__":
    main()
