import nmap3
import os
cmd = 'ip route | grep / > out_file.txt'
os.system(cmd)

def convert(lst):
    return (lst[:].split())

with open('out_file.txt') as f:
    contents = f.read()
    subnet = convert(contents)[0]
    my_ip = convert(contents)[8]
    os.remove("out_file.txt")

count = 0
for_loop = ""
for i in my_ip:
    for_loop += str(i)
    if i == ".":
        count += 1
        if count == 3:
            break

nmap = nmap3.Nmap()
for i in range(200, 256):
    for_loop1 = for_loop + str(i)
    os_results = nmap.nmap_os_detection(for_loop1)
    
    if "error" in os_results:
        print(os_results["msg"])
        break
    else:
        print(f"Scanning now: {for_loop1}")
    if for_loop1 in os_results and os_results[for_loop1]["macaddress"] != None:
        mac = os_results[for_loop1]["macaddress"]["addr"]
    else:
        mac = ""
    if mac == "DC:A6:32:F2:19:BE":
        print(f"The IP address of your Raspberry pi for this network is {for_loop1}")
        print(f"The MAC address of your Raspberry pi is {mac}\n")
        os.system(f"ssh pi@{for_loop1}")
        break