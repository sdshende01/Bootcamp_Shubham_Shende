"""
src/cleaning.py
Reusable cleaning and preprocessing functions for fund + benchmark NAV data.

Assumptions & Rationale:
- Drop missing NAV values (fund holidays, bad API rows).
- Forward-fill gaps if minor (<3 days) to keep continuity.
- Align fund and benchmark on intersection of dates for fair comparison.
- Compute daily returns (pct_change).
- Remove extreme outliers in returns (>|10%|) as likely data errors.
"""

import pandas as pd
import numpy as np

def clean_nav_data(df: pd.DataFrame,
                   fund_col: str = "ICICI_LargeMidcap",
                   bench_col: str = "Nifty50_BeES") -> pd.DataFrame:
    """
    Clean merged fund & benchmark NAV dataset.
    
    Steps:
    - Ensure date is datetime & sorted
    - Drop missing NAVs, forward fill small gaps
    - Align both series on same dates
    - Compute daily returns
    - Winsorize returns at 1st/99th percentile
    """
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").drop_duplicates("date")

    # Drop missing NAVs
    df = df.dropna(subset=[fund_col, bench_col])

    # Forward fill tiny gaps (assume holiday NAV carry-forward is valid)
    df[fund_col] = df[fund_col].fillna(method="ffill", limit=3)
    df[bench_col] = df[bench_col].fillna(method="ffill", limit=3)

    # Re-drop if any remain
    df = df.dropna(subset=[fund_col, bench_col])

    # Compute daily returns
    df["fund_ret"] = df[fund_col].pct_change()
    df["bench_ret"] = df[bench_col].pct_change()

    # Remove outliers (winsorize returns)
    for col in ["fund_ret", "bench_ret"]:
        lower, upper = df[col].quantile([0.01, 0.99])
        df[col] = df[col].clip(lower, upper)

    df = df.dropna().reset_index(drop=True)
    return df
