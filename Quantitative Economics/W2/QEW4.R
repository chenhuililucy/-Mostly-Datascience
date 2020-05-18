library(readr)
#install.packages("estimatr")
#install.packages("margins")
#install.packages("car")
library(estimatr)
library(margins)
library(car)
#h <- read.csv("height.csv")
reg = lm_robust(earnings ~ height, data = h)
reg_lm=lm(earnings ~ height, data = h)

summary(reg)
summary(reg_lm)

reg1 <- lm_robust(earnings  ~ height + sex + sex * height, data = h)
summary(reg1)
linearHypothesis(reg1, c("height:sex = 0"), test = "F")
#reg2 <- lm_robust(earnings  ~ sex * height, data = h)
#linearHypothesis(reg2, c("height:sex = 0"), test = "F")
lths<-ifelse(h$educ<=11, 1, 0)
hs<-ifelse(h$educ==12, 1, 0)
scoll<-ifelse(intersect(h$educ>=13,h$educ<=15), 1, 0)
coll<-ifelse(h$educ>=16, 1, 0)
# 
h$lths<-lths
h$hs<-hs
h$scoll<-scoll
h$coll<-coll

reg3 <- lm_robust(earnings  ~ height, data=subset(h, sex=="0"))
summary(reg3)
reg4 <- lm_robust(earnings  ~ height + lths + hs + scoll, data=subset(h, sex=="0"))
summary(reg4)

linearHypothesis(reg4, c("lths", "hs", "scoll"), test = "F")


