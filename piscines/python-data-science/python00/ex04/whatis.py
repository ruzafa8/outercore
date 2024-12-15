import sys


def parse_int(str_n: str) -> int:
    try:
        return int(str_n)
    except Exception:
        assert str_n.isnumeric(), "argument is not an integer"


def is_pair(n):
    return n % 2 == 0


try:
    num_args = len(sys.argv)
    assert num_args <= 2, "more than one argument is provided"
    if num_args == 2:
        n = parse_int(sys.argv[1])
        if is_pair(n):
            print("I'm Even.")
        else:
            print("I'm Odd.")
except AssertionError as msg:
    print(f"AssertionError: {msg}")
