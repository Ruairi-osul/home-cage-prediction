from pathlib import Path
import pandas as pd

META_FILENAMES = {"mice": "mice.csv"}
FREEZE_FILENAMES = {
    "all": "freeze_behavior.csv",
    "ext_ret": "freeze_ext_ret.csv",
    "extinction": "freeze_extinction.csv",
    "cond": "freeze_fear_conditioning.csv",
    "renewal": "freeze_renewal.csv",
}
HOME_CAGE_FILENAMES = {
    "pre-cond": "hc_pre_conditioning.csv",
    "post-cond": "hc_post_conditioning.csv",
    "post-ext": "hc_post_extinction.csv",
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


def load_freeze_data(data_dir: Path) -> pd.DataFrame:
    """
    Load freeze data from all sessions.

    Args:
        data_dir (Path): Path to the raw data directory.

    Returns:
        pd.DataFrame: The freeze data for all sessions.
    """
    filename = FREEZE_FILENAMES["all"]
    file_path = data_dir / filename
    df = pd.read_csv(file_path)
    return df


def load_freeze_session_data(data_dir: Path, session: str) -> pd.DataFrame:
    """
    Load freeze data from a session.

    Args:
        data_dir (Path): Path to the raw data directory.
        session (str): The session to load data for. One of "ext_ret", "extinction", "cond", or "renewal".

    Returns:
        pd.DataFrame: The freeze data for the session.
    """
    filename = FREEZE_FILENAMES[session]
    file_path = data_dir / filename
    df = pd.read_csv(file_path)
    return df


def load_home_cage_data(data_dir: Path, segment: str) -> pd.DataFrame:
    """
    Load home cage data from a segment.

    Args:
        data_dir (Path): Path to the raw data directory.
        segment (str): The segment to load data for. One of "pre-cond", "post-cond", or "post-ext".

    Returns:
        pd.DataFrame: The home cage data for the segment.
    """
    filename = HOME_CAGE_FILENAMES[segment]
    file_path = data_dir / filename
    df = pd.read_csv(file_path)
    return df
