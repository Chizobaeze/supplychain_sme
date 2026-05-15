from datasets import load_dataset
import pandas as pd


def load_data():

    ds = load_dataset(
        "electricsheepafrica/africa-synth-banking-sme-loans-nigeria"
    )

    df = ds["train"].to_pandas()

    df = df.head(500)

    return df