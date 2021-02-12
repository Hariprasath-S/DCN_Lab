from arpmodule import findMAC

key = input("Enter a key value:")

Mac = findMAC(key)

if(Mac==0):
    print("There is no corresponding MAC address")
else:
    print("The corresponding MAC address is:",Mac)
