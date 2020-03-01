import sklearn

from sklearn.datasets import load_iris 
#this is one of the earliest data set developed to predict the type of iris based on features 
from sklearn.ensemble import RandomForestClassifier 
import pandas as pd 
import numpy as np 
np.random.seed(0)
iris=load_iris() 
df=pd.DataFrame(iris.data,columns=iris.feature_names)
print(df.head())
#print(iris)
df['species']=pd.Categorical.from_codes(iris.target,iris.target_names)
#as the dataset is 3 dimensional, we need to add a separate column for species names 
print(df.head())

##################

df['is_train']=np.random.uniform(0,1,len(df))<=.6 
#returns a boolean column with True or false showing if the column has been selected 
print(df.head())
train,test=df[df["is_train"]==True], df[df["is_train"]==False]
print("training set length: ", len(train))
print("testing set length: ", len(test))

features=df.columns[:4]
y=pd.factorize(train["species"])[0]
#train species of 0, when we run this piece of codes, you notice that y generates an array of 0s, 1s and 2s 
#convert species into 0,1s,and 2s 
clf=RandomForestClassifier(n_jobs=2,random_state=0) 
#passing 2 variables, n_jobs to prioritise this, this number changes the priority setting 
print(clf.fit(train[features],y))
#take training set with the features and get target y, remember that features is the dataset we are fitting in 

################
#Out 
# RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
#                        max_depth=None, max_features='auto', max_leaf_nodes=None,
#                        min_impurity_decrease=0.0, min_impurity_split=None,
#                        min_samples_leaf=1, min_samples_split=2,
#                        min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=2,
#                        oob_score=False, random_state=0, verbose=0,
#                        warm_start=False)
################

clf.predict(test[features])
#print(test[features]) 

###############


#If you are just printing features, you get categorical output, however, if you are printing test[features]
#You get the entire pandas data frame 

################
#generate a diff prediction model, which will require different viewing 
print(clf.predict_proba(test[features])[0:10]) #This piece of code allows one to view the predicted probabilities of the 
#first 10 observations 

# #[[0.9 0.1 0. ]
#  [1.  0.  0. ]
#  [1.  0.  0. ]
#  [1.  0.  0. ]
#  [0.9 0.1 0. ]
#  [1.  0.  0. ]
#  [0.9 0.1 0. ] 
#  [1.  0.  0. ]
#  [1.  0.  0. ]
#  [1.  0.  0. ]]

#all of these are preidictive probabilities 
preds=iris.target_names[clf.predict(test[features])]
preds[0:5]
pd.crosstab(test['species'],preds,rownames=['Actual'],colnames=["Predicted"])
#crosstab takes 2 sets of data and creates a data table out of it