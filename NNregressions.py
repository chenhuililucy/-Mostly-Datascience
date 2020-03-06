
from keras.datasets import boston_housing 

(train_data,train_targets),(test_data,test_targets)=boston_housing.load_data()
print(train_data,train_targets)


mean=train_data.mean(axis=0)
#normalisation procedure, subtract by the mean (features wise) divideby the standard deviation 
train_data-=mean
std=train_data.std(axis=0)
train_data/=std 
test_data-=mean
std=test_data.std(axis=0)
test_data/=std 


