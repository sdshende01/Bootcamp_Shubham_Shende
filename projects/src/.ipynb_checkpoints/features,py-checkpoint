"""
Feature Engineering functions for fund NAV and returns.
"""

import pandas as pd
import numpy as np

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add engineered features to fund NAV dataset.
    
    Parameters:
        df (pd.DataFrame): Must include ['date', 'fund_nav', 'fund_ret', 'benchmark_ret']
    
    Returns:
        pd.DataFrame: DataFrame with new feature columns.
    """

    df = df.copy()

    # Rolling averages and volatility
    df["fund_ret_ma5"] = df["fund_ret"].rolling(window=5).mean()
    df["fund_ret_ma20"] = df["fund_ret"].rolling(window=20).mean()
    df["fund_vol20"] = df["fund_ret"].rolling(window=20).std()

    # Benchmark rolling averages
    df["benchmark_ret_ma20"] = df["benchmark_ret"].rolling(window=20).mean()

    # Excess return (fund - benchmark)
    df["excess_ret"] = df["fund_ret"] - df["benchmark_ret"]

    # Cumulative returns (growth of $1)
    df["fund_cumret"] = (1 + df["fund_ret"]).cumprod()
    df["benchmark_cumret"] = (1 + df["benchmark_ret"]).cumprod()

    # Rolling correlation with benchmark
    df["rolling_corr"] = df["fund_ret"].rolling(window=60).corr(df["benchmark_ret"])

    # Risk-adjusted return proxy (Sharpe ratio-like)
    df["sharpe20"] = df["fund_ret_ma20"] / df["fund_vol20"]

    # Lagged features (autoregression)
    df["fund_ret_lag1"] = df["fund_ret"].shift(1)
    df["fund_ret_lag5"] = df["fund_ret"].shift(5)
    df["fund_ret_lag10"] = df["fund_ret"].shift(10)

    return df
