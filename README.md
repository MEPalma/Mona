# Mona
This is the replication repository for the Mona Language and Mona Interpreter.
The language provides functionality for program evaluation, program execution snapshotting and execution snapshot replay or re-execution.

## Executing Mona Programs
Programs are initially parsed utilising the Mona Parser:
```python
from mona.interpreter.parsing import Parser

src = 'println("Hello, World!")'
program, cmp_store = Parser.parse(src)
```
which returns the program interpreter and the components store of the specified definition.
To execute, the interpreter requires an Environment object, which also encapsulates an Execution Mode `ExecMode`.
This execution mode can be `ExecModeRun` for basic program evaluations, `ExecModeRecord` for execution snapshotting, `ExecModeStmtCount` for counting the number of program evaluation expression for the resulting execution, and `ExecModeReplay` for replaying a recorded memory snapshot.
Please note that all memory snapshots are already configured with a `ExecModeReplay` Execution Mode.
This repository offers factory methods for configuring all the described Execution Modes.
You can review usage of such factory in `mona/main.py` which utilises all of the modes to evaluate a demo program:

```plaintext
decl strlst(lst) {
    if (lenof(lst) > 0) {
        print(lst[0], "->");
        strlst(lst[1:]);
    }
}
strlst([1, 2, 3]);
```
The Mona Interpreter operates in an output directory.
In this program execution and replay snapshots are dumped.
The demo program outputs to `.output_dir/`.

You can execute this demo by running:
```
python main.py
```

### Evaluating Program
It is possible to evaluate a program utilising the provided factory method as:
```python
from mona import runtime_factory
runtime_factory.run(src=DEMO_SRC, output_dir=OUTPUT_DIR)
```
alternatively, the explicit workflow is:
```python
from mona.interpreter.parsing import Parser
from mona.interpreter.environment.environment import (
    Environment, ExecModeRun
)

env = Environment(exec_mode=ExecModeRun(dump_dir=OUTPUT_DIR))

program, cmp_store = Parser.parse(DEMO_SRC)
env.before_execution()
program.eval(env=env)
env.after_execution()
```

### Counting Evaluation Expressions
It is possible to count the total number of expressions that the MI evaluates during runtime utilising the factory method
```python
from mona import runtime_factory
runtime_factory.run_and_count_expressions(src=DEMO_SRC, output_dir=OUTPUT_DIR)
```
alternatively, the explicit workflow is:
```python
from mona.interpreter.parsing import Parser
from mona.interpreter.environment.environment import (
    Environment, ExecModeStmtCount
)

env = Environment(exec_mode=ExecModeStmtCount(dump_dir=OUTPUT_DIR))

program, cmp_store = Parser.parse(DEMO_SRC)
env.before_execution()
program.eval(env=env)
env.after_execution()
```

The number of expressions can be accessed by the output memory snapshot:
```python
with open(os.path.join(OUTPUT_DIR, "stmt_count_snap.pickle"), "rb") as df:
    env = pickle.load(df)
print("Expressions count: ", env.__dict__["_exec_mode"].stmts_run)
```

### Recording Execution Snapshots
It is possible to evaluate a program and record execution snapshots for a given steps size using the factory method:
```python
from mona import runtime_factory
runtime_factory.run_and_record(src=DEMO_SRC, output_dir=OUTPUT_DIR, steps=STEPS)
```
alternatively, the explicit workflow is:
```python
from mona.interpreter.parsing import Parser
from mona.interpreter.environment.environment import (
    Environment, ExecModeRecord
)

env = Environment(exec_mode=ExecModeRecord(dump_dir=OUTPUT_DIR, steps=STEPS))

program, cmp_store = Parser.parse(DEMO_SRC)
env.before_execution()
program.eval(env=env)
env.after_execution()
```

### Replaying Execution Snapshots
It is possible to replay a program snapshot recorded with the ExecModeRecord ExecutionMode using the factory method:
```python
from mona import runtime_factory
 runtime_factory.replay_snapshot(src=DEMO_SRC, snapshot_filename=replay_snapshot_filepath)
```
where `replay_snapshot_filepath` is the path to the recorded memory snapshot.
The resulting memory snapshot will be dumped in the same output directory.

alternatively, the explicit workflow is:
```python
from mona.interpreter.parsing import Parser

with open(replay_snapshot_filepath, "rb") as df:
    env = pickle.load(df)

program, cmp_store = Parser.parse(DEMO_SRC)
env.before_execution()
program.eval(env=env)
env.after_execution()
```

## Overview of language features

Here follows a brief demo of the main language features for mona.
For further details about the grammar of Mona please review the ANTLR4 `GramParser.g4` grammar file in `mona/antlr/GramParser.g4`.  
#### Variable Declarations
```plaintext
var x = 10;
var y = "Hello";
```

#### If-Else Blocks
```plaintext
if (x < 5) {
    println("x is less than 5");
} else if (x > 10) {
    println("x is greater than 10");
} else {
    println("x is between 5 and 10");
}
```

#### Function Declarations
```plaintext
decl add(a, b) {
    ret a + b;
}
```

#### Function Calls
```plaintext
result = add(5, 3);
sinValue = sin(30);
```

#### While Loops
```plaintext
while (x < 10) {
    println(x);
    x = x + 1;
}
```

#### Assignment Statements
```plaintext
x = 5;
arr[0] = 42;
```

#### Print Statements
```plaintext
println("Hello, world!");
print("Value of x: ", x);
```

#### Expressions
```plaintext
result = (3 + 2) * 4;
length = lenof(arr);
copyArr = copyof(arr);
```

