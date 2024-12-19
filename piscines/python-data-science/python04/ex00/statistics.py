def ft_mean(n: list) -> float:
    return sum(n) / len(n)


def ft_median(n: list) -> float:
    size = len(n)
    middle = size // 2

    n.sort()
    if size % 2 == 0:
        return n[middle - 1] + n[middle]
    return n[middle]


def ft_quartile(n: list) -> list:
    size = len(n)
    n.sort()
    return [float(n[size // 4]), float(n[size * 3 // 4])]


def ft_std(n: float) -> float:
    return ft_var(n) ** 0.5


def ft_var(n: list) -> float:
    mean = ft_mean(n)
    return sum((x - mean) ** 2 for x in n) / len(n)


def ft_statistics(*args, **kwargs) -> None:
    FN_DICT = {
        "mean": ft_mean,
        "median": ft_median,
        "quartile": ft_quartile,
        "std": ft_std,
        "var": ft_var
    }

    num = list(args)

    if not all([isinstance(x, (int, float)) and x >= 0 for x in num]):
        print("ERROR")
    else:
        for fn in kwargs.values():
            try:
                assert num, "No num provided"
                fun = FN_DICT.get(fn)
                if fun:
                    res = fun(num)
                    print(f"{fn} : {res}")
            except BaseException:
                print("ERROR")
