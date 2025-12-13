import pandas as pd

def map_coverage(row: pd.Series) -> float:
    year = row["year"]

    if year < 2010:
        weights = {"city_rate": 1.0, "line_rate": 0.0, "service_rate": 0.0}
    elif 2010 <= year <= 2020:
        weights = {"city_rate": 0.7, "line_rate": 0.3, "service_rate": 0.0}
    else:
        weights = {"city_rate": 0.4, "line_rate": 0.2, "service_rate": 0.4}

    total, w_sum = 0, 0
    for k, w in weights.items():
        if pd.notna(row[k]):
            total += row[k] * w
            w_sum += w

    return total / w_sum if w_sum else None
