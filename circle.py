def ConquestCampaign(N, L, battalion):
    a = set()
    a.add(battalion[0])
    pred = battalion[0] - 1
    next = battalion[0] + 1
    count = 0
    boolPred = True
    boolNext = True
    
    while not((boolPred == False) and (boolNext == False)):
        if (pred >= 1):
            a.add(pred)
            pred -= 1
        else:
            boolPred = False
        if (next <= N):
            a.add(next)
            next += 1
        else:
            boolNext = False
        count += 1
    return count
print(ConquestCampaign(6,1,[3]))
