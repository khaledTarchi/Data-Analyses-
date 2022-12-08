import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt

#read csv file
data=pd.read_csv("Student_Data.csv",header=0)


#cleaning data
data=data.drop(["Last Name:","First Name:"],axis=1)


le=preprocessing.LabelEncoder()

Se=le.fit_transform(data["sex:"])

Add=le.fit_transform(data["Addres:"])

data["sex:"]=Se
data["Addres:"]=Add

impt=SimpleImputer(missing_values=np.nan,
strategy="mean")

cld=impt.fit_transform(data)
new_data=pd.DataFrame(cld,columns=data.
columns)

new_data

new_data=new_data.dropna()
#relation
rel=new_data.corr()
sns.heatmap(rel)
plt.show()


