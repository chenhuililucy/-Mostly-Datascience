#Perhaps one of the simplest and useful distribution is the uniform distribution. 
# import uniform distribution
from scipy.stats import uniform
n = 10000
start = 10
width = 20

#The uniform function generates a uniform continuous variable between the specified interval via its loc and scale arguments. 
#This distribution is constant between loc and loc + scale. The size arguments describe the number of random variates. 
#If you want to maintain reproducibility, include a random_state argument assigned to a number.
data_uniform = uniform.rvs(size=n, loc = start, scale=width)


"""
Seaborn uniform distribution
"""

# You can use Seaborn’s distplot to plot the histogram of the distribution you just created. 
# Seaborn’s distplot takes in multiple arguments to customize the plot. You first create a plot object ax. 
# Here, you can specify the number of bins in the histogram, specify the color of the histogram and specify density plot option with kde and linewidth option with hist_kws. 
# You can also set labels for x and y axis using the xlabel and ylabel arguments.
# The sns library is called the seaborn library 
ax = sns.distplot(data_uniform,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Uniform Distribution ', ylabel='Frequency')

from scipy.stats import norm
# generate random numbers from N(0,1)
data_normal = norm.rvs(size=10000,loc=0,scale=1)


"""
Seaborn normal distribution
"""


ax = sns.distplot(data_normal,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')


"""
Seaborn poisson distribution
"""


s=np.random.poisson(5, 10000)
import matplotlib.pyplot as plt
plt.hist(s,16,normed=True,color='Green')


""" 
Seaborn bernoulli distribution
"""

s=np.random.binomial(10,0.5,1000)
plt.hist(s,16,normed=True,color='Brown')
