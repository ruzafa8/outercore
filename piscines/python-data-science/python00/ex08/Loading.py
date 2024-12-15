def get_bar(percentage: int) -> str:
    """Given a percentage, returns an str with a bar filled
    til this percentage."""
    size_bar = 50
    num_bars = int(size_bar * percentage / 100)
    bar = "█" * num_bars
    spaces = " " * (size_bar - num_bars)
    return f"{bar}{spaces}"


def ft_tqdm(lst: range):
    """Decorates a range printing a progress bar."""
    lst_len = len(lst)
    for i, elem in enumerate(lst):
        percentage = int((i + 1) / lst_len * 100)
        print(
            f"{percentage:3d}%|{get_bar(percentage)}| {i+1}/{lst_len}",
            end="\r"
        )
        yield elem
