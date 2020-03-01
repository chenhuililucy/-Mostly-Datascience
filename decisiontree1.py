#https://github.com/codebasics/py/blob/master/ML/9_decision_tree/9_decision_tree.ipynb
#practice file
#https://github.com/codebasics/py/blob/master/ML/9_decision_tree/Exercise/titanic.csv

import pandas as pd 
df=pd.read_csv("random.csv")
df.head()
input=df.drop("whatevername",axis="columns") 
target=df["whatevername"]
print(target)

#lable encoder import 
from sklearn.preprocessing import LabelEncoder 

#create classes 
le_company=LabelEncoder()
le_job=LabelEncoder()
le_degree=LabelEncoder()

#call fit and transform on input columns 
input['whatevername']=le_company.fit_transform(inputs['whatevername'])
input(head)

#because we have already applied labelencoder to the dataframe, we can now drop our original dataframe 
input_n=input.drop(['whatever','whatever','any column titles in list form'],axis='column') 
print(input_n)

#import data modules 
model=tree.DecisionTreeClassifier() 
model.fit(input_n,target)

model.score(input_n,target)

#predictions 
model.predict(["whatever data in csv, list form"])






