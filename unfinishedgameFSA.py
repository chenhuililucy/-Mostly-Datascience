 
from enum import Enum, auto 

class State(Enum): 
    IDLE=auto() 
    CHASE=auto() 
    ATTACK=auto() 
    DEATH=auto() 

#what the auto function does is that it is a random number generator and it 
#is a unique decorator 

class GameObject: 
    def __init__(self):
        self.__state=States.IDLE

    def setstate(self,state): 
        self.__state=States 
        
