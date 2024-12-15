import sys
import ft_filter


def get_words_biggest_than(text, n):
    """this function receives a string and a number n and returns
    a list with the words that have more than n characters.
    """
    words_bigger_iter = ft_filter.ft_filter(lambda x: len(x) > n, text.split())
    words_bigger = [word for word in words_bigger_iter]
    return words_bigger


def main():
    """Main function. It receives two arguments:
    a phrase and a number, and print the words bigger than the number"""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert sys.argv[2].isdigit(), "the arguments are bad"

        text = sys.argv[1]
        n = int(sys.argv[2])

        words_bigger = get_words_biggest_than(text, n)
        print(words_bigger)
    except AssertionError as err:
        print(f"AssertionError: {err}")


if __name__ == "__main__":
    main()
