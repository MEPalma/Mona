from mona.interpreter.environment.environment import Environment
from mona.interpreter.parsing.parser import Parser

src = """
var x = True and False;
var y = x is False;
print(x);
print(y);
y = not (x is y);
print(y);
print(False);
print(True);
"""

# src = """
# var x = True;
# var y = not (x is False);
# print(x);
# """


def main():
    program, cmp_store = Parser.parse(src)
    env = Environment()

    # Exec the whole program:
    # env.curr_seq_id = 0
    # env.curr_steps = -1

    # Example program segment execution.
    #
    # From line 5, not, is.
    line_5_not_is = program.following.following.following.following.stmt.trgt.expr
    print(line_5_not_is)
    print(line_5_not_is.seq_id)
    env.curr_seq_id = line_5_not_is.seq_id
    #
    # # For 9 stmts
    env.curr_steps = 9
    # #
    # # # With this memory snapshot:
    env.mem["x"] = True
    env.mem["y"] = False
    env.stack = [
        env.mem["x"],
        env.mem["y"],
    ]  # Result of 'x' and 'y' in stmt '(x is y)'.

    program.eval(env)


if __name__ == "__main__":
    main()
