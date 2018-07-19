from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

# class: 0
df_a = pd.DataFrame({'x1': np.random.randn(100),
                     'x2': np.random.randn(100),
                     'y' : 0})
# class: 1
df_b = pd.DataFrame({'x1': np.random.randn(100) + 5,
                     'x2': np.random.randn(100) + 3,
                     'y' : 1})
df = df_a.append(df_b)

# トレーニングデータとテストデータに分割
X_train, X_test, y_train, y_test = \
    train_test_split(df[['x1','x2']], df['y'], test_size=0.2)