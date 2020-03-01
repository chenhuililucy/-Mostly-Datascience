#https://github.com/codebasics/py/blob/master/ML/11_random_forest/11_random_forest.ipynb


import pandas as pd
from sklearn.datasets import load_digits
digits = load_digits()

dir(digits) #calls class' attributes 

#%matplotlib inline
import matplotlib.pyplot as plt

plt.gray() 

# Set the colormap to "gray".

# This changes the default colormap as well as the colormap of the current image if there is one. See help(colormaps) for more information.

for i in range(4):
    plt.matshow(digits.images[i])


#   Display an array as a matrix in a new figure window.

# The origin is set at the upper left hand corner and rows (first dimension of the array) are displayed horizontally. The aspect ratio of the figure window is that of the array, unless this would make an excessively short or narrow figure.

df = pd.DataFrame(digits.data)
df.head()

df['target'] = digits.target
print(df[0:12]) 

X = df.drop('target',axis='columns')
y = df.target
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=20)
model.fit(X_train, y_train)
model.score(X_test, y_test) #new introduction of probabillity score 
y_predicted = model.predict(X_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predicted)
print(cm)
#%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sn
plt.figure(figsize=(10,7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')



