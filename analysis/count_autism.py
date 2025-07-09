import pandas as pd

data = pd.read_csv("output/dataset.csv.gz")

measure_count = len(data[data["autism_dat"].notnull()])

summary = pd.DataFrame({
    "Measure": ["HI21"],
    "Value": [measure_count]
})

summary.to_csv("output/hi21_summary.csv", index=False)