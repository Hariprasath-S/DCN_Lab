import ipaddress,math

ip=input("Enter an IP Address: ")

prefix = ip.split("/")
addr = int(math.pow(2,(32-int(prefix[1]))))

print("IP address:    ",ip)
print("Address space: ",addr)

n = ipaddress.IPv4Network(ip)
print("First Address: ",n[0])
print("Last Address:  ",n[-1])
