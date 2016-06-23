import random

def settarget():
    k = 0
    targetlist = []

    for i in range(0, 3):
        k = random.randint(0,9)

        targetlist.append(k)

    #print(targetlist)
    targetnum = ''.join(str(e) for e in targetlist)
    return targetnum

def inputpred():

    predict = str('')

    while predict.isdigit() == False or len(predict) != 3:
        predict = str(input("Please insert your predicted number as ### : "))

    else:
        return predict


def calcscore(settarget, predict):
    strike, ball, outt = 0, 0, 0
    predlist = [int(x) for x in str(predict)]
    targetlist = [int(y) for y in str(settarget)]
    for t in range(0, 3):
        if predlist[t] == targetlist[t]:
            strike = strike + 1
        else:
            if predlist[t] in targetlist:
                ball = ball + 1
            else:
                outt = outt + 1

    print("%s STRIKE, %s BALL, %s OUT" % (strike, ball, outt))

    return strike

targetnum = settarget()

score = 0

while score !=3:
    score = calcscore(targetnum, inputpred())
if score == 3:
    print ("Congratulations!")