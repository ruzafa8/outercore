import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """This function loads a csv file as pandas' DataFrame"""
    try:
        assert path.endswith("csv"), "File is not CSV"
        csv = pd.read_csv(path)
        print(f"Loading dataset of dimensions {csv.shape}")
        return csv
    except BaseException as e:
        print(f"{type(e).__name__}: {e}")
        return None
