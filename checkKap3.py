# booleans = [False, True]

# def dm(b,c):
#     return not(b and c) == (not b) or (not c)

# def dmx(b,c):
#     return not(b and c) == (not b) and (not c)

# def isTautology(a):
#     for i in [True, False]:
#         for j in booleans:
#             if not a(i, j):
#                 return False
#     return True

# print(isTautology(dm))

#### Guessing Game Challenge Kap.3 ############
minNum = -100
maxNum = 100
mid = int()

def consistencyCheck():
    #global minNum, maxNum
    if maxNum < minNum:
        print("You lyer!!")
        return 0
    return 1

print("Think of a number between {} and {}!".format(minNum, maxNum))

i = 0
while True:
    i += 1
    if consistencyCheck() < 1:
        break
    mid = (minNum+maxNum)// 2
    hint = str(input("Is your number greater(>), equal(=) or smaller(<) than " + str(mid) + "?"))
    if hint == "<":
        maxNum = mid - 1
        continue
    elif hint == ">":
        minNum = mid + 1
        continue
    elif hint == "=":
        print("Got it!")
        print("I only needed {} guesses.".format(i))
        break
    else:
        print("You need to type in '<', '>' or '='!")
        continue
