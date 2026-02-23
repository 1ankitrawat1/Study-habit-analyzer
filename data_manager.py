import pandas as pd
import os

FILE_NAME = "study_log.csv"

def load_data():
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=["date", "subject", "hours", "focus"])
        df.to_csv(FILE_NAME, index=False)
    return pd.read_csv(FILE_NAME)

def save_entry(date, subject, hours, focus):
    df = load_data()
    new_row = pd.DataFrame([[date, subject, hours, focus]], columns = df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)