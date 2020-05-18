library(readr)
#install.packages("estimatr")
#install.packages("margins")
#install.packages("car")
library(estimatr)
library(margins)
library(car)
reg = lm_robust(log(Y2015) ~ log(L2015)+log(K2015), data = production2015)
summary(reg)

a=log(production2015$L2015)-log(production2015$K2015)
b=log(production2015$Y2015)-log(production2015$K2015)
production2015$a<-a
production2015$b<-b
reg = lm_robust(b ~ a, data = production2015)
summary(reg)
linearHypothesis(reg, c("a"), test = "F")

