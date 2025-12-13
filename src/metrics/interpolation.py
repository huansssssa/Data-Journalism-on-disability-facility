def interpolate_coverage(df):
    df = df.sort_values("year")
    df["coverage_interp"] = df["coverage_rate"].interpolate("linear")
    return df
