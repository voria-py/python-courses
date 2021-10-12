# Get User input
userNum = int(input("Number for HOP:"))

# User input to String
userNum2Str = str(userNum)


hopList=list()
for i in range(1,69):
    hopList.append(i)
    if i%userNum==0:
        hopList.append("HOP")
        hopList.remove(i)

print(hopList)

hav7list=list()
for x in hopList:
    hav7list.append(str(x))

hav7listStr = list()
for y in hav7list:
    if userNum2Str in y:
        print(y,"=>HOP")
        hav7listStr.append(y)



