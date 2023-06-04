from itertools import product
import math

def parseResults(numDice):
    if (numDice == 0):
        print("Dice cannot be 0!")
        return
    
    diceResults = list(product(range(1,7), repeat = abs(numDice)))
    resDict = dict()

    for res in diceResults:
        nums = [0, 0, 0, 0, 0, 0] # number of dice face results
        
        for num in res:
            nums[num - 1] += 1

        # parse through nums and find the result of the roll
        if (numDice < 0):
            actualResult = 7
        else:
            actualResult = 0
        i = 0
        while (i < len(nums)):
            if (numDice > 0 and nums[i] * (i+1) > actualResult):
                actualResult = nums[i] * (i+1)
            elif (numDice < 0 and (nums[i] != 0 and (i+1) < actualResult)):
                actualResult = (i+1)
            i += 1

        #print(str(nums) + " has a result of : " + str(actualResult))
        #print(res)
        #print()

        if actualResult not in resDict:
            resDict[actualResult] = 1
        else:
            resDict[actualResult] += 1

    return resDict
            

print("Input the number of dice to see the probabilities of: ")
K = int(input())

#res = list(product(range(1,7), repeat = K))

#print("The constructed dice Combinations : " + str(res))

ovaRes = parseResults(K)

#print(sorted(ovaRes.items()))
print("OVA Probabilities (Number of Dice: ", K, ")")
freqVal = 0
freqProb = 0
avg = 0
for item in sorted(ovaRes.items()):
    if freqProb < (item[1] / math.pow(6, abs(K))):
        freqProb = item[1] / math.pow(6, abs(K))
        freqVal = item[0]
    avg += item[0] * (item[1] / math.pow(6, abs(K)))
    print("%d ( %d / %d) : %0.6f" % (item[0], item[1], math.pow(6, abs(K)), item[1] / math.pow(6, abs(K))))

print("Most probable result is %d with a probability of %0.6f" % (freqVal, freqProb))
print("Average roll: %0.6f" % (avg))
