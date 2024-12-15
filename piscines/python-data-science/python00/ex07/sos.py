import sys

NESTED_MORSE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': '/ ',
}


def morse(text):
    """this function receives a string and returns the morse code
    for the string.
    """
    return ' '.join([NESTED_MORSE.get(c, c) for c in text.upper()])


def validate_input():
    """Validates the input is a phrase"""
    assert len(sys.argv) == 2, "the arguments are bad"
    text = sys.argv[1]

    for c in text:
        assert c.isalnum() or c.isspace(), "the arguments are bad"
    return text


def main():
    """main function. This function receives one argument,
    which is a phrase and prints it in morse code."""
    try:
        text = validate_input()
        print(morse(text))
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
