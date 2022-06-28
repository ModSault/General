#This is for having a long list of items inside of 1 cell
#with proper break points. This is mainly for personal use

#I won't mention this directly, but use as you please

print("Type everything, type \"fi\" on a new line to stop")
allInputs = []
line = input()
while (line != "fi"):
   allInputs.append(line)
   line = input()
print()
print()

toPrint = ""
for line in allInputs:
   toPrint += line
   toPrint += " <br /> "
print(toPrint[0:len(toPrint)-8])

stall = input()
