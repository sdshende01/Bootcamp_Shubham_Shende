"""
src/outliers.py

Reusable functions for detecting, removing, or flagging outliers in NAV return data.

Outlier Assumptions:
- Daily mutual fund returns > |5%| are unusual for diversified funds; likely errors or rare events.
- Use statistical methods (Z-score, IQR) as general-purpose detection.
- Strategy: either remove or winsorize depending on modeling goals.
"""

import pandas as pd
import numpy as np

def detect_outliers_zscore(series: pd.Series, threshold: float = 3.0) -> pd.Series:
    """
    Detect outliers using Z-score method.
    
    Parameters:
    - series: numeric pandas Series
    - threshold: absolute z-score cutoff
    
    Returns: Boolean mask where True = outlier
    """
    z_scores = (series - series.mean()) / series.std(ddof=0)
    return z_scores.abs() > threshold

def detect_outliers_iqr(series: pd.Series, factor: float = 1.5) -> pd.Series:
    """
    Detect outliers using Interquartile Range (IQR).
    
    Returns: Boolean mask where True = outlier
    """
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower, upper = q1 - factor * iqr, q3 + factor * iqr
    return (series < lower) | (series > upper)

def winsorize_series(series: pd.Series, lower_q: float = 0.01, upper_q: float = 0.99) -> pd.Series:
    """
    Winsorize series by capping values at lower/upper quantiles.
    """
    lower, upper = series.quantile([lower_q, upper_q])
    return series.clip(lower, upper)
