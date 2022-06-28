# This is mainly just for me to easily transfer my Gecko codes from
# a Google Doc to a table in .md format

# I won't directly mention this, but use it as you see fit

print("How many colums?")
colNum = int(input())

print("Type everything, including the header row, below. Type \"fi\" to stop")
allInputs = []
line = input()
while (line != "fi"):
    allInputs.append(line)
    line = input()
print()
print()

elementNum = 0
toPrint = ""
for temp in allInputs:
   cell = temp.replace("”", "\"")
   cell = cell.replace("’", "'")
   cell = cell.replace("“", "\"")
   amtSpace = 0
   
   if (elementNum == colNum):
      for i in range(colNum):
         toPrint += ":---"
         if (i != colNum-1):
            toPrint += " | "
      print(toPrint)
      toPrint = ""
      
   while (cell[:3] == "   "):
      amtSpace = amtSpace + 1
      cell = cell[3:]
   
   for i in range(amtSpace):
      toPrint += "&nbsp; "
   toPrint += cell 
   
   if (len(toPrint.split("|")) == colNum):
      print(toPrint)
      toPrint = ""
   else:
      toPrint += " | "

   elementNum = elementNum + 1

print(toPrint)
stall = input()
