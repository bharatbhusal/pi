import nmap3
import os

def get_sentence():
    write = 'ip route | grep / > out_file.txt'
    os.system(write)

def convert(lst):
    return (lst[:].split())

def get_address(numb1, numb2):
    global subnet, my_ip
    with open('out_file.txt') as file:
        contents = file.read()
        get_address.subnet = convert(contents)[numb1]
        get_address.my_ip = convert(contents)[numb2]
        os.remove("out_file.txt")

def comman_in_ip():
    global for_loop
    count = 0
    for_loop = ""
    for a in get_address.my_ip:
        for_loop += str(a)
        if a == ".":
            count += 1
            if count == 3:
                break
    comman_in_ip.for_loop = for_loop

def ip_mac():
    print(f"The IP address of your Raspberry pi for this network is {os_scan.for_loop1}")
    print(f"The MAC address of your Raspberry pi is {os_scan.mac}\n")
    os.system(f"ssh pi@{os_scan.for_loop1}")

def os_scan():
    global for_loop1, os_results, mac
    nmap = nmap3.Nmap()
    for i in range(100, 110):
        os_scan.for_loop1 = comman_in_ip.for_loop + str(i)
        os_scan.os_results = nmap.nmap_os_detection(os_scan.for_loop1)
        if "error" in os_scan.os_results:
            print(os_scan.os_results["msg"])
            break
        else:
            print(f"Scanning now: {os_scan.for_loop1}")
        if os_scan.for_loop1 in os_scan.os_results and os_scan.os_results[os_scan.for_loop1]["macaddress"] != None:
            os_scan.mac = os_scan.os_results[os_scan.for_loop1]["macaddress"]["addr"]
        else:
            os_scan.mac = ""
        if os_scan.mac == "DC:A6:32:F2:19:BE":
            ip_mac()
            break

get_sentence()
get_address(0, 8)
comman_in_ip()
os_scan()
