from enum import IntEnum, Enum
import pandas as pd
from pydantic import BaseModel


class Ternary(IntEnum):
    unknown = -1
    false = 0
    true = 1


class SourceType(Enum):
    prediction = "prediction"
    unknown = "unknown"
    easi_fish = "easi_fish"
    immunohistochemistry = "immunohistochemistry"


class Evidence(Enum):
    weak = "*"
    moderate = "**"
    strong = "***"


class Row(BaseModel):
    cell_type: str
    acetylcholine: Ternary
    glutamate: Ternary
    gaba: Ternary
    dopamine: Ternary
    serotonin: Ternary
    octopamine: Ternary
    tyramine: Ternary
    glycine: Ternary
    histamine: Ternary
    nitric_oxide: Ternary
    source: str
    source_type: SourceType
    evidence: Evidence


def validate_row(row: dict) -> Row:
    return Row(**row)


def validate_df(df):
    return df.apply(validate_row, axis=1)


def test_example():
    filename = "example_data.csv"
    df = pd.read_csv(filename)
    validate_df(df)
