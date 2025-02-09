import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """This function loads a csv file as pandas' DataFrame"""
    try:
        assert path.endswith("csv"), "File is not CSV"
        csv = pd.read_csv(path)
        return csv
    except FileNotFoundError:
        raise AssertionError("file not found")
