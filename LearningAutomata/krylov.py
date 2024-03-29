import random

i = [1,2,3,4,5,6,7,8]
results = [0,0,0,0,0,0,0,0]
Gi=[]
fi=[]

def mapStrengths():
    for x in i:
        if(len(Gi)==0):
            Gi.append(x)
        else:
            Gi.insert(random.randrange(0, len(Gi)+1), x)

def addNoise():
    return random.gauss(0,0.7)

def updateStrengths():
    fi.clear()
    for x in Gi:
        h = addNoise()
        temp = ((3*x)/2)+h
        fi.append(temp)

def defineAction(action):
    if action%3 == 0:
        return action//3
    elif action%3 == 1:
        return (action + 2)//3
    else:
        return (action + 1)//3
    
def Krylov(runs, checks):
    updateStrengths()
    action = 3
    for j in range(runs):
        beta = Teacher(defineAction(action))
        updateStrengths()
        if beta == 0:
            if action%3 != 0:
                action = action - 1
        if beta == 1:
            phi =  random.randint(0, 1)
            if phi == 0:
                if action%3 != 0:
                    action = action - 1
            else:
                if action%3 == 0:
                    if action != 24:
                        action = action + 3
                    else:
                        action = 3
                else:
                    action = action + 1
    #f = open('kry.txt', 'w')
    for j in range(checks):
        #f.write(str(j)+" "+str(defineAction(action))+'\n')
        results[defineAction(action)-1] = results[defineAction(action)-1] + 1
        beta = Teacher(defineAction(action))
        updateStrengths()
        if beta == 0:
            if action%3 == 0:
                action = action - 2
            elif action%3 == 2:
                action = action - 1
        if beta == 1:
            if action%3 == 0:
                if action != 24:
                    action = action + 3
                else:
                    action = 3
            else:
                action = action + 1

def Teacher(action):
    answer = 0
    for x in range(0,len(fi)):
        if fi[answer] < fi[x]:
            answer = x
    if answer+1 == action:
        return 0
    else:
        return 1
        

mapStrengths()
for j in range(100):
    Krylov(15000, 5000)
for x in range(len(results)):
    print("Action "+str((x+1))+" chosen "+str(results[x]/500000.0*100)+"% of the time, with strength around: "+str(Gi[x]))
