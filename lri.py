import random

i = [1,2,3,4,5,6,7,8]
results = [0,0,0,0,0,0,0,0]
Gi=[]
fi=[]
p=[0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]

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
    
def chooseAction():
    choice = random.random()
    runner = 0
    for x in range(len(p)):
        if runner<=choice<(p[x]+runner):
            return x + 1
        else: 
            runner = runner + p[x]
def Lri(runs, checks):
    lam = 0.1
    updateStrengths()
    for j in range(runs):
        action = chooseAction()
        beta = Teacher(action)
        updateStrengths()
        if beta == 0:
            p[action-1]=p[action-1]+lam*(1-p[action-1])
            change = 0
            for j in range(len(p)):
                change = change + p[j]
            change = (change - 1)/7
            for j in range(len(p)):
                if j != (action-1):
                    p[j] = p[j] - change
    #f = open('lri.txt', 'w')
    for j in range(checks):
        #f.write(str(j)+" "+str(action)+'\n')
        results[action-1] = results[action-1] + 1
        action = chooseAction()
        beta = Teacher(action)
        updateStrengths()
        if beta == 0:
            p[action-1]=p[action-1]+lam*(1-p[action-1])
            change = 0
            for j in range(len(p)):
                change = change + p[j]
            change = (change - 1)/7
            for j in range(len(p)):
                if j != (action-1):
                    p[j] = p[j] - change

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
    Lri(20, 5000)
for x in range(len(results)):
    print("Action "+str((x+1))+" chosen "+str(results[x]/500000.0*100)+"% of the time, with strength around: "+str(Gi[x]))