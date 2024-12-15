import sys


def print_text_breakdown(text):
    """this function iterates over the string and counts
    the upper, lower, digits, punctuation maks and spaces,
    and prints a resume.
    """
    num_chars = 0
    num_upper = 0
    num_lower = 0
    num_punctuation_marks = 0
    num_spaces = 0
    num_digits = 0

    for c in text:
        if c.isupper():
            num_upper += 1
        elif c.islower():
            num_lower += 1
        elif c.isdigit():
            num_digits += 1
        elif c.isspace():
            num_spaces += 1
        else:
            num_punctuation_marks += 1
        num_chars += 1

    print(f"The text contains {num_chars} characters:")
    print(f"{num_upper} upper letters")
    print(f"{num_lower} lower letters")
    print(f"{num_punctuation_marks} punctuation marks")
    print(f"{num_spaces} spaces")
    print(f"{num_digits} digits")


def main():
    """main function"""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print("What is the text to count?")
            text = sys.stdin.readline()
        print_text_breakdown(text)
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
