passNum = input()
passList = []
for x in range(int(passNum)):
    passWrd = input()
    passList.append(passWrd)
for y in range(len(passList)):
    a = passList[y][::-1]
    if a in passList:
        out = passList[y]
print(len(passList[y]), out[len(out) // 2])