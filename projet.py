import pandas as pd
#import numpy as np
from sklearn import preprocessing
import seaborn as sns
import matplotlib.pyplot as plt

#read csv file
data=pd.read_csv("Dat2.csv",header=0)


#cleaning data
data=data.drop(["Last Name:","First Name:"],axis=1)

data=data.dropna()

le=preprocessing.LabelEncoder()
Labeling=le.fit_transform(data["sex:"])

data["sex:"]=Labeling
print(data)

#relation
rel=data.corr()
sns.heatmap(rel)
plt.show()


