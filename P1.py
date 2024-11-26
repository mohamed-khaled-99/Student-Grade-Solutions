# tracking steps
# Allow user input steps
steps = input("Enter Steps, \" Separated \" by spaces\n")
# split the steps to convert to int
stepsSplit = steps.split()
# cnovert to string
stepConvert = map(int, stepsSplit)
# lists the steps
stepsList = list(stepConvert)
# print max steps
maxSteps = max(stepsList)
print("Max steps: ", maxSteps)
# print min steps
minSteps = min(stepsList)
print("Min steps: ", minSteps)
#calculate avverage steps
averageSteps = sum(stepsList) / len(stepsList)
print("avverage steps: ", averageSteps)
# sort the steps max to min
sortedSteps = sorted(stepsList, reverse=True)
print("Sorted steps: ", sortedSteps)
