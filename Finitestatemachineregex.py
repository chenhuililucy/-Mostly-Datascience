

## I still don't understand how you can implement the NFA pseudo code in python
#each object can have 1 state active at a time, 
#state machines are created with native enumerate classes


class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []

    def add_state(self, name, handler, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self, cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            raise InitializationError("must call .set_start() before .run()")
        if not self.endStates:
            raise  InitializationError("at least one state must be an end_state")
    
        while True:
            (newState, cargo) = handler(cargo)
            if newState.upper() in self.endStates:
                print("reached ", newState)
                break 
            else:
                handler = self.handlers[newState.upper()]

from statemachine import StateMachine

positive_adjectives = ["great","super", "fun", "entertaining", "easy"]
negative_adjectives = ["boring", "difficult", "ugly", "bad"]

def start_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "Python":
        newState = "Python_state"
    else:
        newState = "error_state"
    return (newState, txt)

def python_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "is":
        newState = "is_state"
    else:
        newState = "error_state"
    return (newState, txt)

def is_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word == "not":
        newState = "not_state"
    elif word in positive_adjectives:
        newState = "pos_state"
    elif word in negative_adjectives:
        newState = "neg_state"
    else:
        newState = "error_state"
    return (newState, txt)

def not_state_transitions(txt):
    splitted_txt = txt.split(None,1)
    word, txt = splitted_txt if len(splitted_txt) > 1 else (txt,"")
    if word in positive_adjectives:
        newState = "neg_state"
    elif word in negative_adjectives:
        newState = "pos_state"
    else:
        newState = "error_state"
    return (newState, txt)

def neg_state(txt):
    print("Hallo")
    return ("neg_state", "")

if __name__== "__main__":
    m = StateMachine()
    m.add_state("Start", start_transitions)
    m.add_state("Python_state", python_state_transitions)
    m.add_state("is_state", is_state_transitions)
    m.add_state("not_state", not_state_transitions)
    m.add_state("neg_state", None, end_state=1)
    m.add_state("pos_state", None, end_state=1)
    m.add_state("error_state", None, end_state=1)
    m.set_start("Start")
    m.run("Python is great")
    m.run("Python is difficult")
    m.run("Perl is ugly")


                 #=============================================================================#



"""Initialize States"""
q0=0
q1=1
q2=2

i=0

finstate=q2  #final state is q2

array=[[[0],[0,1]],[[2],[2]],[[],[]]]  #3d array for state transitions

def accepts(state, word):
    global i
    if i==len(word): #if accept stage is current search stage, that is, the final stage 
        return state==finstate  #if last state is final state accept

    char=word[i]
    i+=1
    int(char) #covert char to int

    nextstates=array[state][char]

    for i in range(len(word)):
        if accepts(nextstates, word):  #recursion
            return True
    return False

def main():
    string= "01" #sample input 
    if accepts(q0, string):
        print("accepts")
    else:
        print("rejects")

main()


################################################################################################################################
 
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
        
