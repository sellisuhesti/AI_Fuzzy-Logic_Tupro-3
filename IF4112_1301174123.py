import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Datafuzzy():
    def __init__(self, score, decission):
        self.score = float(score)
        self.decission = decission

def fuzzyFollower(countFol):

    follower = []
    # stabil
    if (0 <= countFol and countFol <=20000):
        scoreFuzzy = 1
        follower.append(Datafuzzy(scoreFuzzy, "NANO"))
      
    # turun
    elif (20000 < countFol and countFol <= 30000):
        scoreFuzzy = np.absolute((countFol - 20000) / (30000 - 20000))
        follower.append(Datafuzzy("%.2f" % scoreFuzzy, "NANO"))
      
    # MICRO
    # naik
    if (20000 <= countFol and countFol <= 30000):
        scoreFuzzy = 1 - scoreFuzzy 
        follower.append(Datafuzzy("%.2f" % scoreFuzzy, "MICRO"))
      
    # stabil
    elif (30000 < countFol and countFol < 50000):
        scoreFuzzy = 1
        follower.append(Datafuzzy(scoreFuzzy, "MICRO"))
      
    # turun
    elif (50000 <= countFol and countFol <= 70000):
        scoreFuzzy = np.absolute((countFol - 50000) / (70000 - 50000))
        follower.append(Datafuzzy("%.2f" % scoreFuzzy, "MICRO"))

    # MEDIUM
    # naik
    if (50000 <= countFol and countFol <= 70000):
        scoreFuzzy = 1 - scoreFuzzy
        follower.append(Datafuzzy("%.2f" % scoreFuzzy, "MEDIUM"))
      
  # stabil
    elif (70000 < countFol and countFol <= 80000):
        scoreFuzzy = 1
        follower.append(Datafuzzy(scoreFuzzy, "MEDIUM"))
        
    elif (countFol > 80000):
        scoreFuzzy = np.absolute((countFol - 80000) / (100000 - 80000))
        follower.append(Datafuzzy(scoreFuzzy, "MEDIUM"))
    
    return follower
    
def fuzzyEngagement(countEng):

    engagement = []
    # stabil
    if (0 <= countEng and countEng <= 0.3):
        scoreFuzzy = 1
        engagement.append(Datafuzzy(scoreFuzzy, "NANO"))
      
    # turun
    elif (0.3 < countEng and countEng <= 1.7):
        scoreFuzzy = np.absolute((countEng - 0.31) / (1.7 - 0.31))
        engagement.append(Datafuzzy("%.2f" % scoreFuzzy, "NANO"))
      
    # MICRO
    # naik
    if (0.3 < countEng and countEng <= 1.7):
        scoreFuzzy =  1 - scoreFuzzy # np.absolute((countEng - 0.3) / (1.7 - 0.3))
        engagement.append(Datafuzzy("%.2f" % scoreFuzzy, "MICRO"))

    # turun
    elif (1.7 < countEng and countEng <= 5.7):
        scoreFuzzy = np.absolute((countEng - 1.71) / (5.7 - 1.71))
        engagement.append(Datafuzzy("%.2f" % scoreFuzzy, "MICRO"))

    # MEDIUM
    # naik
    if (1.7 < countEng and countEng <= 5.7):
        scoreFuzzy = 1 - np.absolute((countEng - 1.71) / (5.7 - 1.71))
        engagement.append(Datafuzzy("%.2f" % scoreFuzzy, "MEDIUM"))
      
    # stabil
    elif (5.71 < countEng and countEng <= 10.0):
        scoreFuzzy = 1
        engagement.append(Datafuzzy(scoreFuzzy, "MEDIUM"))
        
    return engagement

# rules
def fuzzyRules(follower, engagement):
    temp_yes = []
    temp_no = []
    
    # jika desicion pertama dari test follower nano
    if (follower[0].decission == "NANO"):
        # dapat minimal score 
        temp_yes.append(min(follower[0].score,engagement[0].score))
        
        # jika  dapat 2 data fuzzy engagement
        if (len(engagement) > 1):
            temp_yes.append(min(follower[0].score,engagement[1].score))
            
    # jika follower micro atau medium                    
    else:
        if (engagement[0].decission == "NANO"):
            temp_no.append(min(follower[0].score, engagement[0].score))
            
        elif (engagement[0].decission == "MICRO"):
            if (follower[0].decission == "MICRO"):
                temp_yes.append(min(follower[0].score, engagement[0].score))
            else:
                temp_no.append(min(follower[0].score,engagement[0].score))
                
        else:
            temp_yes.append(min(follower[0].score, engagement[0].score))
            
        # Jika dapat 2 data fuzzy engagement 
        if (len(engagement) > 1):
            if (engagement[1].decission == "MICRO"):
                temp_no.append(min(follower[0].score, engagement[1].score))
                
            elif (engagement[0].decission == "MICRO"):
                if (follower[0].decission == "MICRO"):
                    temp_yes.append(min(follower[0].score, engagement[1].score))
                else:
                    temp_no.append(min(follower[0].score,engagement[1].score))
                    
            else:
                temp_yes.append(min(follower[0].score, engagement[1].score))
                
    # jika dapat 2 data fuzzy follower                   
    if (len(follower) > 1):
        # jika pilihan kedua followernya nano
        if (follower[1].decission == "NANO"):
            temp_yes.append(min(engagement[0].score,follower[1].score))  
            
            if (len(engagement) > 1):
                temp_yes.append(min(engagement[1].score,follower[1].score))
                
        # pilihan kedua follower nya micro atau medium
        else:
            if (engagement[0].decission == "NANO"):
                temp_no.append(min(follower[1].score, engagement[0].score))
                
            elif (engagement[0].decission == "MICRO"):
                if (follower[1].decission == "MICRO"):
                    temp_yes.append(min(follower[1].score, engagement[0].score))
                else:
                    temp_no.append(min(follower[1].score,engagement[0].score))
                    
            #jika dapat 2 data fuzzy engagement
            if (len(engagement) > 1):
                if (engagement[1].decission == "NANO"):
                    temp_no.append(min(follower[1].score, engagement[1].score))
                    
                elif (engagement[1].decission == "MICRO"):
                    if (follower[1].decission == "MICRO"):
                        temp_yes.append(min(follower[1].score, engagement[1].score))
                    else:
                        temp_no.append(min(follower[1].score,engagement[1].score))
    
    return temp_yes, temp_no

# Hasil
def getResult(resultYes, resultNo):
    yes = 0
    no = 0
    if(not resultYes and not resultNo):
        print("NO and YES is Error")
    else:
        if(resultNo):
            if (len(resultNo) > 1):
                no = max(resultNo)
            else:
                no = float(resultNo[0])

        if(resultYes):
            if(len(resultYes) > 1):
                yes = max(resultYes)
            else:
                yes = float(resultYes[0])
    return yes, no

def finalDecission(yes, no):
    sugeno = ((no * 60) + (yes * 80)) / (no + yes)
    return sugeno

def mainFunction(followerCount, engagementRate):
    follower = fuzzyFollower(followerCount)
    engagement = fuzzyEngagement(engagementRate)
    
    resultYes, resultNo = fuzzyRules(follower, engagement)
    yes, no = getResult(resultYes, resultNo)
    
    return finalDecission(yes, no)

data = pd.read_csv('influencers.csv')
hasil = []
for i in range (len(data)):
    hasil.append([data.loc[i, 'id'], mainFunction(data.loc[i, 'followerCount'], data.loc[i, 'engagementRate'])])
hasil.sort(key=lambda x:x[1], reverse=True)
print("HASIL")
print(*hasil, sep='\n')

chosen = pd.DataFrame(hasil[:20], columns=['ID', 'Score'])
chosen.to_csv('choosen.csv')





xa = [0,20000,30000]
ya = [1, 1, 0]
xb = [20000,30000,50000,70000]
yb = [0,1,1,0]
xc = [50000,70000,80000]
yc = [0, 1, 1]
plt.plot(xa, ya, label='jelek')
plt.plot(xb, yb, label='sedang')
plt.plot(xc, yc, label='bagus')
plt.show()

o.close()       
k =input()  
