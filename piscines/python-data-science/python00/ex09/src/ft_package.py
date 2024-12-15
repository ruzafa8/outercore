def count_in_list(lst: list, item: str) -> int:
    return len([x for x in lst if x == item])
