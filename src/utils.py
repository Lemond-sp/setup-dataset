import pandas as pd

filename = "hoge"
df = pd.read_csv(filename,sep='\t')


def remove_newline(df,target_col: str):
    # object型を改行する際には、regexが必要
    df[target_col] = df[target_col].replace('\n','',regex=True)
    return df