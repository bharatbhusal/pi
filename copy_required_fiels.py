import os

def write_lines(arg1, arg2):
    file = open(arg1, "w")
    file.writelines(arg2)
    file = open(arg1)
    read_file(arg1)

def create_file(arg):
    create_file.file = open(arg, "x")

def read_file(arg):
    file = open(arg, "r")
    read_file.message = file.read()

def save_credentials(args):
    cmd = f"nmcli device wifi show-password > {args}"
    os.system(cmd)
    read_file(args)
    os.remove(args)

def get_text():
    new = read_file.message.split("\n")
    lst = {}
    for i in new:
        j = i.split(": ")
        if len(j) >= 2:
            lst[j[0]]= j[1]
    ssid = lst["SSID"]
    password = lst["Password"]
    get_text.text_list = [

f'''country=us
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={{
 scan_ssid=1
 ssid="{ssid}"
 psk="{password}"
}}'''
]



file_name = "wpa_supplicant.conf"
save_credentials("wifi.txt")
get_text()
try:
    create_file("ssh")
    create_file(file_name)
    write_lines(file_name, get_text.text_list)
except FileExistsError:
    write_lines(file_name, get_text.text_list)


print(f'''
Two files have been created for you.
One is for enabling ssh in your Raspberry Pi
And the other is for auto connecting to the Wifi.

Just copy these files and paste them in the boot partation of the micro SD card which has your Raspberry Pi OS.
Enjoy your day!!!'''
)