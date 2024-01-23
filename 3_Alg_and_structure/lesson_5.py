denomanations = [1, 2, 5, 10, 20, 50, 100]

def returnChange(change, denomanations):
    toGiveBack = [0] * len(denomanations)
    
    for pos, coin in enumerate(reversed(denomanations)):
        while coin <= change:
            change -= coin
            toGiveBack[pos] += 1
        
    return (toGiveBack)

print(returnChange(60, denomanations))
