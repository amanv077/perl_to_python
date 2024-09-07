# Define the IP components
ip1 = 80
ip2 = 208
ip3 = 192

# Loop through the range of IP addresses
for i in range(ip3, 208):  # Equivalent to $i <= 207
    ip4 = 0
    ip4e = 255
    if i == ip3:
        ip4 = 1
    if i == 207:
        ip4e = 254
    
    for l in range(ip4, ip4e + 1):  # Equivalent to $l <= $ip4e
        print(f"\t- {ip1}.{ip2}.{i}.{l}/20")
