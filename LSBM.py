""" 

Implementing LSBM with IMBD datasets with coursera tutorial and workbook

""" 
 
 #load data file 


# class documents(): 
#      def __init__(self): 
#       self.label_type=label_type 


import os 
imdir="/Users/lucy/Desktop/assortedcodes/aclImdb"
traindir=imdir+'/train'
testdir=imdir+'/test'

label=[] 
texts=[]
 
for label_type in ["neg", "pos"]: 
    
    dirname=os.path.join(traindir,label_type)
    for filenames in os.listdir(dirname): 
        #print(filenames)
        if filenames[-4:] == ".txt": 
            f=open(os.path.join(dirname,filenames))
            texts.append(f.read())
            f.close()
            if label_type == "neg": 
                label.append(0)
            else: 
                label.append(1)

print("done")

# tockenizing text 

from keras.preprocessing.text import Tokenizer 

# text tokenization utility class 
# vectorize a text corpus, turning each text into either a 
# sequence of integers or vector where the coefficient 
# of each token could be binary, based on wordcount/tfidf 

from keras.preprocessing.sequence import pad_sequences 
import numpy as np 

maxlen1=100 
trainsamples=200 
validation_samples=10000 
maxwords=10000

tokenizer=Tokenizer(num_words=maxwords)
tokenizer.fit_on_texts(texts)

# transform each text in texts to a sequence of integers 
# So it basically takes each word in the text and replaces it with its corresponding integer value from the word_index dictionary.
# Nothing more, nothing less, certainly no magic involved.
sequence=tokenizer.texts_to_sequences(texts)


# tokenizer.fit_on_texts expects a list of texts, 
# where you are passing it a single string.
#  Likewise for tokenizer.texts_to_sequences(). 
# Try passing lists to both methods:


word_index=tokenizer.word_index
print("%s word index" %len(word_index)) 
X = pad_sequences(sequence, maxlen=maxlen1)
label=np.asarray(label)
print("Shape of data tensor:", X.shape)
print("Shape of label tensor:", label.shape)
dir(X.shape)
indices=np.arange(X.shape[0]) 
np.random.shuffle(indices)

X=X[indices]
label=label[indices]

x_train=X[:trainsamples]
y_train=label[:trainsamples]
x_val=X[trainsamples:trainsamples+validation_samples]
y_val=X[trainsamples:trainsamples+validation_samples]



""" 

Parsing the Glove word-embeddings file

""" 

glove_dir=""
embeddings_index={}
f=open(os.path.join(glove_dir, "")
for line in f: 
    values=line.split() 
    word=values[0]
    coefs=np.asarray(values[1:],dtype='float32')
    embeddings_index[word]=coefs 
f.close() 
print("Found %s word vectors" %len(embeddings_index))

# embedding matrix that you can load into an Embedding layer 
# must be a matrix of shape (max_words, embedding_dim) 
# each entry i contains the embedding_dim domensional vector 
# for the word of index i in the reference word index 

embedding_dim=100 
embedding_matrix=np.zeros((max_words,embedding_dim)) 
for word, i in word_index.items() 
    if i<max_words: 
        embedding_vector=embedding_index.get(word)
        if embedding_vector is not None: 
            embedding_matrix[i] = embedding_vector 


from keras.models import Sequential 
from keras.layers import Embedding, Flatten, Dense 

model=Sequential() 
model.add(Embedding(max_words,embedding_dim,input_length=maxlen)) 
model.add(Flatten())
model.add(Dense(32,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.summary() 


