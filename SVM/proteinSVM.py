import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

#0 is a alpha helix
#1 is a beta strand
#2 is a random coil

aminoAcids = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 
              'R', 'S', 'T', 'V', 'W', 'Y']
polarity = [-0.591,-1.343,1.05,1.357,-1.006,-0.384,0.336,-1.239,1.831,-1.019,-0.663,
            0.945,0.189,0.931,1.538,-0.228,-0.032,-1.337,-0.595,0.26]
hydrophobicity = [1.8,2.5,-3.5,-3.5,2.8,-0.4,-3.2,4.5,-3.9,3.8,1.9,-3.5,-1.6,-3.5,
                  -4.5,-0.8,-0.7,4.2,-0.9,-1.3]
helixProp = [0.6,1.1,1,1,1.1,0.8,1.8,1,1.2,0.95,1,1.4,0.8,1,1.4,1,1,0.85,1.35,1.3]
strandProp = [0.7,1,1.6,1.1,1.2,1.05,1.7,0.81,1.1,0.7,0.95,1,1,0.9,1.6,1,0.9,0.75,
              1.4,1.2]
randomProp = [0.8,1.4,1.1,1,1.2,0.9,1.1,0.95,1,1,1.7,1,0.8,1.2,1.5,0.9,0.95,0.8,
              1.4,1.8]

F = open("train.txt", "r")
for i in range(9):
    line = F.readline()
sequences = []
structures = []
while(True):
    if (line[0] == "<" and line[1] == ">"):
        line = F.readline()
        s1 = []
        s2 = []
        while (line.find("end") == -1):
            if(line[0] != "<"):
                s1.append(line[0])
                s2.append(line[2])
            line = F.readline()
        sequences.append(s1)
        structures.append(s2)
        line = F.readline()
        
    if (line == ""):
        break
F.close()



num = 3636
X = []
Y = []
h = 0
s = 0
r = 0

for i in range(len(sequences)):
    for j in range(len(sequences[i])):
        if (structures[i][j] == 'h' and h < num):
            h = h + 1
            Y.append(0)
            p1 = 0
            p2 = 0
            p3 = 0
            p4 = 0
            p5 = 0
            tot = 0
            for n in range(len(aminoAcids)):
                if(aminoAcids[n] == sequences[i][j]):
                    tot = tot + 1
                    p1 = p1 + polarity[n]
                    p2 = p2 + hydrophobicity[n]
                    p3 = p3 + helixProp[n]
                    p4 = p4 + strandProp[n]
                    p5 = p5 + randomProp[n]
                if (j > 0):
                    if (aminoAcids[n] == sequences[i][j-1]):
                        tot = tot + 1
                        p1 = p1 + polarity[n]
                        p2 = p2 + hydrophobicity[n]
                        p3 = p3 + helixProp[n]
                        p4 = p4 + strandProp[n]
                        p5 = p5 + randomProp[n]
                if (j < len(sequences[i])-1):
                    if (aminoAcids[n] == sequences[i][j+1]):
                        tot = tot + 1
                        p1 = p1 + polarity[n]
                        p2 = p2 + hydrophobicity[n]
                        p3 = p3 + helixProp[n]
                        p4 = p4 + strandProp[n]
                        p5 = p5 + randomProp[n]
            X.append([p1/tot, p2/tot, p3/tot, p4/tot, p5/tot])
        elif (structures[i][j] == 'e' and s < num):
            s = s + 1
            Y.append(1)
            p1 = 0
            p2 = 0
            p3 = 0
            p4 = 0
            p5 = 0
            tot = 0
            for n in range(len(aminoAcids)):
                if(aminoAcids[n] == sequences[i][j]):
                    tot = tot + 1
                    p1 = p1 + polarity[n]
                    p2 = p2 + hydrophobicity[n]
                    p3 = p3 + helixProp[n]
                    p4 = p4 + strandProp[n]
                    p5 = p5 + randomProp[n]
                if (j > 0):
                    if (aminoAcids[n] == sequences[i][j-1]):
                        tot = tot + 1
                        p1 = p1 + polarity[n]
                        p2 = p2 + hydrophobicity[n]
                        p3 = p3 + helixProp[n]
                        p4 = p4 + strandProp[n]
                        p5 = p5 + randomProp[n]
                if (j < len(sequences[i])-1):
                    if (aminoAcids[n] == sequences[i][j+1]):
                        tot = tot + 1
                        p1 = p1 + polarity[n]
                        p2 = p2 + hydrophobicity[n]
                        p3 = p3 + helixProp[n]
                        p4 = p4 + strandProp[n]
                        p5 = p5 + randomProp[n]
            X.append([p1/tot, p2/tot, p3/tot, p4/tot, p5/tot])
        elif (structures[i][j] == '_' and r < num):
            r = r + 1
            Y.append(2)
            p1 = 0
            p2 = 0
            p3 = 0
            p4 = 0
            p5 = 0
            tot = 0
            for n in range(len(aminoAcids)):
                if(aminoAcids[n] == sequences[i][j]):
                    tot = tot + 1
                    p1 = p1 + polarity[n]
                    p2 = p2 + hydrophobicity[n]
                    p3 = p3 + helixProp[n]
                    p4 = p4 + strandProp[n]
                    p5 = p5 + randomProp[n]
                if (j > 0):
                    if (aminoAcids[n] == sequences[i][j-1]):
                        tot = tot + 1
                        p1 = p1 + polarity[n]
                        p2 = p2 + hydrophobicity[n]
                        p3 = p3 + helixProp[n]
                        p4 = p4 + strandProp[n]
                        p5 = p5 + randomProp[n]
                if (j < len(sequences[i])-1):
                    if (aminoAcids[n] == sequences[i][j+1]):
                        tot = tot + 1
                        p1 = p1 + polarity[n]
                        p2 = p2 + hydrophobicity[n]
                        p3 = p3 + helixProp[n]
                        p4 = p4 + strandProp[n]
                        p5 = p5 + randomProp[n]
            X.append([p1/tot, p2/tot, p3/tot, p4/tot, p5/tot])
    if(h >= num-1 and r >= num-1 and s >= num-1):
        break
svc = svm.SVC(kernel = 'linear', C=100)
svc.fit(X, Y)


F = open("test.txt", "r")
testSequences = []
testStructures = []
for i in range(9):
    line = F.readline()
while(True):
    if (line[0] == "<" and line[1] == ">"):
        line = F.readline()
        testS1 = []
        testS2 = []
        while (line.find("end") == -1):
            if(line[0] != "<"):
                testS1.append(line[0])
                testS2.append(line[2])
            line = F.readline()
        testSequences.append(testS1)
        testStructures.append(testS2)
        line = F.readline()
        
    if (line == ""):
        break
F.close()
testValues = []
testAnswers = []
for i in range(len(testSequences)):
    for j in range(len(testSequences[i])):
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        p5 = 0
        tot = 0
        for n in range(len(aminoAcids)):
            if(aminoAcids[n] == testSequences[i][j]):
                tot = tot + 1
                p1 = p1 + polarity[n]
                p2 = p2 + hydrophobicity[n]
                p3 = p3 + helixProp[n]
                p4 = p4 + strandProp[n]
                p5 = p5 + randomProp[n]
            if (j > 0):
                if (aminoAcids[n] == testSequences[i][j-1]):
                    tot = tot + 1
                    p1 = p1 + polarity[n]
                    p2 = p2 + hydrophobicity[n]
                    p3 = p3 + helixProp[n]
                    p4 = p4 + strandProp[n]
                    p5 = p5 + randomProp[n]
            if (j < len(testSequences[i])-1):
                if (aminoAcids[n] == testSequences[i][j+1]):
                    tot = tot + 1
                    p1 = p1 + polarity[n]
                    p2 = p2 + hydrophobicity[n]
                    p3 = p3 + helixProp[n]
                    p4 = p4 + strandProp[n]
                    p5 = p5 + randomProp[n]
        testValues.append([p1/tot, p2/tot, p3/tot, p4/tot, p5/tot])
        if (testStructures[i][j] == 'h'):
            testAnswers.append(0)
        elif (testStructures[i][j] == 'e'):
            testAnswers.append(1)
        elif (testStructures[i][j] == '_'):
            testAnswers.append(2)

y = Y
temp = np.array(X)
X_norm = (temp - temp.min())/(temp.max() - temp.min())

lda = LDA(n_components=2) #2-dimensional LDA
lda_transformed = pd.DataFrame(lda.fit_transform(X_norm, y))

#plt.scatter(lda_transformed[y==0][0], lda_transformed[y==0][1], label='Class 1', c='red')

helixX = []
helixY = []
strandX = []
strandY = []
randomX = []
randomY = []
for h in range(len(lda_transformed[0])):
    if (h%75 == 0):
        if(Y[h] == 0):
            helixX.append(lda_transformed[0][h])
            helixY.append(lda_transformed[1][h])
        elif(Y[h] == 1):
            strandX.append(lda_transformed[0][h])
            strandY.append(lda_transformed[1][h])
        elif(Y[h] == 2):
            randomX.append(lda_transformed[0][h])
            randomY.append(lda_transformed[1][h])
        

transHX = np.array(helixX)
transHY = np.array(helixY)
transSX = np.array(strandX)
transSY = np.array(strandY)
transRX = np.array(randomX)
transRY = np.array(randomY)


plt.scatter(transHX, transHY, label='Alpha Helices', c='red', marker='.')
plt.scatter(transSX, transSY, label='Beta Sheets', c='blue', marker='.')
plt.scatter(transRX, transRY, label='Random Coils', c='green', marker='.')

plt.legend()
plt.show()





sum = 0
sumh = 0
sumr = 0
sums = 0
toth = 0
totr = 0
tots = 0
for x in range(len(testValues)):
    prediction = svc.predict([testValues[x]])[0]
    #print('Prediction: ' + str(svc.predict([testValues[x]])))
    #print('Answer: ' + str(testAnswers[x]))
    if(prediction == testAnswers[x]):
        sum = sum + 1
    if(testAnswers[x] == 0):
        if(prediction == testAnswers[x]):
            sumh = sumh + 1
        toth = toth + 1
    if(testAnswers[x] == 1):
        if(prediction == testAnswers[x]):
            sums = sums + 1
        tots = tots + 1
    if(testAnswers[x] == 2):
        if(prediction == testAnswers[x]):
            sumr = sumr + 1
        totr = totr + 1
print("Total Accuracy = " +str(sum/len(testValues)*100))
print("Helix Accuracy = " +str(sumh/toth*100))
print("Strand Accuracy = " +str(sums/tots*100))
print("Random Accuracy = " +str(sumr/totr*100))
