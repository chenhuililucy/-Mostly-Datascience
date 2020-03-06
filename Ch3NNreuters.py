#working with the reuters dataset 
#the reuters dataset is a set of short newswires and their topics, published by reuters in 1986 

DEBUG=True
from keras.datasets import reuters 
(train_data,train_labels),(test_data,test_labels)=reuters.load_data(num_words=10000)
if DEBUG: 

    print(len(train_data))
    print(len(test_data)) 
# will arrive at integers (list of word indices)
    print(train_data[10])
# to convert the coded integers back to words


#==========================================================================================#

# Decoding back to text 

word_index=reuters.get_word_index()
print(word_index) 
reversewordindex=dict([(value,keys) for (keys, value) in word_index.items()])
print(reversewordindex)
decoded_new=" ".join([reversewordindex.get(i-3,"?") for i in train_data[0]])
print(train_labels[5]) 

#==========================================================================================#


# Preparing the data 

import numpy as np
def vectorize_sequences(sequences,dimension=10000): 
    results =np.zeros((len(sequences), dimension)) # why ar there 2 backets? 
    for i, sequence in enumerate(sequences): 
            ## Python program to illustrate 
            # # enumerate function 
            # l1 = ["eat","sleep","repeat"] 
            # s1 = "geek"
  
            # # creating enumerate objects 
            # obj1 = enumerate(l1) 
            # obj2 = enumerate(s1) 
  
            # print "Return type:",type(obj1) 
            # print list(enumerate(l1)) 
  
            # # changing start index to 2 from 0 
            # print list(enumerate(s1,2)) 
        results[i,sequence]=1 # label as 1 in the place of a labled index 
    return results

X_train=vectorize_sequences(train_data)
Y_train=vectorize_sequences(test_data)

#Two methods to vectorize the labels 
#one hot encoding is widefly used format for categorizing data
#consists of embedding each label 

def one_hot(labels,dimensions=46): 
    results=np.zeros((len(labels),dimensions))
    for i, labels in enumerate(labels): 
        results[i,labels]=1 # label as 1 in the place of a labled index 
    return results 

one_hot_train=one_hot(train_labels)
one_hot_test=one_hot(test_labels)

#==========================================================================================#

#Model definition 

"""

model.layers is a flattened list of the layers comprising the model.
model.inputs is the list of input tensors of the model.
model.outputs is the list of output tensors of the model.
model.summary() prints a summary representation of your model. For layers with multiple outputs, multiple is displayed instead of each individual output shape due to size limitations. Shortcut for utils.print_summary

model.get_config() returns a dictionary containing the configuration of the model. The model can be reinstantiated from its config via:

config = model.get_config()
model = Model.from_config(config)
# or, for Sequential:
model = Sequential.from_config(config)

"""


from keras import models 
from keras import layers 

model=models.Sequential()
model.add(layers.Dense(64, activation='relu',input_shape=(10000,)))
model.add(layers.Dense(64,activation="relu"))
model.add(layers.Dense(46,activation='softmax'))

model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

""" 

Below codes cant debug 

"""
model.fit(partial_x_train,partial_y_train,epochs=9,batch_size=512,validation_data=(x_val,y_val))
results=model.evaluate(x_test, one_hot_test_labels) 

predictions=model.predict(x_test)



