#1BFAFF40000 -80000000
#0x81800000

print("Type starting memory address")
startAddress = input()
print("type all hex numbers for the inital")
inital = input()
print("type all hex numbers for the final")
final = input()
print()
print()

x = 0
val = int(startAddress, base=16)
toPrint1 = ""
toPrint2 = ""
for i in range(0,len(inital)):
    if (inital[i:i+1] != " "):
        if (inital[i:i+1] == final[i:i+1]):
            toPrint1 = toPrint1 + "-"
            toPrint2 = toPrint2 + "-"
        else:
            toPrint1 = toPrint1 + inital[i:i+1]
            toPrint2 = toPrint2 + final[i:i+1]
        
        if ((len(toPrint1)+1)%3 == 0):
            toPrint1 = toPrint1 + " "
            toPrint2 = toPrint2 + " "
            x = x + 1
        if (x == 16):
            print(str(hex(val)))
            print(toPrint1)
            print(toPrint2)
            print()

            toPrint1 = ""
            toPrint2 = ""
            val = val + 16
            x = 0

if (len(toPrint1) > 0):
    print(str(hex(val)))
    print(toPrint1)
    print(toPrint2)

stall = input()
