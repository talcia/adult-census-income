import pandas as pd


def prepare_data_to_visual(df):

    df.loc[(df['workclass'] == 'Self-emp-not-inc') | (df['workclass'] == 'Self-emp-inc'), ['workclass']] = 'Self-emp'
    df.loc[(df['workclass'] == 'Local-gov') | (df['workclass'] == 'State-gov') |
           (df['workclass'] == 'Federal-gov'), ['workclass']] = 'Govermnet'
    df.loc[(df['workclass'] == '?') | (df['workclass'] == 'Never-worked') |
           (df['workclass'] == 'Without-pay'), ['workclass']] = 'Govermnet'

    df.loc[(df['marital-status'] == 'Married-AF-spouse') | (df['marital-status'] == 'Married-civ-spouse') |
           (df['marital-status'] == 'Married-spouse-absent'), ['marital-status']] = 'Married'
    df.loc[(df['marital-status'] == 'Never-married') | (df['marital-status'] == 'Divorced') |
           (df['marital-status'] == 'Separated') | (df['marital-status'] == 'Widowed'), ['marital-status']] = 'Single'

    df.loc[(df['occupation'] == 'Craft-repair') | (df['occupation'] == 'Farming-fishing') |
           (df['occupation'] == 'Handlers-cleaners') | (df['occupation'] == 'Machine-op-inspct') |
           (df['occupation'] == 'Transport-moving'),
           ['occupation']] = 'Physical-worker'

    df.loc[(df['occupation'] == 'Tech-support') | (df['occupation'] == 'Protective-serv') |
           (df['occupation'] == 'Priv-house-serv') | (df['occupation'] == 'Other-service'),
           ['occupation']] = 'Service'

    df.loc[(df['occupation'] == 'Adm-clerical') | (df['occupation'] == 'Exec-managerial'),
           ['occupation']] = 'Office-worker'

    df.loc[(df['race'] == 'Other') | (df['race'] == 'Black') | (df['race'] == 'Asian-Pac-Islander') |
           (df['race'] == 'Amer-Indian-Eskimo'),
           ['race']] = 'Other'

    return df


def prepare_data(df):
    df = df.drop(['fnlwgt', 'capitalgain', 'capitalloss', 'native-country', 'education'], axis=1)
    df = df.dropna()
    df['sex'] = df.apply(lambda row: 1 if 'Female' in row['sex'] else 0, axis=1)
    df['class'] = df.apply(lambda row: 1 if '>50' in row['class'] else 0, axis=1)
    df['marital-status'] = df.apply(lambda row: 1 if 'Married' in row['marital-status'] else 0, axis=1)
    df['race'] = df.apply(lambda row: 1 if 'White' in row['race'] else 0, axis=1)

    df = pd.get_dummies(df, columns=['workclass', 'occupation', 'relationship'])

    return df
