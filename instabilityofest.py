
#https://www.quantopian.com/research/notebooks/Cloned%20from%20%22Instability%20of%20Estimates%22%202.ipynb

# Instability of estimates notes 

# We'll be doing some examples, so let's import the libraries we'll need
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
# Set a seed so we can play with the data without generating new random numbers every time
np.random.seed(123)

#we need to examine the variance of sample sizes of diff sizes to see if the data is skewed
#first, we generate a random sample from the standard normal distribution (a list of 500 items)
#then we look at the normal mean of these items
normal = np.random.randn(500)
print(np.mean(normal[:10]))
print(np.mean(normal[:100]))
print(np.mean(normal[:250]))
print(np.mean(normal))

# The 'normed' kwarg was deprecated in Matplotlib 2.1 and will be removed in 3.1. Use 'density' instead.
# Plot a stacked histogram of the data
# As you can see, the normal withe the greater sample size looks more like the textbook normal distribution
plt.hist([normal[:10], normal[10:100], normal[100:250], normal], density=1, histtype='bar', stacked=True)
plt.ylabel('Frequency')
plt.xlabel('Value')
plt.show()


###################### 
"""
Binomial Distribution method notes: 
""" 


#Generate some data from a bi-modal distribution


# Jacques-Bera Test  
def bimodal(n):
    X = np.zeros((n))
    for i in range(n):
        if np.random.binomial(1, 0.5) == 0:
            X[i] = np.random.normal(-5, 1)
        else:
            X[i] =  np.random.normal(5, 1)
    return X
            
X = bimodal(1000)

#Let's see how it looks
plt.hist(X, bins=50)
plt.ylabel('Frequency')
plt.xlabel('Value')
print 'mean:', np.mean(X)
print 'standard deviation:', np.std(X)