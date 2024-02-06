from pathlib import Path
import pandas as pd

META_FILENAMES = {"mice": "etoh_mice.csv"}
FILENAMES = {
    "etoh": "etoh_behavior.csv",
    "hc-base": "etoh_hc_base.csv",
    "hc-week-1": "etoh_hc_week1.csv",
    "hc-week-2": "etoh_hc_week2.csv",
    "hc-week-3": "etoh_hc_week3.csv",
}

def load_mice(data_dir: Path) -> pd.DataFrame:
    """
    Load metadata for mice.

    Args:
        data_dir (Path): Path to the raw data directory.

    Returns:
        pd.DataFrame: The metadata for the mice.
    """
    filename = META_FILENAMES["mice"]
    file_path = data_dir / filename
    mice = pd.read_csv(file_path)
    return mice


def load_etoh_data(data_dir: Path) -> pd.DataFrame:
    """
    Load ethinol consumption data from all weeks.

    Args:
        data_dir (Path): Path to the raw data directory.

    Returns:
        pd.DataFrame: The ethinol consumption data for all sessions.
    """
    filename = FILENAMES["etoh"]
    file_path = data_dir / filename
    df = pd.read_csv(file_path)
    return df


def load_home_cage_data(data_dir: Path, week: str) -> pd.DataFrame:
    """
    Load home cage data from a segment.

    Args:
        data_dir (Path): Path to the raw data directory.
        week (str): The week to load data for. One of "hc-base", "hc-week-1", "hc-week-2" or "hc-week-3".

    Returns:
        pd.DataFrame: The home cage data for the week.
    """
    filename = FILENAMES[week]
    file_path = data_dir / filename
    df = pd.read_csv(file_path)
    return df
