import pandas as pd
import matplotlib.pyplot as plt


# statystyka podstawowywch informacji
def statistic(df):
    for col in df.columns:
        if col == 'class':
            break
        print('Columns', col)
        print('Min', df[[col]].min())
        print('Max', df[[col]].max())
        print('Mean', df[[col]].mean())
        print('Error', len(df[df[col] == '?'])/len(df), '%')
        if isinstance(df[col][1], str):
            # counts = df[col].value_counts().to_dict()
            if not col == 'native-country':
                counts = df[col].value_counts().to_dict()
            else:
                counts = {'United-States': len(df[df[col] == 'United-States']),
                          'Mexico': len(df[df[col] == 'Mexico']),
                          '?': len(df[df[col] == '?']),
                          }
                counts['Other'] = len(df[[col]]) - counts['United-States'] - counts['Mexico'] - counts['?']
        else:
            if col == 'age':
                counts = {'17-26': len(df[(df[col] >= 17) & (df[col] <= 26)]),
                          '27-35': len(df[(df[col] >= 27) & (df[col] <= 35)]),
                          '35-49': len(df[(df[col] >= 35) & (df[col] <= 49)]),
                          '50-59': len(df[(df[col] >= 50) & (df[col] <= 59)]),
                          '60-69': len(df[(df[col] >= 60) & (df[col] <= 69)]),
                          '70+': len(df[df[col] >= 70]),
                          }
            elif col == 'fnlwgt':
                counts = {'12.3K-86K': len(df[(df[col] >= 12285) & (df[col] < 86000)]),
                          '86K-160K': len(df[(df[col] >= 86000) & (df[col] < 160000)]),
                          '160K-233K': len(df[(df[col] >= 160000) & (df[col] < 233000)]),
                          '233K-306K': len(df[(df[col] >= 233000) & (df[col] < 306000)]),
                          '306K-380K': len(df[(df[col] >= 306000) & (df[col] < 380000)]),
                          '380K+': len(df[df[col] >= 380000]),
                          }
            elif col == 'education-num':
                counts = df[col].value_counts().to_dict()
                counts = dict(sorted(counts.items()))
            elif col == 'capitalgain':
                counts = {'0': len(df[df[col] == 0]),
                          'not 0': len(df[df[col] > 0]),
                          }
            elif col == 'capitalloss':
                counts = {'0': len(df[df[col] == 0]),
                          'not 0': len(df[df[col] > 0]),
                          }
            elif col == 'hoursperweek':
                counts = {'1h-20h': len(df[df[col] <= 20]),
                          '21h-35h': len(df[(df[col] >= 21) & (df[col] <= 35)]),
                          '36h-50h': len(df[(df[col] >= 35) & (df[col] < 50)]),
                          '51h-69h': len(df[(df[col] >= 51) & (df[col] < 70)]),
                          '70h-99h': len(df[df[col] >= 70]),
                          }
        try:
            counts['no data'] = counts.pop('?')
        except KeyError:
            print('we have all data')
        print(counts)
        y_pos = range(len(counts.keys())) if col != 'education-num' else [i+1 for i in range(len(counts.keys()))]
        plt.figure(figsize=(8, 6))
        plt.bar(counts.keys(), counts.values())
        plt.xticks(y_pos, counts.keys(), rotation=75)
        plt.tight_layout(pad=3)
        plt.title('the frequency in ' + str(col))
        plt.show()



