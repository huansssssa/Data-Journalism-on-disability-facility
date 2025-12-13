import yaml
import pandas as pd

from src.fetch.fetch_policy_text import fetch_policy_text
from src.llm.extract_indicators import extract_with_qwen
from src.metrics.coverage_mapping import map_coverage
from src.metrics.interpolation import interpolate_coverage

def main():
    with open("config/urls.yaml", "r", encoding="utf-8") as f:
        urls = yaml.safe_load(f)

    records = []

    for year, url in urls.items():
        print(f"Processing year {year}")
        text = fetch_policy_text(url)
        indicators = extract_with_qwen(text)
        indicators["year"] = int(year)
        records.append(indicators)

    df = pd.DataFrame(records)
    df["coverage_rate"] = df.apply(map_coverage, axis=1)
    df = interpolate_coverage(df)

    df.to_csv("data/output/coverage_timeseries.csv", index=False)
