library(readr)
install.packages("rmarkdown")
library(rmarkdown)
install.packages(c("digest", "caTools", "bitops"))
tsadata <- read_csv("tsadata.csv")
View(tsadata)
hist(tsadata$TSA, xlab="TSA scores", main="histogram of TSA scores",col="green",border="black")
mean(tsadata$TSA)
sd(tsadata$TSA)
x<-seq(20,100,by=.1)
y<-dnorm(x,mean(tsadata$TSA),sd(tsadata$TSA))
#png(file="dnorm.png")
#plot(x,y)
matplot(x=x, 
        y=cbind(y), 
        type="l",
        lty=1,
        col=c("red"),
        xlab="values",
        ylab="densities",
        main="TSA distribution")
#yes the normal distribution captured the data to a high extent, although 
#the distribution is arguably more weighted towards the left

################################################################
#gendervector<-seq(min(tsadata$Gender),max(tsadata$Gender),by=.1)
#schoolvector<-seq(min(tsadata$SchoolType),max(tsadata$SchoolType),by=.1)
#decisionvector<-seq(min(tsadata$Admit),max(tsadata$Admit),by=.1)

x<-seq(min(tsadata$TSA),max(tsadata$TSA),by=.1)
#x<-seq(20,100,by=.1)
y<-dnorm(x,mean(tsadata$TSA[tsadata$Gender=="F"]),sd(tsadata$TSA[tsadata$Gender=="F"]))
z<-dnorm(x,mean(tsadata$TSA[tsadata$Gender=="M"]),sd(tsadata$TSA[tsadata$Gender=="M"]))
matplot(x=x, 
        y=cbind(y,z), 
        type="l",
        lty=1,
        col=c("red","blue"),
        xlab="values",
        ylab="densities",
        main="females and males")

x<-seq(min(tsadata$TSA),max(tsadata$TSA),20,100,by=.1)
#x<-seq(20,100,by=.1)
y<-dnorm(x,mean(tsadata$TSA[tsadata$SchoolType=="I"]),sd(tsadata$TSA[tsadata$SchoolType=="I"]))
z<-dnorm(x,mean(tsadata$TSA[tsadata$SchoolType=="S"]),sd(tsadata$TSA[tsadata$SchoolType=="S"]))
u<-dnorm(x,mean(tsadata$TSA[tsadata$SchoolType=="O"]),sd(tsadata$TSA[tsadata$SchoolType=="O"]))

matplot(x=x, 
        y=cbind(y,z,u), 
        type="l",
        lty=1,
        col=c("red","blue","black"),
        xlab="values",
        ylab="densities",
        main="The three different school types")

x<-seq(min(tsadata$TSA),max(tsadata$TSA),by=.1)
#x<-seq(20,100,by=.1)
y<-dnorm(x,mean(tsadata$TSA[tsadata$Admit=="0"]),sd(tsadata$TSA[tsadata$Admit=="0"]))
z<-dnorm(x,mean(tsadata$TSA[tsadata$Admit=="1"]),sd(tsadata$TSA[tsadata$Admit=="1"]))

matplot(x=x, 
        y=cbind(y,z), 
        type="l",
        lty=1,
        col=c("red","blue"),
        xlab="values",
        ylab="densities",
        main="Those admitted and not admitted")


#y<-dnorm(x,mean(tsadata$TSA[tsadata$Gender=="F"]),sd(tsadata$TSA[tsadata$Gender=="F"]))
#z<-dnorm(x,mean(tsadata$TSA[tsadata$Gender=="M"]),sd(tsadata$TSA[tsadata$Gender=="M"]))
t.test(tsadata$TSA[tsadata$Gender=="F"],tsadata$TSA[tsadata$Gender=="M"],alternative="less")

#y<-dnorm(x,mean(tsadata$TSA[tsadata$SchoolType=="I"]),sd(tsadata$TSA[tsadata$SchoolType=="I"]))
#z<-dnorm(x,mean(tsadata$TSA[tsadata$SchoolType=="S"]),sd(tsadata$TSA[tsadata$SchoolType=="S"]))
#t.test(y,z,alternative="greater")

t.test(tsadata$TSA[tsadata$SchoolType=="I"],tsadata$TSA[tsadata$SchoolType=="S"],alternative="less")


#y<-dnorm(x,mean(tsadata$TSA[tsadata$Admit==0]),sd(tsadata$TSA[tsadata$Admit==0]))
#z<-dnorm(x,mean(tsadata$TSA[tsadata$Admit==1]),sd(tsadata$TSA[tsadata$Admit==1]))
#t.test(y,z)

t.test(tsadata$TSA[tsadata$Admit==0],tsadata$TSA[tsadata$Admit==1])





