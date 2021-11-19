# pi

This two python programs helps us to use raspberry pi without monitor. From installing the OS to enabling SSH to accessing it in our laptop. 


This program works only on linux.
Remember to sudo su before executing the files.

copy_required_files.py file:
it creates 2 files in the directory.
One for connecting wifi in the raspberry pi 
and another for enabling ssh in the pi.
then it will copy those 2 files in the boot partition of booted sd card.

scan_my_pi.py
this file will guess the ip address of the raspberry pi. we will need ip address to ssh into the pi. 

