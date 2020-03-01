
import numpy 
import matplotlib
data=pd.read.csv("randomname.csv")
print(data.shape) #get datashape in terms of the column and row 
data.head() #get header of data (the first few rows)
X=data['datacolumntitle1'].values
Y=data['datacolumntitle2'].values 
mean.X=np.mean(X)
mean.Y=np.mean(Y)
for i in range(n)
    num=(X[i]-mean.X)*(Y[i]-mean.Y)
    denom=(Y[i]-mean.Y)**2
B=num/denom

#what is the last step in calculating the equation? 
